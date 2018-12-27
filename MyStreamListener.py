import tweepy
import re
import json
import collections
from examples.streaming import StdOutListener

import Credentials
import TweetHandler
from RegressionModel import RegressionModel
import time
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class MyStreamListener(tweepy.StreamListener):
    pos_tweets = 0
    neg_tweet = 0
    total = 0
    regression_model = RegressionModel()
    start_time = None
    duration =20
    words = []
    stop_words = None

    def __init__(self, api=None):
        super(MyStreamListener, self).__init__()
        self.start_time = time.time()
        self.stop_words = set(stopwords.words('english'))
        self.stop_words.add('amp')
        self.stop_words.add('rt')

    # When there is a new tweet detected in the stream it will perform the following actions (generate a new tweet)
    def on_status(self, status):

        if time.time() > self.start_time + self.duration:
            print("DONE STREAMING")

            cnt = collections.Counter(self.words)

            five = cnt.most_common(5)
            formatted = ['%s (%d occurrences)' % (t[0], t[1]) for t in five]
            pos = (self.pos_tweets / self.total) * 100
            tweet = "Today, I sampled " + str(self.total) + " tweets and " + str(round(pos)) + "% of them were positive. The ten most common words were " + str(formatted)
            Credentials.api.update_status(tweet)
            print(tweet)
            return False
        else:

            j = json.loads(json.dumps(status._json))
            # tweeter = "@" + j["user"]["screen_name"]
            # print("JSON: " + j["user"])
            text = status.text

            # print("TEXT: " + text)

            text = TweetHandler.clean_tweet(text.lower())
            # self.words.extend(word_tokenize(text))
            word_tokens = word_tokenize(text)
            filtered_sentence = [w for w in word_tokens if not w in self.stop_words]
            self.words.extend(filtered_sentence)

            res = self.regression_model.classify_text(text)
            if res == 1:
                self.pos_tweets +=1
                sent = 'Positive'
            else:
                self.neg_tweet +=1
                sent = 'Negative'
            self.total += 1
            # if self.total % 10000 == 0:
            #     print('POSITIVE TWEETS: ', self.pos_tweets)
            #     print('NEGATIVE TWEETS: ', self.neg_tweet)
            #     print('%positive: ', self.pos_tweets/self.total)
            print(sent + " " + text)
            return True

