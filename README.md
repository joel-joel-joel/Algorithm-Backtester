# Algorithmic Trading Backtester

## Overview
A complete Python-based algorithmic trading backtesting framework for testing MA crossover strategies on historical stock data.

## Features
- Download historical stock data from Yahoo Finance
- Calculate technical indicators (SMA, EMA, RSI)
- Generate trading signals using MA crossover
- Execute trades on historical data without lookahead bias
- Calculate comprehensive performance metrics (CAGR, Sharpe, Drawdown, etc.)
- Generate visualizations (price charts, equity curves, drawdown charts)
- Unit tests for all components

## Folder Structure
```
algo-backtester/
├── data/
│   └── sample.csv
├── src/
│   ├── data_loader.py   # Data loading and fetching
│   ├── indicators.py    # Technical indicators
│   ├── signals.py       # Signal generation
│   ├── backtester.py    # Backtesting engine
│   ├── metrics.py       # Performance metrics
│   ├── plotter.py       # Visualization
│   └── main.py          # CLI runner
├── tests/
│   ├── test_indicators.py
│   ├── test_signals.py
│   └── test_backtester.py
├── requirements.txt
└── README.md
```

## Strategy Explanation
**Simple MA Crossover**: Buy when short MA crosses above long MA, sell when it crosses below.

## Installation
```bash
pip install -r requirements.txt
```

## Usage
```bash
python src/main.py --symbol AAPL --start 2018-01-01 --end 2025-01-01 --short 50 --long 200
```

### Arguments:
- `--symbol`: Stock ticker (default: AAPL)
- `--start`: Start date (YYYY-MM-DD)
- `--end`: End date (YYYY-MM-DD)
- `--short`: Short MA window (default: 50)
- `--long`: Long MA window (default: 200)

## Running Tests
```bash
pytest -v
```

## Output
- **Console**: Backtest metrics (return, CAGR, Sharpe ratio, etc.)
- **Charts**: Saved to `results/` directory
  - `price_sma.png`: Price with MA lines
  - `equity_curve.png`: Strategy equity over time
  - `drawdown.png`: Drawdown analysis

## Metrics
- **Total Return**: Percentage return of strategy
- **CAGR**: Compound Annual Growth Rate
- **Max Drawdown**: Largest peak-to-trough decline
- **Volatility**: Annualized standard deviation of returns
- **Sharpe Ratio**: Risk-adjusted return
- **Win Rate**: Percentage of profitable trades

## Future Enhancements
- Multi-timeframe analysis
- More indicators (Bollinger Bands, MACD, etc.)
- Portfolio optimization
- Risk management (stop-loss, position sizing)
- Walk-forward analysis
- Parameter optimization
