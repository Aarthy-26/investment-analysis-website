import yfinance as yf
import pandas as pd

# Read stock universe from CSV
stocks_df = pd.read_csv("data/stocks_list.csv")

all_data = []

for _, row in stocks_df.iterrows():
    ticker = row["ticker"]
    stock_name = row["stock_name"]

    df = yf.download(
        ticker,
        period="30d",        # rolling window
        interval="1d",
        progress=False
    )

    if df.empty:
        continue

    df = df.reset_index()

    # Vectorized & safe datetime handling
    df["date"] = pd.to_datetime(df["Date"]).dt.strftime("%Y-%m-%d")
    df["stock"] = stock_name

    df = df[["date", "stock", "Open", "High", "Low", "Close", "Volume"]]
    df.columns = ["date", "stock", "open", "high", "low", "close", "volume"]

    all_data.append(df)

# Combine all stocks into one table
final_df = pd.concat(all_data, ignore_index=True)

# Overwrite CSV (no unlimited growth)
final_df.to_csv("data/daily_prices.csv", index=False)

print("✅ Daily stock data updated successfully")
