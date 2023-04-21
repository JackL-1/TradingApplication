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
from rest_framework.views import APIView


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

        # Calculate the Trade Value 
        execution_price = latest_price.price
        trade_value = latest_price.price * Decimal(str(quantity))

        # Check if trade value is <= funds
        if trade_value > request.user.funds:
            return Response({'detail': 'Insufficient funds'}, status=status.HTTP_400_BAD_REQUEST)

        # Create the trade with the retrieved price and timestamp
        trade = Trade.objects.create(
            user=request.user,  # Add the user to the trade
            asset_id=asset_id,
            quantity=quantity,
            buy_sell=buy_sell,
            execution_timestamp=execution_timestamp,
            execution_price=execution_price
        )

        # Subtract trade_value from funds
        request.user.funds -= trade_value
        request.user.save()

        # Serialize the trade object and return the response
        serializer = self.get_serializer(trade)
        return Response({'detail': 'Trade booked', 'data': serializer.data}, status=status.HTTP_201_CREATED)



class ExitTradeView(APIView):
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def delete(self, request, *args, **kwargs):
        # Retrieve the trade object using the trade ID provided in the URL
        try:
            trade = Trade.objects.get(id=kwargs['trade_id'], user=request.user)
        except Trade.DoesNotExist:
            return Response({'detail': 'Trade not found'}, status=status.HTTP_404_NOT_FOUND)

        # Calculate the PnL
        pnl = trade.pnl
        print(pnl)

        # Update the user's funds
        request.user.funds += pnl
        request.user.save()

        # Delete the trade
        trade.delete()

        # Return a response indicating the trade has been successfully deleted
        return Response({
        'detail': 'Trade exited successfully',
        'pnl': f'${pnl:.3f}',
    }, status=status.HTTP_200_OK)
    
