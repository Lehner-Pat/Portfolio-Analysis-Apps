import pandas as pd
import numpy as np

def calculate_returns(df):
    return df.pct_change().dropna()

def calculate_volatility(returns):
    return returns.std()

def calculate_covariance(returns):
    return returns.cov()

def calculate_correlation(returns):
    return returns.corr()

def calculate_sharpe(returns, risk_free_rate=0.0):
    excess_returns = returns - risk_free_rate
    return excess_returns.mean() / excess_returns.std()

def calculate_portfolio_metrics(returns, weights):
    weights = np.array(weights)
    mean_returns = returns.mean()
    cov_matrix = returns.cov()

    portfolio_return = np.dot(weights, mean_returns)
    portfolio_variance = np.dot(weights.T, np.dot(cov_matrix, weights))
    portfolio_std_dev = np.sqrt(portfolio_variance)

    return {
        "Expected Return": round(portfolio_return, 6),
        "Portfolio Variance": round(portfolio_variance, 6),
        "Portfolio Std. Dev.": round(portfolio_std_dev, 6)
    }
