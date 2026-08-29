import pandas as pd
from task1_data_collection import get_trending_coins
coins = get_trending_coins()

df = pd.DataFrame(coins)
print(df)

df.shape
df.columns
df.info()
df.head()

df["market_cap"] = pd.to_numeric(
    df["market_cap"].str.replace("$", "").str.replace(",", "")
)

df["total_volume"] = pd.to_numeric(
    df["total_volume"].str.replace("$", "").str.replace(",", "")
)

print(df.dtypes)

top_gainer = df.loc[df["price_change_24h"].idxmax()]
top_market_cap = df.loc[df["market_cap"].idxmax()]

print("🔥 TOP GAINER")
print(f"Coin: {top_gainer['name']} ({top_gainer['symbol']})")
print(f"24h Change: {top_gainer['price_change_24h']:.2f}%")

print("\n💰 HIGHEST MARKET CAP")
print(f"Coin: {top_market_cap['name']} ({top_market_cap['symbol']})")
print(f"Market Cap: ${top_market_cap['market_cap']:,}")

top_coins = df.sort_values(
    "price_change_24h",
    ascending=False
)

print(top_coins[["name", "symbol", "price_change_24h"]])