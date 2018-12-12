from requests_oauthlib import OAuth1Session
import json
import os
import datetime
import pytz

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

q = "シクロクロス"
print("https://api.twitter.com/1.1/search/tweets.json", params = q)