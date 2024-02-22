import requests
import datetime as dt
import os

# Stock API
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = os.environ.get("STOCK_API_KEY") # Ensure to add your API key into the os environment variable
STOCK = "TSLA"

# News API
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = os.environ.get("NEWS_API_KEY") # Ensure to add your API key into the os environment variable
COMPANY_NAME = "Tesla Inc" 

def check_stock_prices_diff():
  stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "outputsize": "compact",
    "apikey": STOCK_API_KEY,
  }

  response = requests.get(STOCK_ENDPOINT, params=stock_parameters)
  response.raise_for_status()
  data = response.json()

  days = [(dt.datetime.now() - dt.timedelta(days=i)).date().strftime("%Y-%m-%d") for i in range(1, 3)]
  prices = [float(data["Time Series (Daily)"][day]["4. close"]) for day in days]
  price_diff = round((prices[0] - prices[1]) / prices[0]  * 100, 2)
  
  return price_diff

def get_news(price):
  news_parameters = {
    "qInTitle": COMPANY_NAME,
    "apikey": NEWS_API_KEY,
  }

  response = requests.get(NEWS_ENDPOINT, params=news_parameters)
  response.raise_for_status()
  data = response.json()

  articles = data["articles"][:3]

  for article in articles:
    title = article["title"]
    desc = article["description"]
    print(f'{STOCK}: {"🔺" if price > 0 else "🔻"} {price}%')
    print(f'Headline: {title}')
    print(f'Brief: {desc}')

# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then get and print news.
price_diff = check_stock_prices_diff()

if price_diff <= -5 or price_diff >= 5:
  get_news(price_diff)