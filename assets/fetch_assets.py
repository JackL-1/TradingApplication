import finnhub
from assets.models import Asset
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TradingApplication.settings")
django.setup()

finnhub_client = finnhub.Client(
    api_key="cguhu6pr01qu2uq60r50cguhu6pr01qu2uq60r5g")


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




# # print(finnhub_client.stock_symbols('US')[0:5])
