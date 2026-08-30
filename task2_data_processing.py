import pandas as pd
from task1_data_collection import get_trending_coins
coins = get_trending_coins()

def process_data(coins):
    df = pd.DataFrame(coins)

    df["market_cap"] = pd.to_numeric(
        df["market_cap"].str.replace("$", "").str.replace(",", "")
    )

    df["total_volume"] = pd.to_numeric(
        df["total_volume"].str.replace("$", "").str.replace(",", "")
    )

    return df

if __name__ == '__main__':
    coins = get_trending_coins()
    df = process_data(coins)

    print(df)
    print('\nData Types:')
    print(df.dtypes)
