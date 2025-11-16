"""
Financial Data Analysis Project
Basic stock data analysis using Python
"""

import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt

# Get stock data
tickers = ['AAPL', 'TSLA', 'MSFT']
data = yf.download(tickers, start='2024-01-01', end='2024-06-01')['Close']

print("📈 Financial Data Analysis")
print("=" * 40)

# Calculate daily returns
returns = data.pct_change()

# Basic analysis
print("\n📊 Performance Summary (2024 YTD):")
for ticker in tickers:
    total_return = (data[ticker][-1] / data[ticker][0] - 1) * 100
    print(f"{ticker}: {total_return:.2f}%")

# Simple visualization
plt.figure(figsize=(10, 6))
for ticker in tickers:
    plt.plot(data.index, data[ticker] / data[ticker][0], label=ticker)

plt.title('Stock Performance (Normalized)')
plt.xlabel('Date')
plt.ylabel('Normalized Price')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('stock_performance.png')
plt.show()

print("\n✅ Analysis complete! Check 'stock_performance.png'")
