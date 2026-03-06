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
