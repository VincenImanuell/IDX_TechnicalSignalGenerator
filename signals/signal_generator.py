def moving_average_analysis(data):
    clean = data.dropna(subset=["MA20", "MA50"])
    if clean.empty:
        return "HOLD", "Not enough MA20/MA50 data yet."

    latest = clean.iloc[-1]
    ma20 = float(latest["MA20"])
    ma50 = float(latest["MA50"])

    if ma20 > ma50:
        return "BUY", f"MA20 ({ma20:.2f}) is above MA50 ({ma50:.2f})."

    elif ma20 < ma50:
        return "SELL", f"MA20 ({ma20:.2f}) is below MA50 ({ma50:.2f})."

    return "HOLD", f"MA20 ({ma20:.2f}) is equal to MA50 ({ma50:.2f})."


def moving_average_signal(data):
    signal, _ = moving_average_analysis(data)
    return signal


def rsi_analysis(data, lower=30, upper=70):
    clean = data.dropna(subset=["RSI14"])
    if clean.empty:
        return "HOLD", "Not enough RSI14 data yet."

    latest = clean.iloc[-1]
    rsi_value = float(latest["RSI14"])

    if rsi_value < lower:
        return "BUY", f"RSI14 ({rsi_value:.2f}) is below {lower} (oversold)."

    elif rsi_value > upper:
        return "SELL", f"RSI14 ({rsi_value:.2f}) is above {upper} (overbought)."

    return "HOLD", f"RSI14 ({rsi_value:.2f}) is between {lower}-{upper} (neutral)."


def rsi_signal(data, lower=30, upper=70):
    signal, _ = rsi_analysis(data, lower=lower, upper=upper)
    return signal


def combined_analysis(data):
    ma_sig, ma_reason = moving_average_analysis(data)
    rsi_sig, rsi_reason = rsi_analysis(data)

    if ma_sig == rsi_sig and ma_sig != "HOLD":
        return ma_sig, f"MA and RSI both indicate {ma_sig}. {ma_reason} {rsi_reason}"

    if ma_sig == "HOLD" and rsi_sig == "HOLD":
        return "HOLD", f"Both indicators are neutral or incomplete. {ma_reason} {rsi_reason}"

    if ma_sig == "HOLD":
        return rsi_sig, f"MA is neutral, following RSI: {rsi_sig}. {ma_reason} {rsi_reason}"

    if rsi_sig == "HOLD":
        return ma_sig, f"RSI is neutral, following MA: {ma_sig}. {ma_reason} {rsi_reason}"

    return "HOLD", f"MA and RSI conflict ({ma_sig} vs {rsi_sig}), so final signal is HOLD. {ma_reason} {rsi_reason}"


def combined_signal(data):
    signal, _ = combined_analysis(data)
    return signal
