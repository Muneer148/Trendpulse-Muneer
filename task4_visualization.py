import time
import matplotlib.pyplot as plt

from task1_data_collection import get_trending_coins
from task2_data_processing import process_data

fig, ax = plt.subplots(figsize=(10, 6))
while plt.fignum_exists(fig.number):

    coins = get_trending_coins()
    if coins is None:
        print("Waiting for the next API attempt...")
        plt.pause(60)
        continue
    df = process_data(coins)
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
    ax.set_title("TrendPulse — Live Trending Coin Price Changes")

    ax.invert_yaxis()
    plt.tight_layout()
    plt.pause(60)