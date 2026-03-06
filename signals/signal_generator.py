def moving_average_signal(data):
    clean = data.dropna(subset=["MA20", "MA50"])
    if clean.empty:
        return "HOLD"

    latest = clean.iloc[-1]
    ma20 = float(latest["MA20"])
    ma50 = float(latest["MA50"])

    if ma20 > ma50:
        return "BUY"

    elif ma20 < ma50:
        return "SELL"

    return "HOLD"


def rsi_signal(data, lower=30, upper=70):
    clean = data.dropna(subset=["RSI14"])
    if clean.empty:
        return "HOLD"

    latest = clean.iloc[-1]
    rsi_value = float(latest["RSI14"])

    if rsi_value < lower:
        return "BUY"

    elif rsi_value > upper:
        return "SELL"

    return "HOLD"


def combined_signal(data):
    ma_sig = moving_average_signal(data)
    rsi_sig = rsi_signal(data)

    if ma_sig == rsi_sig and ma_sig != "HOLD":
        return ma_sig

    if ma_sig == "HOLD":
        return rsi_sig

    if rsi_sig == "HOLD":
        return ma_sig

    return "HOLD"
