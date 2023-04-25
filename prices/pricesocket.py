from assets.models import Asset
from prices.models import Price
import websocket
import json
from datetime import datetime

def on_message(ws, message):
    data = json.loads(message)

    if data['type'] == 'trade':
        # Extract the price and ticker from the first trade in the message
        trade = data['data'][0]
        price = trade['p']
        ticker = trade['s']
        timestamp = datetime.fromtimestamp(trade['t'] / 1000.0)

        # Check if asset exists, and insert if not
        asset, created = Asset.objects.get_or_create(ticker=ticker)

        # Insert price data with corresponding asset_id
        price = Price(price=price, asset=asset, timestamp=timestamp)
        price.save()

    print(message)


def on_error(ws, error):
    print(error)


def on_close(ws):
    print("### closed ###")

# define the tickers of live data feed we wish to subscribe to 
def on_open(ws):
    ws.send('{"type":"subscribe","symbol":"AMZN"}')


if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp(
        "wss://ws.finnhub.io?token=os.getenv('API_KEY')",
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.on_open = on_open
    ws.run_forever()
