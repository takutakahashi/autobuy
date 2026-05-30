import ccxt

def from_jpy(ticker, jpy):
    tmap = {
        "ETH_JPY": "ETH/JPY",
        "BTC_JPY": "BTC/JPY"
    }
    exchange = ccxt.bitbank()
    ticker_data = exchange.fetch_ticker(tmap[ticker])
    ltp = ticker_data["last"]
    return round(float(jpy) / ltp, 4) - 0.0001
