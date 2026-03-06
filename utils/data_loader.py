import yfinance as yf

def load_stock_data(ticker, start="2023-01-01"):
    ticker = ticker + ".JK"
    data = yf.download(ticker, start=start)
    return data