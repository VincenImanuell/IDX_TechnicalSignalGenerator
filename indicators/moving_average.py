def calculate_ma(data, period):
    return data['Close'].rolling(period).mean()