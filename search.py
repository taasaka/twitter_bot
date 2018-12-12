from requests_oauthlib import OAuth1Session
import json
import os
import datetime
import pytz

twitter = OAuth1Session( _
	os.environ["CONSUMER_KEY"],  _
	os.environ["CONSUMER_SECRET"],  _
	os.environ["ACCESS_TOKEN_KEY"],  _
	os.environ["ACCESS_TOKEN_SECRET"])

q = "シクロクロス"
print("https://api.twitter.com/1.1/search/tweets.json", params = q)