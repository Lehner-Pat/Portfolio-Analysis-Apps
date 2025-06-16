import pandas as pd
import numpy as np
from app.models.data_model import fetch_asset_data

def get_all_data(weights):
    df = fetch_asset_data()  # Returns a DataFrame with datetime index and price columns
    returns = df.pct_change().dropna()  # Daily returns

    # Calculate stats
    cov_matrix = returns.cov()
    corr_matrix = returns.corr()
    port_variance = np.dot(weights, np.dot(cov_matrix, weights))
    port_std_dev = np.sqrt(port_variance)
    asset_returns = returns.mean()
    volatility = returns.std()

    results = {
        "asset_returns": asset_returns.to_dict(),
        "volatility": volatility.to_dict(),
        "correlation_matrix": corr_matrix.to_dict(),
        "covariance_matrix": cov_matrix.to_dict(),
        "weights": dict(zip(df.columns, weights)),
        "portfolio_variance": port_variance,
        "portfolio_std_dev": port_std_dev
    }

    return results
