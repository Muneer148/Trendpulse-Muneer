def analyze_data(df):

    # Top gainer
    top_index = df["price_change_24h"].idxmax()
    top_gainer = df.loc[top_index]

    # Top loser
    bottom_index = df["price_change_24h"].idxmin()
    bottom_loser = df.loc[bottom_index]

    # Highest market cap
    market_cap_index = df["market_cap"].idxmax()
    highest_market_cap = df.loc[market_cap_index]

    # Average 24h price change
    average_change = df["price_change_24h"].mean()

    return {
        "top_gainer": top_gainer,
        "bottom_loser": bottom_loser,
        "highest_market_cap": highest_market_cap,
        "average_change": average_change
    }

if __name__ == "__main__":
    from task2_data_processing import process_data
    from task1_data_collection import get_trending_coins

    coins = get_trending_coins()
    df = process_data(coins)

    analysis = analyze_data(df)

    print("\nTop Gainer:")
    print(analysis["top_gainer"])

    print("\nTop Loser:")
    print(analysis["bottom_loser"])

    print("\nHighest Market Cap:")
    print(analysis["highest_market_cap"])

    print("\nAverage 24h Change:")
    print(analysis["average_change"])