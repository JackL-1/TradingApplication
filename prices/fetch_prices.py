import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'your_project_name.settings')
django.setup()

import finnhub
from decimal import Decimal
from datetime import datetime
from assets.models import Asset
from prices.models import Price

from apscheduler.schedulers.background import BackgroundScheduler


finnhub_client = finnhub.Client(
    api_key="cguhu6pr01qu2uq60r50cguhu6pr01qu2uq60r5g")


def fetch_price(ticker):
    response = finnhub_client.quote(ticker)
    price = response['c']
    timestamp = datetime.now()

    # Check if asset exists, and insert if not
    asset, created = Asset.objects.get_or_create(ticker=ticker)

    # Insert price data with corresponding asset_id
    price_data = Price(asset=asset, timestamp=timestamp, price=price)
    price_data.current_price = response['c']
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
scheduler.add_job(fetch_price, 'interval', minutes=0.25, args=['TSLA'])  

# Start the scheduler
scheduler.start()

fetch_price('TSLA')

# print(finnhub_client.quote('TSLA'))
# # print(finnhub_client.stock_symbols('US')[0:5])