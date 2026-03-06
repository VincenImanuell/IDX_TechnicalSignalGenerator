def moving_average_signal(data):
    latest = data.iloc[-1]

    if latest["MA20"] > latest["MA50"]:
        return "BUY"

    elif latest["MA20"] < latest["MA50"]:
        return "SELL"

    return "HOLD"