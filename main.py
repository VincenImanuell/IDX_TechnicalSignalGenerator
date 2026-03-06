from utils.data_loader import load_stock_data
from indicators.moving_average import calculate_ma
from signals.signal_generator import moving_average_signal

ticker = input("Stock ticker (BBCA, BBRI, etc): ")

data = load_stock_data(ticker)

data["MA20"] = calculate_ma(data, 20)
data["MA50"] = calculate_ma(data, 50)

signal = moving_average_signal(data)

print("Trading Signal:", signal)