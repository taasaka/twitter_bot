import requests
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session
import json
import os
import datetime

headers = {'User-Agent':'Mozilla/5.0'}

url = 'https://www.cyclocross.jp/news/'
soup = BeautifulSoup(requests.get(url).content,'html.parser')

h2 = soup.html.h2
print(h2.string)
a = soup.find("p", class_="click")
a = a.find("a")
a = a.attrs['href']
print(a)

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

tweet = h2.string + a
params = {"status": tweet}

# Get your "home" timeline
# response = t.statuses.home_timeline()
# print(response)


req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)

