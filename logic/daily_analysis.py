import pandas as pd

def analyze_daily_stock(stock_df):
    stock_df = stock_df.sort_values("date")

    stock_df["daily_return"] = stock_df["close"].pct_change() * 100

    avg_daily_return = stock_df["daily_return"].mean()
    volatility = stock_df["daily_return"].std()

    recent_avg = stock_df.tail(5)["daily_return"].mean()

    if recent_avg > 0.5:
        trend = "Uptrend"
    elif recent_avg < -0.5:
        trend = "Downtrend"
    else:
        trend = "Sideways"

    return avg_daily_return, volatility, trend
