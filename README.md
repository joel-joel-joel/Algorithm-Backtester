# Algorithmic Trading Backtester

## Overview
A simple complete Python-based algorithmic trading backtesting framework for testing MA crossover strategies on historical stock data.

## Why I Made This
Wanted to build a smaller scale python/finance related project. An attempt to apply fundamental algorithmic trading concepts and try building a testing framework. Built this on Repilt. 

## Tech Stack

| Component | Technology | Purpose |
|-----------|------------|---------|
| Language | Python 3.12.5 | Core logic and calculations |
| Data Source | yfinance | Yahoo Finance API integration |
| Data Processing | pandas, NumPy | Time series analysis |
| Visualization | matplotlib | Chart generation |
| Testing | pytest | Unit testing framework |

## Key Features & Implementation Details

### 1. Modular Architecture
- **Data Layer** (`data_loader.py`): Yahoo Finance integration with CSV fallback support
- **Indicators** (`indicators.py`): Technical indicator library (SMA, EMA, RSI)
- **Signals** (`signals.py`): Strategy signal generation logic
- **Backtester** (`backtester.py`): Core execution engine with trade tracking
- **Metrics** (`metrics.py`): Comprehensive performance calculations
- **Plotter** (`plotter.py`): Visualization suite for analysis

### 2. Historical Data Management
- **Yahoo Finance Integration:** Downloads OHLCV data for any ticker via `yfinance`
- **Date Range Flexibility:** Customizable start/end dates via command-line arguments
- **Data Preparation:** Automatic datetime indexing and chronological sorting
- **CSV Support:** Alternative data loading from local files

### 3. Technical Indicators
```python
# Simple Moving Average
def sma(data, window):
    return data.rolling(window=window).mean()

# Exponential Moving Average
def ema(data, window):
    return data.ewm(span=window, adjust=False).mean()

# Relative Strength Index
def rsi(data, window=14):
    # Momentum oscillator calculation
```

### 4. Trading Strategy
- **MA Crossover Logic:** Buy when short MA crosses above long MA, sell when it crosses below
- **Signal Generation:** Returns series of 1 (buy), -1 (sell), 0 (hold)
- **No Lookahead Bias:** Signals use only data available at each timestamp
- **Extensible Framework:** Base `Strategy` class for implementing custom strategies

### 5. Backtesting Engine
- **Trade Execution:** Simulates buy/sell orders with configurable fees
- **Position Management:** Tracks cash, shares, and portfolio value over time
- **Trade History:** Records all transactions with dates, prices, and quantities
- **Equity Curve:** Generates time series of portfolio value

```python
class Backtester:
    def __init__(self, initial_cash=10000, fee_per_trade=0):
        # Initialize with starting capital and optional fees
        
    def run(self, prices, signals):
        # Execute backtest and return equity curve
```

### 6. Performance Metrics
Comprehensive analysis suite in `metrics.py`:
- **Total Return:** Overall percentage gain/loss
- **CAGR:** Compound Annual Growth Rate (annualized return)
- **Max Drawdown:** Largest peak-to-trough decline (risk measure)
- **Volatility:** Annualized standard deviation of returns
- **Sharpe Ratio:** Risk-adjusted return (excess return per unit of risk)
- **Win Rate:** Percentage of profitable trades

### 7. Visualization Suite
Three chart types saved to `results/` directory:
- **Price & SMA Chart** (`price_sma.png`): Historical prices with MA overlays
- **Equity Curve** (`equity_curve.png`): Strategy performance over time
- **Drawdown Analysis** (`drawdown.png`): Visual risk representation

  
### 8. Web Frontend (Flask UI)

The Flask-based UI allows users to:

- Enter a stock symbol, start/end dates, and moving average windows via an HTML form.  
- Submit the form to run the backtest directly in the browser.  
- View metrics such as **Total Return**, **CAGR**, **Max Drawdown**, **Sharpe Ratio**, and **Win Rate**.  
- Generate charts (**Price + MA overlay**, **Equity Curve**, **Drawdown**) saved in the `results/` folder each time a new backtest is run.  

Future enhancements will include interactive charts using **Plotly.js**.

