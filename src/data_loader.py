import pandas as pd
import yfinance as yf
from datetime import datetime

def load_csv(filepath):
    """Load data from CSV file."""
    df = pd.read_csv(filepath, index_col=0, parse_dates=True)
    return df

def fetch_data(symbol, start, end):
    """Fetch historical data from Yahoo Finance."""
    df = yf.download(symbol, start=start, end=end)
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.droplevel('Ticker')
    return df

def prepare_data(df):
    """Ensure datetime index and sort."""
    df.index = pd.to_datetime(df.index)
    df = df.sort_index()
    return df
