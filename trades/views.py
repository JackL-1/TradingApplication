from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Trade
from .serializers import TradeSerializer
from prices.models import Price
from django.contrib.auth import get_user_model
from users.authentication import JWTAuthentication
from decimal import Decimal


class TradePostView(generics.CreateAPIView):
    serializer_class = TradeSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        asset_id = request.data.get('asset')
        quantity = request.data.get('quantity')
        buy_sell = request.data.get('buy_sell')

        # Get latest price for the asset
        latest_price = Price.objects.filter(
            asset_id=asset_id).order_by('-timestamp').first()
        
        if not latest_price:
            return Response({'detail': 'Asset price not found'}, status=status.HTTP_404_NOT_FOUND)

        # Set execution timestamp to now
        execution_timestamp = timezone.now()

        # Calculate the execution price
        execution_price = latest_price.price

        # Create the trade with the retrieved price and timestamp
        trade = Trade.objects.create(
            user=request.user,  # Add the user to the trade
            asset_id=asset_id,
            quantity=quantity,
            buy_sell=buy_sell,
            execution_timestamp=execution_timestamp,
            execution_price=execution_price
        )

        # Serialize the trade object and return the response
        serializer = self.get_serializer(trade)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def get_queryset(self, user_id):
        return Trade.objects.filter(user_id=user_id)

