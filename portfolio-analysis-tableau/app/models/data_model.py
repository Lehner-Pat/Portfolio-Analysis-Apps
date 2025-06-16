import os
import pandas as pd
import requests
from datetime import datetime

API_KEY = "Enter your API key here"
BASE_URL = "https://api.twelvedata.com/time_series"
ASSETS = {
    "BTC/EUR": "BTC/EUR",
    "USD/EUR": "USD/EUR",
    "MCD": "MCD"  # McDonald's ticker from US exchanges
}
START_DATE = "2023-01-01"
OUTPUT_PATH = "data/historical_prices.csv"

def fetch_price_data():
    if os.path.exists(OUTPUT_PATH):
        print("📁 Using cached data.")
        return pd.read_csv(OUTPUT_PATH, parse_dates=["datetime"], index_col="datetime")

    dfs = []
    for label, symbol in ASSETS.items():
        params = {
            "symbol": symbol,
            "interval": "1day",
            "apikey": API_KEY,
            "start_date": START_DATE,
            "format": "JSON",
            "outputsize": 5000
        }
        r = requests.get(BASE_URL, params=params)
        data = r.json()

        if "values" not in data:
            raise ValueError(f"API error for {symbol}: {data.get('message', 'Unknown error')}")

        df = pd.DataFrame(data["values"])
        df["datetime"] = pd.to_datetime(df["datetime"])
        df.set_index("datetime", inplace=True)
        df = df.sort_index()
        df = df.rename(columns={"close": label})
        df = df[[label]].astype(float)
        dfs.append(df)

    full_df = pd.concat(dfs, axis=1).dropna()
    os.makedirs("data", exist_ok=True)
    full_df.to_csv(OUTPUT_PATH)

    return full_df
