from utils.data_loader import load_stock_data
from indicators.moving_average import calculate_ma
from indicators.rsi import calculate_rsi
from signals.signal_generator import moving_average_signal, rsi_signal, combined_signal

print("IDX Technical Signal Generator")
print("Method: MA20/MA50 crossover + RSI14 (30/70)")
print("Final signal combines MA and RSI.")

ticker = input("Stock ticker (BBCA, BBRI, etc): ")

data = load_stock_data(ticker)

data["MA20"] = calculate_ma(data, 20)
data["MA50"] = calculate_ma(data, 50)
data["RSI14"] = calculate_rsi(data, 14)

ma_sig = moving_average_signal(data)
rsi_sig = rsi_signal(data)
signal = combined_signal(data)

latest_rsi = data["RSI14"].dropna()
if latest_rsi.empty:
    rsi_text = "N/A"
else:
    rsi_text = f"{float(latest_rsi.iloc[-1]):.2f}"

print("MA Signal:", ma_sig)
print("RSI Signal:", rsi_sig, f"(RSI14: {rsi_text})")
print("Trading Signal (MA + RSI):", signal)
