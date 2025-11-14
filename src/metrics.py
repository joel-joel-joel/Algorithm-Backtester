import pandas as pd
import numpy as np

def total_return(equity_curve):
    return ((equity_curve.iloc[-1] - equity_curve.iloc[0]) / equity_curve.iloc[0]) * 100

def cagr(equity_curve, periods_per_year=252):
    if len(equity_curve) < 2:
        return 0
    years = len(equity_curve) / periods_per_year
    if years > 0:
        return (((equity_curve.iloc[-1] / equity_curve.iloc[0]) ** (1 / years)) - 1) * 100
    return 0

def max_drawdown(equity_curve):
    running_max = equity_curve.expanding().max()
    drawdown = (equity_curve - running_max) / running_max
    return drawdown.min() * 100

def volatility(returns, periods_per_year=252):
    return returns.std() * np.sqrt(periods_per_year) * 100

def sharpe_ratio(returns, risk_free_rate=0.02, periods_per_year=252):
    excess_returns = returns - (risk_free_rate / periods_per_year)
    if returns.std() == 0:
        return 0
    return (excess_returns.mean() / returns.std()) * np.sqrt(periods_per_year)

def win_rate(trades):
    if not trades:
        return 0
    profitable = sum(1 for t in trades if t.get("profit", 0) > 0)
    return (profitable / len(trades)) * 100 if len(trades) > 0 else 0
