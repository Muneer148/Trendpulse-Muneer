from datetime import datetime
import matplotlib.pyplot as plt

from task1_data_collection import get_trending_coins
from task2_data_processing import process_data
from task3_analysis import analyze_data

fig, ax = plt.subplots(figsize=(10, 6))
while plt.fignum_exists(fig.number):

    coins = get_trending_coins()
    if coins is None:
        print("Waiting for the next API attempt...")
        plt.pause(60)
        continue
    current_time = datetime.now().strftime('%H:%M:%S')
    df = process_data(coins)
    if df is None:
        print("No DataFrame to analyze.")
        plt.pause(60)
        continue

    analysis = analyze_data(df)
    top_gainer = analysis["top_gainer"]
    bottom_loser = analysis["bottom_loser"]

    df = df.sort_values("price_change_24h", ascending=False)

    colors = [
        "green" if value >= 0 else "red"
        for value in df["price_change_24h"]
    ]

    ax.clear()

    ax.barh(
        df["name"],
        df["price_change_24h"],
        color=colors
    )

    ax.axvline(0)

    for i, value in enumerate(df["price_change_24h"]):
        ax.text(
            value,
            i,
            f"{value:.1f}%",
            va="center"
        )

    ax.set_xlabel("24h Price Change (%)")
    ax.set_ylabel("Coin")
    ax.set_title(f"TrendPulse — Live Trending Coin Price Changes\n"
                 f"Top: {top_gainer['name']} +{top_gainer['price_change_24h']:.1f}% | "
                 f"Bottom: {bottom_loser['name']} {bottom_loser['price_change_24h']:.1f}%\n"
                 f"(Last Updated on: {current_time})  | Refreshing every 60 seconds")

    ax.invert_yaxis()
    plt.tight_layout()
    plt.pause(60)