import pandas as pd
import yfinance as yf

def data_fetcher(ticker_symbol):
    data = yf.download(ticker_symbol, start='2018-01-01', end='2023-12-31')
    if 'Close' not in data.columns:
        raise ValueError("DataFrame must contain 'Close' column.")
    return data

#print(data.head())