from abc import ABC, abstractmethod
from typing import Dict, Optional
import pandas as pd


class Strategy(ABC):
    """Base class for all trading strategies"""

    def __init__(self, params: Optional[Dict] = None):
        self.params = params or {}
        self.name = self.__class__.__name__

    @abstractmethod
    def generate_signals(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Generate trading signals based on price data.

        Args:
            data: DataFrame with OHLCV data

        Returns:
            DataFrame with added 'signal' column (1=buy, -1=sell, 0=hold)
        """
        pass

    @abstractmethod
    def get_required_indicators(self) -> list:
        """Return list of indicators needed for this strategy"""
        pass

    def validate_data(self, data: pd.DataFrame) -> bool:
        """Validate that data has required columns"""
        # Use capitalized column names as returned by yfinance
        required = ['Open', 'High', 'Low', 'Close', 'Volume']
        return all(col in data.columns for col in required)