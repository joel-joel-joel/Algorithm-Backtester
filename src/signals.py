import pandas as pd

def ma_crossover_signals(sma_short, sma_long):
    signals = pd.Series(0, index=sma_short.index)
    signals[sma_short > sma_long] = 1
    signals[sma_short < sma_long] = -1
    return signals

def generate_trades(signals):
    trades = signals.diff()
    return trades
