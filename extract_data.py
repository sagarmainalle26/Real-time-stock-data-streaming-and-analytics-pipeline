import yfinance as yf
import json

stock_symbols = ['AAPL', 'MSFT']

def fetch_stock_data(stock_symbols):
    stock_data_list = [] 

    for symbol in stock_symbols:
        stock = yf.Ticker(symbol)
        data = stock.history(period='1d', interval='1m')
        latest = data.tail(1)

        if not latest.empty:
            for index, row in latest.iterrows():
                stock_data = {
                    'symbol' : symbol,
                    'timestamp' : str(index),
                    'open' : round(float(row['Open']), 2),
                    'high' : round(float(row['High']),2),
                    'low' : round(float(row['Low']),2),
                    'close' : round(float(row['Close']),2),
                    'volume' : int(row['Volume'])
                }
                stock_data_list.append(stock_data)

    return stock_data_list


