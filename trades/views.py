from rest_framework import generics, authentication, permissions
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from .models import Trade
from .serializers import TradeSerializer
from prices.models import Price
from django.contrib.auth import get_user_model

class TradePostView(generics.CreateAPIView):
    serializer_class = TradeSerializer
    authentication_classes = ()
    permission_classes = ()

    def create(self, request, *args, **kwargs):
        asset_id = request.data.get('asset')
        volume = request.data.get('volume')
        buy_sell = request.data.get('buy_sell')

        # Get latest price for the asset
        latest_price = Price.objects.filter(
            asset_id=asset_id).order_by('-timestamp').first()

        # Set execution timestamp to now
        execution_timestamp = timezone.now()

        # Calculate the execution price
        execution_price = latest_price.price if latest_price else None

        # Create the trade with the retrieved price and timestamp
        trade = Trade.objects.create(
            asset_id=asset_id,
            volume=volume,
            buy_sell=buy_sell,
            execution_timestamp=execution_timestamp
        )

        # Serialize the trade object and return the response
        serializer = self.get_serializer(trade)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
