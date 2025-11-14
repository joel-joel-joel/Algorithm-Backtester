from typing import Dict, Optional
import pandas as pd
from strategy import Strategy
from indicators import sma


class MAcrossoverStrategy(Strategy):
    """Moving Average Crossover Strategy

    Generates buy/sell signals based on crossover of short and long moving averages.
    - Buy signal: short MA crosses above long MA (golden cross)
    - Sell signal: short MA crosses below long MA (death cross)
    """

    def __init__(self, params: Optional[Dict] = None):
        """Initialize MA crossover strategy

        Args:
            params: Dictionary with 'short_window' (default 50) and 'long_window' (default 200)
        """
        super().__init__(params)
        self.params.setdefault('short_window', 50)
        self.params.setdefault('long_window', 200)

    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """Generate MA crossover signals

        Args:
            data: DataFrame with 'close' price column

        Returns:
            DataFrame with 'short_ma', 'long_ma', and 'signal' columns
        """
        # Make a copy to avoid modifying original
        df = data.copy()

        # Calculate indicators
        df['short_ma'] = sma(df['close'], self.params['short_window'])
        df['long_ma'] = sma(df['close'], self.params['long_window'])

        # Generate signals (initialize all to 0)
        df['signal'] = 0

        # Detect crossovers using shift to get previous bar values
        # Buy signal: short crosses above long
        buy_signal = (df['short_ma'] > df['long_ma']) & (
            df['short_ma'].shift(1) <= df['long_ma'].shift(1))
        # Sell signal: short crosses below long
        sell_signal = (df['short_ma'] < df['long_ma']) & (
            df['short_ma'].shift(1) >= df['long_ma'].shift(1))

        # Apply signals (this naturally handles NaN as False in boolean indexing)
        df.loc[buy_signal, 'signal'] = 1
        df.loc[sell_signal, 'signal'] = -1

        # Fill any remaining NaN in signal column from shift operations
        df['signal'] = df['signal'].fillna(0)

        return df

    def get_required_indicators(self) -> list:
        """Return required indicators for this strategy

        Returns:
            List of indicator names: ['SMA']
        """
        return ['SMA']
