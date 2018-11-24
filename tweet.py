# coding: utf-8 

from requests_oauthlib import OAuth1Session
import json
import os
import random
import datetime

twitter = OAuth1Session(os.environ["CONSUMER_KEY"],  os.environ["CONSUMER_SECRET"], os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

tweets = ["わん","わんわん","わんわんわん"]

randomtweet = tweets[random.randrange(len(tweets))]

timestamp = datetime.datetime.today() + datetime.timedelta(hours=9)
timestamp = str(timestamp.strftime("%Y/%m/%d %H:%M"))

params = {"status": randomtweet + " " + timestamp}
req = twitter.post("https://api.twitter.com/1.1/statuses/update.json", params = params)