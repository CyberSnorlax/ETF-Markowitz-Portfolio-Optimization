# 🧠 Generating Alpha Strategies Using Machine Learning

This project explores the use of machine learning to develop profitable **alpha-generating trading strategies** by integrating technical indicators, fundamental financial metrics, and market news sentiment. 
Each branch will contain a different alpha strategy which have already been ML-trained and back-tested against the S&P for 2024 performances.

---

## 📌 Project Objectives

We aim to answer the following key questions:

1. Which combination of **technical indicators**, **fundamental metrics**, and **news sentiment features** yields the best predictive power for alpha generation?
2. Which **machine learning algorithms** are most effective for forecasting asset price movements?
3. How can we **mitigate overfitting** in noisy financial data?
4. What is the impact of **different time horizons** (monthly vs. weekly) on strategy performance?

---

## Successful Alphas 
**[Alpha 2](https://github.com/CyberSnorlax/ETF-Markowitz-Portfolio-Optimization/tree/Alpha2)** 
- Long: Stocks trading above 200-day SMA, with ROE > 20% and Debt/Equity < 1
- Short: Stocks trading below 200-day SMA, with ROE < 10% and Debt/Equity > 2

**Alpha 3 (Under Training)**
- Long: ROIC > sector median Debt/Equity ↓ 10% YoY. 6-month price momentum > sector 75th percentile. RSI(14) < 60 (avoid overbought).
- Short: ROIC < sector 25th percentile. Debt/Equity ↑ 10% YoY. 6-month price momentum < sector 25th percentile. RSI(14) > 40 (avoid oversold rebounds).

---

## 📊 Data Sources

### 📈 Technical Indicators

- **Source**: Yahoo Finance / Alpha Vantage  
- **Examples**: SMA, EMA, RSI, MACD, Bollinger Bands  
- **Access**: Public APIs (5-10 years of historical data)

### 📉 Fundamental Data

- **Source**: Yahoo Finance, public filings  
- **Metrics**: P/E ratio, EPS, revenue growth, debt-to-equity ratio  

---

## 🛠️ Methodology

### 🔍 Preprocessing

- Clean and normalize numeric data  
- Encode categorical variables  
- Handle missing values  

### 🧪 Feature Engineering

- Combine technical and fundamental indicators  
- Add lagged features (e.g., 5-day returns)  
- Generate interaction terms (e.g., RSI × sentiment)

### 🧠 Model Training

We will explore:

- **Random Forest**, **XGBoost**, **LightGBM** for non-linear relationships  
- **RNN/LSTM** for temporal dependencies  
- **Ensemble models** combining KNN, Logistic Regression, etc.

**Validation**: Time-series cross-validation to prevent data leakage

### 📈 Evaluation Metrics

- **Sharpe Ratio**  
- **Annualized Returns**  
- **Maximum Drawdown**

**Backtesting** will be used to assess real-world performance

---

## 🔧 Optimization

- Hyperparameter tuning via Grid Search or Bayesian Optimization  
- Comparison of models across different time horizons


