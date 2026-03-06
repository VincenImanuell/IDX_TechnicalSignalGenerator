import yfinance as yf
import pandas as pd

def load_stock_data(ticker, start="2023-01-01"):
    ticker = ticker.upper() + ".JK"
    data = yf.download(ticker, start=start, progress=False)

    # yfinance can return MultiIndex columns even for a single ticker.
    # Normalize to one level so downstream code gets scalar values.
    if isinstance(data.columns, pd.MultiIndex):
        data.columns = data.columns.get_level_values(0)

    return data
