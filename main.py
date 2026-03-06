from utils.data_loader import load_stock_data
from indicators.moving_average import calculate_ma
from indicators.rsi import calculate_rsi
from signals.signal_generator import moving_average_analysis, rsi_analysis, combined_analysis

print("IDX Technical Signal Generator")
print("Method: MA20/MA50 crossover + RSI14 (30/70)")
print("Final signal combines MA and RSI.")

ticker = input("Stock ticker (BBCA, BBRI, etc): ")

data = load_stock_data(ticker)

data["MA20"] = calculate_ma(data, 20)
data["MA50"] = calculate_ma(data, 50)
data["RSI14"] = calculate_rsi(data, 14)

ma_sig, ma_reason = moving_average_analysis(data)
rsi_sig, rsi_reason = rsi_analysis(data)
signal, final_reason = combined_analysis(data)

print("MA Signal:", ma_sig)
print("MA Reason:", ma_reason)
print("RSI Signal:", rsi_sig)
print("RSI Reason:", rsi_reason)
print("Trading Signal (MA + RSI):", signal)
print("Final Reason:", final_reason)
