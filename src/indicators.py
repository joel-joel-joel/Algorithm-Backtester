import pandas as pd
import numpy as np

def sma(data, window):
    return data.rolling(window=window).mean()

def ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

def rsi(data, window=14):
    delta = data.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=window).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=window).mean()
    rs = gain / loss
    rsi = 100 - (100 / (1 + rs))
    return rsi
