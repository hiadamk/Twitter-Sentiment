import re


# Cleans tweets
def clean_tweet(text):
    t = text
    t = re.sub("rt ", "", t)
    return ' '.join(
        re.sub(r"(@(\w){1,15})|([^0-9A-Za-z \t])|(\w+:\/\/\S+)| (http\S+) |(#\w*)|(\$\w*)|(\&\w*;)| (http\S+)",
               " ", t).split())
