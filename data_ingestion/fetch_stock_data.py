import yfinance as yf
import pandas as pd
import os
from datetime import datetime

TICKERS = ['AAPL']
DATA_DIR = "data"

def fetch_stock_data(ticker, period = '1d', interval = '1m'):
    stock = yf.Ticker(ticker)
    data = stock.history(period = period, interval = interval)
    return data


def save_to_csv(data, ticker):
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    
    filename = f"{DATA_DIR}/{ticker}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
    data.to_csv(filename)
    print(f"Data saved to {filename}")

if __name__ == "__main__":
    for ticker in TICKERS:
        print(f"Fetching data for {ticker}...")
        data = fetch_stock_data(ticker)
        print(data.head())
        save_to_csv(data,ticker)
    