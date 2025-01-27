import pandas as pd
import numpy as np
import yfinance as yf
import cvxpy as cp

# Define assets and download historical data
assets = ['QQQ', 'TLT', 'DIA', 'SPY', 'GLD']
close = yf.download(assets, start="2020-01-01", end="2025-01-01")['Close']

# Calculate daily returns
returns = close.pct_change().dropna()

# Display basic statistics of daily returns
print(returns.describe())

# Covariance matrix
cov_matrix = returns.cov()

# Risk aversion parameter
risk_aversion = 0.35

# Define variables
n_assets = len(assets)
weights = cp.Variable(n_assets)  # Portfolio weights
expected_returns = returns.mean()

# Define portfolio variance and expected return
portfolio_variance = cp.quad_form(weights, cov_matrix)
portfolio_return = weights @ expected_returns

# Objective: Minimize risk and maximize return
objective = cp.Minimize(risk_aversion * portfolio_variance - (1 - risk_aversion) * portfolio_return)

#  constraints
constraints = [
    cp.sum(weights) == 1,  # Weights sum to 1
    weights >= 0           # No short selling
]

# Solve the optimization problem
problem = cp.Problem(objective, constraints)
problem.solve()

# Get the optimal weights
optimal_weights = weights.value
print("Optimal Weights:", optimal_weights)

# Calculate CML
risk_free_rate = 0.02  # Risk-free rate (e.g., 2%)
market_return = portfolio_return # Market portfolio return (e.g., 8%)
market_risk = portfolio_variance

# Sharpe Ratio
sharpe_ratio = (market_return - risk_free_rate) / market_risk
print(f"Sharpe Ratio (Slope of CML): {sharpe_ratio:.2f}")

# Generate portfolio risks (standard deviations)
portfolio_risks = np.linspace(0, 0.25, 100)  # Range of risks from 0% to 25%

# Calculate portfolio returns on the CML
portfolio_returns = risk_free_rate + sharpe_ratio * portfolio_risks

# Plot the CML
plt.figure(figsize=(8, 6))
plt.plot(portfolio_risks, portfolio_returns, label="CML (Efficient Portfolios)", color="blue")
plt.scatter([market_risk], [market_return], color="red", label="Market Portfolio", zorder=5)
plt.axhline(y=risk_free_rate, color="gray", linestyle="--", label="Risk-Free Rate")

# Labels and legend
plt.title("Capital Market Line (CML)")
plt.xlabel("Portfolio Risk (Standard Deviation)")
plt.ylabel("Portfolio Return")
plt.legend()
plt.grid(True)
plt.show()  
