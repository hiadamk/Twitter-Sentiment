import Credentials
import re


def get_trends(id):
    trends = Credentials.api.trends_place(id)
    trends = str(trends)
    trends = trends.replace('\'', '"')
    print(trends)


# get_trends(23424975)

def clean_tweet(text):
    t = text
    t = re.sub("rt ", "", t)
    return ' '.join(re.sub (r"(@(\w){1,15})|([^0-9A-Za-z \t])|(\w+:\/\/\S+)| (http\S+) |(#\w*)|(\$\w*)|(\&\w*;)| (http\S+)",
                            " ", t).split())
