# Alpha Strategy with Technical Indicators

## Strategy Overview

This project builds a long-short equity strategy using machine learning on technical indicators. It selects top/bottom S&P 500 stocks and predicts short-term returns using an ensemble of Logistic Regression, KNN, and LSTM models.

---

## Data Pipeline

- **Data Source**: S&P 500 stocks via `yfinance`
- **Period**:
  - Train: 2019–2022  
  - Validation: 2023  
  - Test: 2024
- **Selection**: Top & bottom 50 tickers by return (training window)
- **Market Regime**: Defined by 200-day moving average of S&P 500

---

## Feature Engineering

Each stock includes:
- `sma_ratio`: SMA20 / SMA50 - 1  
- `rsi`: 14-day RSI  
- `macd_hist`: MACD histogram  
- `volatility`: 30-day rolling return std (annualized)  
- `bb_width`: Bollinger Band width  
- `arima_forecast`: 21-day ahead return (ARIMA)  
- `regime`: Bull/Bear indicator  
- Labels: Forward 21-day return quantiles (`-1`, `0`, `1`)

---

## Model Training

- **Logistic Regression**: Multinomial classifier on scaled features  
- **KNN**: k=5 neighbors  
- **LSTM**: Sequence model on 20-day windows, outputting 3-class softmax  
- Models trained on `2019–2022`, validated on `2023`

---

## Performance Comparison

- **Ensemble**: Average of predictions from LR, KNN, and LSTM  
- **Portfolio**: Monthly top 10 long / bottom 10 short stocks  
- **Backtest (2024)**:
  - Return: **-1.97%**
  - Volatility: **5.40%**
  - Sharpe: **-0.74**
  - Max Drawdown: **-5.46%**

**S&P 500 (2024)**:
- Return: **26.99%**
- Volatility: **10.21%**
