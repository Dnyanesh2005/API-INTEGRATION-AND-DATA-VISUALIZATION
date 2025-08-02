import requests
import matplotlib.pyplot as plt
# Step 1: Fetch data from CoinGecko API
url = "https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd"
response = requests.get(url)
data = response.json()
# Step 2: Extract top 10 coins
coins = [coin['name'] for coin in data[:10]]
prices = [coin['current_price'] for coin in data[:10]]
# Step 3: Visualize
plt.figure(figsize=(10, 6))
plt.bar(coins, prices, color='skyblue')
plt.title("Top 10 Cryptocurrencies by Price (USD)", fontsize=16)
plt.xlabel("Cryptocurrency")
plt.ylabel("Price (USD)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
