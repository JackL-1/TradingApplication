
from django.apps import apps
from prices.serializers.common import PriceSerializer
from dotenv import load_dotenv
from django.utils import timezone
import finnhub
import django
import os

load_dotenv()
django.setup()
from apscheduler.schedulers.background import BackgroundScheduler

finnhub_client = finnhub.Client(api_key=os.getenv('API_KEY'))

def fetch_price(ticker):
    response = finnhub_client.quote(ticker)
    timestamp = timezone.now()

    # Check if asset exists, and insert if not
    asset_model = apps.get_model('assets', 'Asset')
    asset = asset_model.objects.get(ticker=ticker)

    # Insert price data with corresponding asset_id
    price_model = apps.get_model('prices', 'Price')
    price_data = price_model( asset=asset, timestamp=timestamp)
    price_data.price = response['c']
    price_data.open_price = response['o']
    price_data.close_price = response['pc']
    price_data.low_price = response['l']
    price_data.high_price = response['h']
    price_data.previous_close = response['pc']
    price_data.change = response['d']
    price_data.percent_change = response['dp']
    
    price_data.save()


# Create a scheduler and add the fetch_price job
scheduler = BackgroundScheduler()


def start_scheduler(ticker):
    existing_jobs = scheduler.get_jobs()

    for job in existing_jobs:
        if job.args[0] == ticker:
            # We use an early return in the case that the job already exists
            return
    # otherwise this block runs
    scheduler.add_job(fetch_price, 'interval', minutes=0.5, args=[ticker])
    scheduler.start()

# scheduler.shutdown()

#print(finnhub_client.quote('AAPL'))
