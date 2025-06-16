from app.models.data_model import fetch_price_data
from app.controllers.analysis_controller import run_analysis

import pandas as pd
import os

if __name__ == "__main__":
    # Fetch historical price data
    df = fetch_price_data()

    # Define path and ensure folder exists
    data_dir = os.path.join(os.path.dirname(__file__), 'app', 'data')
    os.makedirs(data_dir, exist_ok=True)  # ✅ Create folder if missing

    output_path = os.path.join(data_dir, 'historical_prices.csv')

    # Save the data
    df.to_csv(output_path, index=True)
    print(f"✅ Historical price data saved to {output_path}")

    # Run analysis
    results = run_analysis(df)

    # Print the results
    print("\n===== 📊 Portfolio Analysis Results =====")
    for key, value in results.items():
        print(f"\n🔹 {key}:")
        print(value)
