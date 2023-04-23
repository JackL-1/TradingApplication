from rest_framework.response import Response
from rest_framework.views import APIView
import json
from .models import Price
from .fetch_prices import fetch_price, start_scheduler
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from prices.serializers.common import PriceSerializer

class GetAllPricesView(APIView):
    # permission_classes = (IsAuthenticatedOrReadOnly,)
    def post(self, request):
        data = json.loads(request.body)
        ticker = data.get('ticker')
        #Calls fetch_price function with the ticker from the client as an arg. 
        # fetching here prevents delay of the schedulers interval.
        #behaviour fetches then waits for interval defined in fetch_prices 
        fetch_price(ticker)
        #Calling our function to also start the scheduler for prices to update at a set interval
        start_scheduler(ticker)
        
        prices = Price.objects.all()
        serialized_prices = PriceSerializer(prices, many=True)
        return Response({"message": f"Fetched price for {ticker}", "all prices data": serialized_prices.data})
    
class GetSinglePriceView(APIView):
    #permission_classes = (IsAuthenticatedOrReadOnly,)

    def post(self, request):
        data = json.loads(request.body)
        ticker = data.get('ticker')
        
        # Calls fetch_price function with the ticker from the client as an arg. 
        # Fetching here prevents delay of the scheduler's interval.
        # Behaviour fetches then waits for interval defined in fetch_prices 
        fetch_price(ticker)
        
        # Calling our function to also start the scheduler for prices to update at a set interval
        start_scheduler(ticker)
        
        # Order the prices queryset by the date and time of the price in descending order
        
        latest_price = Price.objects.latest('id')
        
        serialized_price = PriceSerializer(latest_price)
        return Response({"message": f"Fetched price for {ticker}", "latest price data": serialized_price.data})