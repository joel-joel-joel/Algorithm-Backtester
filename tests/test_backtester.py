import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pandas as pd
import pytest
from backtester import Backtester

def test_backtester():
    index = pd.date_range("2020-01-01", periods=6)
    prices = pd.Series([100, 101, 102, 103, 104, 105], index=index)
    signals = pd.Series([0, 1, 0, -1, 0, 0], index=index)
    bt = Backtester(initial_cash=1000)
    equity = bt.run(prices, signals)
    assert len(equity) > 0
    assert equity.iloc[-1] > 0
