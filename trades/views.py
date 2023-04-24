from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.utils import timezone
from .models import Trade, Asset
from .serializers.common import TradeSerializer
from prices.models import Price
from django.contrib.auth import get_user_model
from users.authentication import JWTAuthentication
from decimal import Decimal
from rest_framework.views import APIView
from .models import Trade

from prices.fetch_prices import fetch_price, start_scheduler
from trades.serializers.common import TradeSerializer

class TradesView(APIView):

    serializer_class = TradeSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get(self, request):
          
        user_trades = Trade.objects.filter(user=request.user)
        serialized_trades = TradeSerializer(user_trades, many=True)
        return Response({"TradeData": serialized_trades.data})


class TradePreConfirm(APIView):
    # serializer_class = TradeSerializer
    # authentication_classes = (JWTAuthentication,)
    # permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        asset_ticker = request.data.get('ticker')
        quantity = request.data.get('quantity')
        buy_sell = request.data.get('buy_sell')

        try:
            asset = Asset.objects.get(ticker=asset_ticker)
        except Asset.DoesNotExist:
            return Response({"error": "Asset not found"}, status=status.HTTP_404_NOT_FOUND)
        # fetches the latest quote to be displayed
        fetch_price(asset_ticker)
        latest_price = Price.objects.filter(
            asset=asset).order_by('-timestamp').first()

        if not latest_price:
            # Fetch the price
            fetched_price = fetch_price(asset_ticker)

            # Save the fetched price to the database
            price = Price(asset=asset, price=fetched_price)
            price.save()

            if fetched_price is None:
                return Response({"error": f"price not found for {asset_ticker}"})
            # Return the fetched price
            return Response({"price": fetched_price}, status=status.HTTP_200_OK)

        # Return the pre confirm of trade request
        return Response({
            f'Trade Pre confirm:'
            f"buy_sell": buy_sell,
            f"quantity": quantity,
            f"ticker": asset_ticker,
            f"price": latest_price.price}, status=status.HTTP_200_OK)


class TradePostView(generics.CreateAPIView):
    serializer_class = TradeSerializer
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        asset_ticker = request.data.get('ticker')
        quantity = request.data.get('quantity')
        buy_sell = request.data.get('buy_sell')

        # Get latest price for the asset
        try:
            asset = Asset.objects.get(ticker=asset_ticker)
        except Asset.DoesNotExist:
            return Response({"error": "Asset not found"}, status=status.HTTP_404_NOT_FOUND)

        latest_price = Price.objects.filter(
            asset=asset).order_by('-timestamp').first()
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
            asset=asset,
            quantity=quantity,
            buy_sell=buy_sell,
            execution_timestamp=execution_timestamp,
            execution_price=execution_price
        )

        # Subtract trade_value from funds
        request.user.funds -= trade_value
        request.user.save()

        # Start the scheduler to retrieve regular prices which will trigger the pnl to be tracked
        start_scheduler(asset_ticker)

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
