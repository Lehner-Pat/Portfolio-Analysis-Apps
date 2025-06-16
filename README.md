# 📊 Portfolio Analysis Apps

This repository contains **two complementary financial analytics tools**, built in Python, that demonstrate different approaches to analyzing portfolio performance:

---

## 🔹 1. `portfolio-analysis-tableau`  
**Command-line app for historical analysis**

### 📌 Description  
A lightweight script that pulls **daily historical prices** from the [Twelve Data API](https://twelvedata.com/), computes portfolio metrics from a defined starting point, and exports the results as **Tableau-ready CSV files**.

### ✅ Features
- Assets: `BTC/EUR`, `USD/EUR`, `MCD/EUR`
- Assumes **€10,000 investment per asset** starting **01.01.2023**
- Computes:
  - Daily asset returns
  - Portfolio cumulative value
  - Annualized volatility, variance
  - **Sharpe Ratio** and **Sortino Ratio**
  - Correlation & Covariance matrices
- Outputs:
  - `historical_prices.csv` (raw prices)
  - `portfolio_analysis.csv` (metrics + portfolio values)

### 📁 Folder: `historical_analysis_csv/`  
This folder contains:
- `main.py` — entry point  
- `/app/` — modular code in MVC-like style  
- `/data/` — CSV outputs

---

## 🔹 2. `portfolio-dashboard-flask`  
**Flask-based API for live portfolio stats**

### 📌 Description  
A modular **Flask web application** using MVC architecture to fetch **live financial data** and serve portfolio insights via JSON or downloadable CSV.

### ✅ Features
- Pulls live daily prices from Twelve Data API
- Computes and returns:
  - Asset return
  - Volatility
  - Correlation & Covariance
  - Portfolio variance & std. dev.
- Custom weight input via query params (e.g., `?btc=0.6&usd=0.4`)
- API endpoints:
  - `/api/data` – Returns JSON of KPIs
  - `/api/export` – Downloads raw data as CSV
- Easily extendable for dashboard frameworks or frontend use

### 🧱 Tech
- Flask
- pandas
- requests

### 📁 Folder: `live_dashboard_mvc/`

---

## 🚀 Getting Started

### 🔧 Requirements
Create and activate a virtual environment, then:

```bash
pip install -r requirements.txt
