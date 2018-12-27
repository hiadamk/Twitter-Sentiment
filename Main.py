from TextClassifier import TextClassifier
import time
import datetime
from MyStreamListener import MyStreamListener
import Credentials
import tweepy

# start = time.time()
# t = TextClassifier()
#
# end = time.time()
# print(str(datetime.timedelta(seconds=(end-start))))

myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=Credentials.api.auth, listener=myStreamListener)

while True:
    try:
        myStream.filter(languages=["en"], track=["a", "the", "i", "you", "u", "to", "and", "is", "in","it", "you",
                                                 "of", "for", "on", "my", "that", "at","with", "me", "do", "have",
                                                 "just", "this", "be", "so", "are", "not", "was", "but", "out"
                                                 "up", "what", "now", "new", "from", "your", "like", "good", "no"
                                                 "get", "all", "about", "we", "if", "time", "as", "day", "will",
                                                 "one", "twitter", "how", "can", "some", "an", "am", "by", "going",
                                                 "they", "go", "or", "has", "rt", "know", "today", "there", "love"
                                                 "more", "work", "too", "got", "he", "back", "think", "did",
                                                 "lol", "when", "see", "really", "had", "great", "off", "would",
                                                 "need", "here", "thanks", "been", "blog", "still", "people",
                                                 "who", "night", "want", "why", "home", "should", "well", "oh",
                                                 "much", "then", "right", "make", "last", "over", "way", "can't",
                                                 "does", "getting", "watching", "its", "only", "her", "post", "his",
                                                 "morning", "very", "she", "them", "could", "first", "than", "better"
                                                 "after", "tonight", "our", "again", "down", "news", "man", "looking",
                                                 "us", "tomorrow", "best", "into", "any", "hope", "week", "nice",
                                                 "show", "yes", "where", "take", "check", "come", "trying", "fun",
                                                 "say", "working", "next", "happy", "were", "even", "live", "watch",
                                                 "feel", "thing", "life", "little", "never", "something", "bad",
                                                 "free", "doing", "world", "video", "sure", "yeah", "bed", "let",
                                                 "let", "use", "their", "look", "being", "long", "done", "sleep",
                                                 "before", "year", "find", "awesome", "big", "things", "ok", "another",
                                                 "him", "cool", "old", "ever", "help", "anyone", "made", "ready",
                                                 "days", "die", "other", "read", "because", "two", "playing",
                                                 "though", "house", "always", "also", "listening"])
    except Exception:
        print("Tried to break but still here")
        continue