### Launching the Web UI

Run the following command in your project directory:
```bash
python app.py
```

Then open the Replit web preview or navigate to:  
[http://localhost:8080](http://localhost:8080)

### Form Fields

| Field           | Description                              | Example    |
|-----------------|------------------------------------------|------------|
| Stock Symbol    | Stock ticker to backtest                 | AAPL       |
| Start Date      | Start of historical data (YYYY-MM-DD)    | 2018-01-01 |
| End Date        | End of historical data (YYYY-MM-DD)      | 2025-01-01 |
| Short MA Window | Number of days for short moving average  | 20         |
| Long MA Window  | Number of days for long moving average   | 50         |

### Example Usage

After submitting the form, the page will display:

```bash
Backtest Results
Total Return: 0.18
CAGR: 0.11
Max Drawdown: -0.12
Sharpe Ratio: 1.20
Win Rate: 0.57
```


### Generated Charts

Charts are automatically generated and saved in the `results/` folder:

- `price_sma.png` – Historical price with short/long MA overlays  
- `equity_curve.png` – Portfolio value over time  
- `drawdown.png` – Drawdown periods highlighted  

These charts are updated every time a new backtest is run, so the folder always contains the latest results.

### Notes

- The web UI uses a simple HTML form and Flask backend.  
- No JavaScript or chart libraries are required initially, but **Plotly.js** can be added later for interactive charts.  
- The backend reuses the same `Backtester` class, ensuring consistency between the CLI and web results.



## Setup

### 1. Create a Virtual Environment (Recommended)
```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

**On Windows:**
```bash
venv\Scripts\activate
```

**On Mac/Linux:**
```bash
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

Required packages:
- `pandas` - Data manipulation
- `numpy` - Numerical computations
- `yfinance` - Yahoo Finance API
- `matplotlib` - Plotting
- `pytest` - Testing framework

## Usage

### Basic Backtest
```bash
python src/main.py --symbol AAPL --start 2018-01-01 --end 2025-01-01 --short 50 --long 200
```

### Command-Line Arguments
- `--symbol`: Stock ticker symbol (default: `AAPL`)
- `--start`: Start date in YYYY-MM-DD format (default: `2018-01-01`)
- `--end`: End date in YYYY-MM-DD format (default: `2025-01-01`)
- `--short`: Short moving average window in days (default: `50`)
- `--long`: Long moving average window in days (default: `200`)

### Example Commands
```bash
# Test Tesla with 20/50 day MAs
python src/main.py --symbol TSLA --short 20 --long 50

# Backtest S&P 500 over 10 years
python src/main.py --symbol SPY --start 2015-01-01 --end 2025-01-01

# Quick test with 10/30 day crossover
python src/main.py --symbol MSFT --short 10 --long 30
```

## Running Tests
```bash
pytest -v
```

Tests cover:
- Indicator calculations
- Signal generation logic
- Backtester execution
- Metrics accuracy

## Output

### Console Output
```
=== BACKTEST RESULTS ===
Final Value: $15,234.56
Total Return: 52.35%
CAGR: 8.92%
Max Drawdown: -18.42%
Volatility: 22.15%
Sharpe Ratio: 0.8734
Win Rate: 56.25%
Number of Trades: 16
```

### Generated Charts
Saved to `results/` directory:
- `price_sma.png` - Price history with short/long MA lines
- `equity_curve.png` - Portfolio value over time
- `drawdown.png` - Drawdown periods highlighted in red


## Future Enhancements
- Multi-timeframe analysis (daily, hourly, minute data)
- Additional indicators (Bollinger Bands, MACD, Stochastic)
- Multiple strategy comparison framework
- Portfolio optimization and asset allocation
- Risk management features (stop-loss, take-profit, position sizing)
- Walk-forward analysis for robustness testing
- Parameter optimization with grid search/genetic algorithms
- Live trading integration with broker APIs
- Web dashboard for interactive backtesting

## Contact
**Email:** leojongenli@gmail.com  
**LinkedIn:** [linkedin.com/in/joel-ong-2b82a3362](https://www.linkedin.com/in/joel-ong-2b82a3362/)
