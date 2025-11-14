import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import pandas as pd
import pytest
from signals import ma_crossover_signals

def test_ma_crossover():
    sma_short = pd.Series([10, 11, 12, 13, 14])
    sma_long = pd.Series([9, 10, 11, 12, 13])
    signals = ma_crossover_signals(sma_short, sma_long)
    assert signals[0] == 1  # Buy
    assert signals[4] == 1  # Buy
