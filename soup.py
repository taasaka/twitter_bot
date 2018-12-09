import requests
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session
import json
import os
import datetime
import pytz

headers = {'User-Agent':'Mozilla/5.0'}

url = 'https://www.cyclocross.jp/news/'
soup = BeautifulSoup(requests.get(url).content,'html.parser')

now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
now_format = "{0:%Y.%m.%d}".format(now)

h2 = soup.html.h2
d = soup.find("p", class_="date")
d = d.string
a = soup.find("p", class_="click")
a = a.find("a")
a = a.attrs['href']

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])
tweet = h2.string + a
params = {"status": tweet}

if d == now_format:
	req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)