def run_analysis(df):
    import numpy as np
    import pandas as pd
    import os

    # Daily returns
    returns = df.pct_change().dropna()

    # Rebased investment value per asset
    initial_investment = 30000
    investment = df.copy()
    for col in df.columns:
        first_price = df[col].iloc[0]
        investment[col] = (df[col] / first_price) * initial_investment

    # Portfolio metrics
    weights = np.array([1/3, 1/3, 1/3])
    portfolio_returns = returns.dot(weights)
    portfolio_cumulative = investment.dot(weights)

    # Annualized stats
    trading_days = 252
    avg_return = portfolio_returns.mean() * trading_days
    volatility = portfolio_returns.std() * np.sqrt(trading_days)
    sharpe_ratio = avg_return / volatility

    # Sortino Ratio calculation
    negative_returns = portfolio_returns[portfolio_returns < 0]
    downside_std = negative_returns.std() * np.sqrt(trading_days)
    sortino_ratio = avg_return / downside_std if downside_std != 0 else np.nan

    summary = {
        "Annualized Return": round(avg_return, 4),
        "Annualized Volatility": round(volatility, 4),
        "Sharpe Ratio": round(sharpe_ratio, 4),
        "Sortino Ratio": round(sortino_ratio, 4),
        "Correlation Matrix": returns.corr(),
        "Covariance Matrix": returns.cov(),
    }

    # Save for Tableau
    full_output = pd.concat([
        df,
        returns.add_suffix('_returns'),
        investment.add_suffix('_value'),
        portfolio_returns.rename('Portfolio_Return'),
        portfolio_cumulative.rename('Portfolio_Value')
    ], axis=1)

    output_csv_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'portfolio_analysis.csv')
    full_output.to_csv(output_csv_path)
    print(f"📄 Tableau-ready file saved to: {output_csv_path}")

    return summary
