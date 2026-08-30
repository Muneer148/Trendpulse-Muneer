import requests


def get_trending_coins():    

    url = "https://api.coingecko.com/api/v3/search/trending"

    try:
        response = requests.get(url)
        response.raise_for_status()
        print(f"HTTP Status: {response.status_code}")
        print("API request successful!")

    except requests.exceptions.RequestException as e:
        print("API request failed:", e)
        return None

    data = response.json()
    print(type(data))     
    print(data.keys())  

    print(type(data['coins']))
    print(len(data['coins']))
    print(data['coins'][0])
    coin = data["coins"][0]["item"]

    print(coin["name"])
    print(coin["symbol"])
    print(coin["market_cap_rank"])
    print(coin["data"]["price"])

    coins = []

    for item in data["coins"]:
        coin = item["item"]
        
        coin_info = {
            "name": coin["name"],
            "symbol": coin["symbol"],
            "market_cap_rank": coin["market_cap_rank"],
            "price": coin["data"]["price"],
            "price_change_24h": coin["data"]["price_change_percentage_24h"]["usd"],
            "market_cap": coin["data"]["market_cap"],
            "total_volume": coin["data"]["total_volume"],
            "score": coin["score"]
        }
        
        coins.append(coin_info)

    print(coins)
    print(len(coins))

    return coins

if __name__ == "__main__":
    coins = get_trending_coins()
    print(coins)