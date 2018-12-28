from MyStreamListener import MyStreamListener
import Credentials
import tweepy

Credentials.api.send_direct_message(user_id='1011275787574669312', text='Starting Sentiment Analysis Sir')
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth=Credentials.api.auth, listener=myStreamListener)

print('Stream Started')

# Filters english tweets based on 400 most common twitter words
while True:
    try:

        myStream.filter(languages=["en"], track=["a", "the", "i", "you", "u", "to", "and", "is", "in", "it", "you",
                                                 "of", "for", "on", "my", "that", "at", "with", "me", "do", "have",
                                                 "just", "this", "be", "so", "are", "not", "was", "but", "out"
                                                                                                         "up", "what",
                                                 "now", "new", "from", "your", "like", "good", "no"
                                                                                               "get", "all", "about",
                                                 "we",
                                                 "if", "time", "as", "day", "will",
                                                 "one", "twitter", "how", "can", "some", "an", "am", "by", "going",
                                                 "they", "go", "or", "has", "rt", "know", "today", "there", "love"
                                                                                                            "more",
                                                 "work",
                                                 "too", "got", "he", "back", "think", "did",
                                                 "lol", "when", "see", "really", "had", "great", "off", "would",
                                                 "need", "here", "thanks", "been", "blog", "still", "people",
                                                 "who", "night", "want", "why", "home", "should", "well", "oh",
                                                 "much", "then", "right", "make", "last", "over", "way", "can't",
                                                 "does", "getting", "watching", "its", "only", "her", "post", "his",
                                                 "morning", "very", "she", "them", "could", "first", "than", "better"
                                                                                                             "after",
                                                 "tonight", "our", "again", "down", "news", "man", "looking",
                                                 "us", "tomorrow", "best", "into", "any", "hope", "week", "nice",
                                                 "show", "yes", "where", "take", "check", "come", "trying", "fun",
                                                 "say", "working", "next", "happy", "were", "even", "live", "watch",
                                                 "feel", "thing", "life", "little", "never", "something", "bad",
                                                 "free", "doing", "world", "video", "sure", "yeah", "bed", "let",
                                                 "let", "use", "their", "look", "being", "long", "done", "sleep",
                                                 "before", "year", "find", "awesome", "big", "things", "ok", "another",
                                                 "him", "cool", "old", "ever", "help", "anyone", "made", "ready",
                                                 "days", "die", "other", "read", "because", "two", "playing",
                                                 "though", "house", "always", "also", "listening", "sad", "maybe",
                                                 "please", "wow", "haha", "having", "thank", "pretty", "game",
                                                 "someone",
                                                 "school", "those", "snow", "gonna", "hey", "many", "start", "wait",
                                                 "while", "google", "finally", "everyone", "para", "try", "god",
                                                 "weekend", "most", "iphone", "stuff", "around", "music", "looks",
                                                 "may", "thought", "keep", "yet", "reading", "must", "which", "same",
                                                 "real", "follow", "bit", "hours", "might", "actually", "online", "job",
                                                 "friends", "said", "obama", "coffee", "hate", "hard", "soon", "tweet",
                                                 "making", "wish", "call", "movie", "tell", "thinking", "via", "site",
                                                 "facebook", "few", "found", "these", "tv", "sorry", "through",
                                                 "already", "lot", "makes", "give", "put", "waiting", "stop", "play",
                                                 "says", "away", "coming", "early", "dinner", "phone", "cold", "using",
                                                 "times", "book", "kids", "went", "nothing", "every", "years", "top",
                                                 "office", "friend", "talk", "feeling", "hour", "head", "web", "food",
                                                 "amazing", "car", "lost", "end", "girl", "since", "guess", "lunch",
                                                 "hot", "sounds", "funny", "idea", "glad", "saw", "hear", "mean",
                                                 "name", "damn", "myself", "guy", "song", "yay", "least", "business",
                                                 "run", "place", "friday", "buy", "enough", "anything", "late",
                                                 "photo", "party", "link", "interesting", "used", "shit", "tired",
                                                 "internet", "following", "left", "guys", "momey", "far", "own",
                                                 "seems", "media", "baby", "class", "social", "seen", "miss",
                                                 "forward", "part", "until", "open", "win", "hi", "almost", "dont",
                                                 "windows", "needs", "super", "finished", "crazy", "update", "email",
                                                 "probably", "welcome", "else", "full", "eat", "city", "everything",
                                                 "mind", "believe", "taking", "test", "family", "break", "birthday",
                                                 "started", "minutes", "weather", "later", "set", "room", "such",
                                                 "without", "sunday", "high", "change", "tweets", "omg", "black",
                                                 "meeting", "kind"])
    except:
        continue
