from django.http import JsonResponse
from django.views import View
import json
from .fetch_prices import fetch_price, start_scheduler


class GetPriceView(View):
    def post(self, request):
        data = json.loads(request.body)
        ticker = data.get('ticker')
        #Calls fetch_price function with the ticker from the client as an arg. 
        # fetching here prevents delay of the schedulers interval.
        #behaviour fetches then waits for interval defined in fetch_prices 
        fetch_price(ticker)
        #Calling our function to also start the scheduler for prices to update at a set interval
        start_scheduler(ticker)

        return JsonResponse({"message": f"Fetched price for {ticker}"})