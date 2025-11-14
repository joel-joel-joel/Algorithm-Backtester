import matplotlib.pyplot as plt
import os

def plot_price_and_sma(prices, sma_short, sma_long, title="Price and SMA", save_path=None):
    plt.figure(figsize=(14, 7))
    plt.plot(prices.index, prices, label="Close Price", color="black", linewidth=2)
    plt.plot(sma_short.index, sma_short, label=f"SMA {len(sma_short)}", color="blue", linewidth=1.5)
    plt.plot(sma_long.index, sma_long, label=f"SMA {len(sma_long)}", color="red", linewidth=1.5)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Price")
    plt.legend()
    plt.grid(True, alpha=0.3)
    if save_path:
        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
        plt.savefig(save_path)
    plt.close()

def plot_equity_curve(equity_curve, title="Equity Curve", save_path=None):
    plt.figure(figsize=(14, 7))
    plt.plot(equity_curve.index, equity_curve, label="Strategy Equity", linewidth=2)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Equity ($)")
    plt.legend()
    plt.grid(True, alpha=0.3)
    if save_path:
        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
        plt.savefig(save_path)
    plt.close()

def plot_drawdown(equity_curve, title="Drawdown", save_path=None):
    running_max = equity_curve.expanding().max()
    drawdown = (equity_curve - running_max) / running_max * 100
    plt.figure(figsize=(14, 7))
    plt.fill_between(drawdown.index, drawdown, 0, color="red", alpha=0.5)
    plt.plot(drawdown.index, drawdown, color="red", linewidth=1)
    plt.title(title)
    plt.xlabel("Date")
    plt.ylabel("Drawdown (%)")
    plt.grid(True, alpha=0.3)
    if save_path:
        os.makedirs(os.path.dirname(save_path) or ".", exist_ok=True)
        plt.savefig(save_path)
    plt.close()
