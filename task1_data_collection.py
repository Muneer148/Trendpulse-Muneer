import requests

url = "https://api.coingecko.com/api/v3/search/trending"

response = requests.get(url)

print(response.status_code)
print(response.text[:500])

data = response.json()
print(type(data))                    
