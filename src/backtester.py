"""Simple backtester for algorithmic trading strategies."""

import pandas as pd


class Backtester:
    """Backtesting engine for trading strategies."""

    def __init__(self, initial_cash=10000, fee_per_trade=0):
        """
        Initialize backtester.

        Args:
            initial_cash: Starting capital
            fee_per_trade: Trading fee per transaction
        """
        self.initial_cash = initial_cash
        self.fee_per_trade = fee_per_trade
        self.cash = initial_cash
        self.shares = 0
        self.trades = []
        self.equity_curve = None

    def run(self, prices, signals):
        """
        Execute backtest on price data with signals.

        Args:
            prices: Series of prices
            signals: Series of signals (1=buy, -1=sell, 0=hold)

        Returns:
            Series representing equity curve
        """
        self.cash = self.initial_cash
        self.shares = 0
        self.trades = []
        equity = []

        for i in range(len(prices)):
            price = prices.iloc[i]
            signal = signals.iloc[i]

            # Buy signal
            if signal == 1 and self.shares == 0:
                shares_to_buy = int(self.cash / price)
                if shares_to_buy > 0:
                    cost = shares_to_buy * price + self.fee_per_trade
                    if cost <= self.cash:
                        self.shares = shares_to_buy
                        self.cash -= cost
                        self.trades.append({
                            'date': prices.index[i],
                            'type': 'buy',
                            'price': price,
                            'shares': shares_to_buy
                        })

            # Sell signal
            elif signal == -1 and self.shares > 0:
                proceeds = self.shares * price - self.fee_per_trade
                self.cash += proceeds
                self.trades.append({
                    'date': prices.index[i],
                    'type': 'sell',
                    'price': price,
                    'shares': self.shares
                })
                self.shares = 0

            # Calculate current equity
            current_equity = self.cash + (self.shares * price)
            equity.append(current_equity)

        self.equity_curve = pd.Series(equity, index=prices.index)
        return self.equity_curve

    def get_final_value(self):
        """Get final portfolio value."""
        if self.equity_curve is not None:
            return self.equity_curve.iloc[-1]
        return self.initial_cash
