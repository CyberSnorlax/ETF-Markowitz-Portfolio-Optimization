# 📈 AlphaStrategy-SP500

A machine learning–driven long-short equity strategy over the S&P 500 universe. Combines technical indicators and fundamental filters to forecast monthly stock returns and construct a rebalanced portfolio with alpha potential.

---

## 🚀 Strategy Overview

This strategy aims to exploit persistent signals in both fundamentals and price action:

- **Long**: Stocks trading **above** 200-day SMA, with **ROE > 20%** and **Debt/Equity < 1**
- **Short**: Stocks trading **below** 200-day SMA, with **ROE < 10%** and **Debt/Equity > 2**

Each month:
- The top 10 and bottom 10 stocks are selected based on **ML model forecasts**
- The portfolio is equally weighted and **rebalanced monthly**
- Returns are compared to the **S&P 500 benchmark**

---

## 🔄 Data Pipeline

- **Price Data**: Daily OHLCV prices for all S&P 500 tickers from Yahoo Finance (`yfinance`)
- **Fundamentals**: ROE and Debt/Equity ratios scraped via `yfinance.info`
- **Index Data**: S&P 500 (^GSPC) used as benchmark and market regime indicator
- **Resampling**: Daily data is resampled to monthly frequency for portfolio returns

---

## ⚙️ Feature Engineering

Each stock is enhanced with a rich set of features:

- **Technical Indicators**:
  - RSI, MACD histogram, Bollinger Band width, volatility, SMA ratios
  - Binary flag: price above or below 200-day SMA
- **Fundamental Filters**:
  - ROE and Debt/Equity used for long/short selection
- **Market Regime**: S&P 500 trend state as macro overlay
- **Labeling**: Forward 1-month return → categorized into 3 classes: ↑ outperform, → neutral, ↓ underperform

---

## 🤖 Model Training

### Structure
- Split into **Train (2019–2022)**, **Validation (2023)**, **Test (2024)**
- Features are standardized using `StandardScaler`

### Ensemble of 3 Models:
1. **Logistic Regression**  
2. **K-Nearest Neighbors (KNN)**  
3. **LSTM Neural Network (TensorFlow)**

Predictions are aggregated to form an ensemble score → top 10 long / bottom 10 short are selected each month.

---

## 📊 Performance Comparison

### ✅ Strategy (2024 Out-of-Sample Results):

| Metric                | Value     |
|-----------------------|-----------|
| Total Return          | 88.4%     |
| Annualized Return     | 99.5%     |
| Annualized Volatility | 28.2%     |
| Sharpe Ratio          | 3.46      |
| Max Drawdown          | –12.5%    |

### 📉 Benchmark: S&P 500 (2024)

- Barely positive cumulative return
- Significantly underperformed the long-short strategy


