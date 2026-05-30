# coding: UTF-8
from lib import parser
from autobuy import calc
from autobuy import bitbank


if __name__ == '__main__':
    args = parser.get_args()
    amount = calc.from_jpy(ticker=args.ticker, jpy=args.jpy)
    print(bitbank.market_buy(ticker=args.ticker, amount=amount))
