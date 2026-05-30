import ccxt
import os

def market_buy(ticker, amount):
    return buy(ticker, amount, "market", None)
def buy(ticker, amount, trade_type, price):
    tmap = {
        "ETH_JPY": "ETH/JPY",
        "BTC_JPY": "BTC/JPY"
    }
    exchange = ccxt.bitbank()
    exchange.apiKey = os.environ.get("BITBANK_API_KEY")
    exchange.secret = os.environ.get("BITBANK_API_SECRET")
    return exchange.create_order (tmap[ticker], trade_type, 'buy', amount, price)