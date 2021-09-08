import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf


tickers = [
    'SHOP',
    'NVDA',
    'AMD',
    'PYPL',
    'MRNA',
    'AAPL',
    'MSFT',
    'TSLA',
    'AMZN',
    '^NDXT',

    '^GSPC',
]
interval = '1mo'
period = '5y'


df = yf.download(tickers=tickers, period=period, interval=interval, rounding=True)

returns = df['Adj Close'].pct_change()
returns  = returns.cumsum() # lol

# std = returns.std()

returns.plot(kind='line')

plt.show()
print('done')
