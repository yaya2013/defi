import pandas as pd
import pandas_datareader as pdr
import numpy as np
import matplotlib.pyplot as plt

# 设置股票代码和时间范围
stock_code = 'AAPL'
start_date = '2019-01-01'
end_date = '2020-12-31'

# 获取股票数据
df = pdr.get_data_yahoo(stock_code, start=start_date, end=end_date)

# 计算简单移动平均线（SMA）
window = 20
df['SMA'] = df['Close'].rolling(window=window).mean()

# 计算收益率
df['Returns'] = df['Close'].pct_change()

# 生成交易信号
df['Signal'] = np.where(df['Close'] > df['SMA'], 1, -1)

# 计算累积收益率
df['Cumulative Returns'] = (1 + df['Returns']).cumprod()

# 绘制收益曲线和交易信号
plt.figure(figsize=(10, 6))
plt.plot(df['Cumulative Returns'], label='Cumulative Returns')
plt.plot(df['Signal'], marker='o', linestyle='', label='Signal')
plt.legend()
plt.title('Stock Trading Strategy')
plt.xlabel('Date')
plt.ylabel('Cumulative Returns')
plt.show()
