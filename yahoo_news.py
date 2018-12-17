import requests
from bs4 import BeautifulSoup
from requests_oauthlib import OAuth1Session
import json
import os
import datetime
import pytz

headers = {'User-Agent':'Mozilla/5.0'}

url = 'https://news.yahoo.co.jp/search/;_ylt=A2RivbFkExFcgRkARCcPk.d7?p=%E3%82%B7%E3%82%AF%E3%83%AD%E3%82%AF%E3%83%AD%E3%82%B9+-%E7%A6%8F%E5%85%89&aq=-1&oq=&ei=UTF-8'
soup = BeautifulSoup(requests.get(url).content,'html.parser')

now = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
now_format = "{0:%m月%d日}".format(now)

h2 = soup.html.h2
d = soup.find("h2", class_="t")
d = d.string
a = soup.find("h2", class_="t")
a = a.find("a")
a = a.attrs['href']
day = soup.find("span", class_="d")
day = day.string
slice6 = day[:6]
slice5 = day[:5]
slice4 = day[:4]

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])
tweet = h2.string + str(a)
params = {"status": tweet}

if slice6 == now_format or slice5 == now_format or slice4 == now_format:
	req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)
#print(now_format)
#print(slice)
#print(tweet)
#print(params)