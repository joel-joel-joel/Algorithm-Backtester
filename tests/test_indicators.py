import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pandas as pd
import pytest
from indicators import sma, ema, rsi

def test_sma():
    data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    result = sma(data, 3)
    assert result[2] == 2.0
    assert result[5] == 5.0

def test_ema():
    data = pd.Series([1, 2, 3, 4, 5])
    result = ema(data, 3)
    assert len(result) == len(data)
    assert result.iloc[-1] > result.iloc[0]

def test_rsi():
    data = pd.Series([100, 102, 101, 103, 102, 105, 104, 106])
    result = rsi(data, 7)
    assert len(result) == len(data)
