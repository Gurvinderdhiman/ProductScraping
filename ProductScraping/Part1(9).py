import string
import pandas as pd
from bs4 import BeautifulSoup as bs
import requests
import re

response = requests.get("https://www.amazon.in/s?k=Audio+interfaces&crid=EJP3H4PCMJ8M")

amazon_webpage = response.text

soup = bs(amazon_webpage, "html.parser")
#print(soup.title)

startUrl = "https://www.amazon.in"
section_heading = soup.find_all(target="_blank", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")
product_urls = []
for tag in section_heading:
    urls = startUrl + tag.get("href")
    product_urls.append(urls)
print(product_urls)

names = soup.find_all('span',class_='a-size-base-plus a-color-base a-text-normal')
#print(names)
product_name = []
for i in range(0,len(names)):
   product_name.append(names[i].get_text())
print(product_name)

price = soup.find_all("span", class_='a-price-whole')
prices = []
for i in range(0,len(price)):
   prices.append(price[i].get_text())
print(prices)

rating = soup.find_all("i", class_='a-icon a-icon-star-small a-star-small-4-5 aok-align-bottom')
ratings = []
for i in range(0,len(rating)):
   ratings.append(rating[i].get_text())
print(ratings)

review = soup.find_all("span", class_='a-size-base s-underline-text')

reviews = []
for i in range(0,len(review)):
   reviews.append(review[i].get_text())
print(reviews)

df = pd.DataFrame()
df['Product url'] = product_urls
print(df)
df['Product name'] = product_name
print(df)
df['Prices'] = prices
print(df)
df['Ratings'] = ratings
print(df)
df['Reviews'] = reviews
print(df)
df.to_csv(r'D:\Products.xls')








