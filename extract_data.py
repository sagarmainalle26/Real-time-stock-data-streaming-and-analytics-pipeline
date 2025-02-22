import yfinance as yf
import json

stock_symbols = ['AAPL', 'MSFT']

def fetch_stock_data(stock_symbols):
    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        data = stock.history(period='1d', interval='1m')
        latest = data.tail(1)

        if not latest.empty:
            for index, row in latest.iterrows():
                stock_data = {
                    'symbol' : symbol,
                    'timestamp' : str(index),
                    'open' : row['Open'],
                    'high' : row['Low'],
                    'close' : row['Close'],
                    'volume' : int(row['Volume'])
                }
                print(json.dumps(stock_data))


fetch_stock_data(stock_symbols)