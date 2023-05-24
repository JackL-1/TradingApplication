import os
import finnhub
import django
from assets.models import Asset
from dotenv import load_dotenv

load_dotenv()
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "trading_applicaiton.settings")
django.setup()


finnhub_client = finnhub.Client(api_key=os.getenv('API_KEY'))


def fetch_assets():
    asset_data = finnhub_client.stock_symbols('US')

    for asset in asset_data:
        ticker = asset['symbol']
        name = asset['description']
        product = asset['type']

        # Check if the asset already exists in the database
        if not Asset.objects.filter(ticker=ticker).exists():
            # Create a new asset record
            Asset.objects.create(ticker=ticker, name=name, product=product)


fetch_assets()
#print(finnhub_client.stock_symbols('US')[0:5])
