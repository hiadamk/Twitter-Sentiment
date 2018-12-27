import tweepy
import re
import json
import Credentials
import TweetHandler
from TextClassifier import TextClassifier


class MyStreamListener(tweepy.StreamListener):

    pos_tweets = 0
    neg_tweet = 0
    text_classifier = TextClassifier()

    # When there is a new tweet detected in the stream it will perform the following actions (generate a new tweet)
    def on_status(self, status):

        j = json.loads(json.dumps(status._json))
        # tweeter = "@" + j["user"]["screen_name"]
        # print("JSON: " + j["user"])
        text = status.text
        print("TEXT: " + text)

        text = TweetHandler.clean_tweet(text)
        res = self.text_classifier.classify(text)

        print(res + " " +text)

