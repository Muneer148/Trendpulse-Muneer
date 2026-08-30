import matplotlib.pyplot as plt
import pandas as pd

from task1_data_collection import get_trending_coins

coins = get_trending_coins()
df = pd.DataFrame(coins)
df = df.sort_values('price_change_24h', ascending = False)

plt.barh(df['name'],df['price_change_24h'])
plt.xlabel('price_change_24h (%)')
plt.ylabel('Coin Name')
plt.title('TrendPulse - Trending Coin Price Changes')
plt.show()