def get_trending_coins():    
    import requests

    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)

    print(response.status_code)
    print(response.text[:500])

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