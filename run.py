#!/usr/bin/env python
# -*- coding:utf-8 -*-

from datetime import datetime
from twitter import APIKey, ITwitter

if __name__ == "__main__":
    key = APIKey(
        consumer_key = "",
        consumer_secret = "",
        bearer_token = r"",
        access_token = "",
        access_token_secret = ""
    )
    now = datetime.now()
    my_tweets_file = "twitter/{}-{}-{}-my-tweets.md".format(now.year, now.month, now.day)
    twitter = ITwitter(key,"http://127.0.0.1:7890")
    twitter.get_tweets(my_tweets_file)
    twitter.empty_tweets()

