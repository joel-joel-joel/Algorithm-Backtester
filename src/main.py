import argparse
import sys
import os

sys.path.insert(0, os.path.dirname(__file__))

from data_loader import fetch_data, prepare_data
from indicators import sma
from signals import ma_crossover_signals
from backtester import Backtester
from metrics import total_return, cagr, max_drawdown, volatility, sharpe_ratio, win_rate
from plotter import plot_price_and_sma, plot_equity_curve, plot_drawdown
import pandas as pd


def main(symbol="AAPL",
         start="2018-01-01",
         end="2025-01-01",
         short_window=50,
         long_window=200):
    print(f"Backtesting {symbol} from {start} to {end}")

    # Fetch data
    print("Fetching data...")
    data = fetch_data(symbol, start, end)
    data = prepare_data(data)
    prices = data["Close"]

    # Calculate indicators
    print("Calculating indicators...")
    sma_short = sma(prices, short_window)
    sma_long = sma(prices, long_window)

    # Generate signals
    print("Generating signals...")
    signals = ma_crossover_signals(sma_short, sma_long)

    # Run backtest
    print("Running backtest...")
    bt = Backtester(initial_cash=10000, fee_per_trade=0)
    equity_curve = bt.run(prices, signals)

    # Calculate metrics
    returns = equity_curve.pct_change().dropna()
    final_value = bt.get_final_value()
    total_ret = total_return(equity_curve)
    cagr_val = cagr(equity_curve)
    max_dd = max_drawdown(equity_curve)
    vol = volatility(returns)
    sharpe = sharpe_ratio(returns)
    win_rt = win_rate(bt.trades)

    # Print results
    print("\n=== BACKTEST RESULTS ===")
    print(f"Final Value: ${final_value:.2f}")
    print(f"Total Return: {total_ret:.2f}%")
    print(f"CAGR: {cagr_val:.2f}%")
    print(f"Max Drawdown: {max_dd:.2f}%")
    print(f"Volatility: {vol:.2f}%")
    print(f"Sharpe Ratio: {sharpe:.4f}")
    print(f"Win Rate: {win_rt:.2f}%")
    print(f"Number of Trades: {len(bt.trades)}")

    # Create results directory
    os.makedirs("results", exist_ok=True)

    # Generate charts
    print("\nGenerating charts...")
    plot_price_and_sma(prices,
                       sma_short,
                       sma_long,
                       short_window,
                       long_window,
                       save_path="results/price_sma.png")
    plot_equity_curve(equity_curve, save_path="results/equity_curve.png")
    plot_drawdown(equity_curve, save_path="results/drawdown.png")
    print("Charts saved to results/ directory")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--symbol", default="AAPL", help="Stock symbol")
    parser.add_argument("--start", default="2018-01-01", help="Start date")
    parser.add_argument("--end", default="2025-01-01", help="End date")
    parser.add_argument("--short",
                        type=int,
                        default=50,
                        help="Short MA window")
    parser.add_argument("--long", type=int, default=200, help="Long MA window")

    args = parser.parse_args()
    main(args.symbol, args.start, args.end, args.short, args.long)
