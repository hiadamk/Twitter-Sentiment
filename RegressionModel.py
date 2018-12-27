import csv
import TweetHandler
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

class RegressionModel:
    training_values = []
    training_outputs = []
    test_values = []
    test_outputs = []
    tweetCorpus = []

    REPLACE_NO_SPACE = re.compile(r"(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")

    classifier = None
    cv = None
    stop_words = set(stopwords.words('english'))

    def preprocess_data(self, data):
        data = [re.sub(r"(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])|@(\w){1,15}|(<br\s*/><br\s*/>)|(\-)|(\/)"
                       , "",line.lower()) for line in data]

        return data

    def __init__(self):
        print('Text classifier created')
        with open('Utils/training.csv', encoding='utf-8', errors='ignore') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                try:
                    self.tweetCorpus.append(row[5])

                except UnicodeDecodeError:
                    continue

        self.training_values = self.tweetCorpus[:640000]
        self.training_values.extend(self.tweetCorpus[800000:1440000])

        self.test_values = self.tweetCorpus[640000:800000]
        self.test_values.extend(self.tweetCorpus[1440000:1600000])

        print(len(self.test_values))
        print(len(self.training_values))

        print("Processing starting")
        self.training_values = self.preprocess_data(self.training_values)
        print("Processing training data done")
        self.test_values = self.preprocess_data(self.test_values)
        print("Processing test values done")

        self.training_outputs = [0 if i < 640000 else 1 for i in range(1280000)]
        self.test_outputs = [0 if i < 160000 else 1 for i in range(320000)]

        self.cv = CountVectorizer(binary=True)
        self.cv.fit(self.training_values)
        X = self.cv.transform(self.training_values)
        X_test = self.cv.transform(self.test_values)

        X_train, X_val, y_train, y_val = train_test_split(
            X, self.training_outputs, train_size=0.80
        )

        final_model = LogisticRegression(C=0.5)
        final_model.fit(X, self.training_outputs)
        self.classifier = final_model
        print("Final Accuracy: %s"
              % accuracy_score(self.test_outputs, final_model.predict(X_test)))

    def classify_text(self, text):
        t = TweetHandler.clean_tweet(text)
        t = self.preprocess_data([t])
        text_matrix = self.cv.transform(t)
        result = self.classifier.predict(text_matrix)

        return result[0].item()


if __name__ == "__main__":
    l = RegressionModel()
    l.classify_text("I love you so much, you make me happy")
    l.classify_text("Jeremy corbyn is a crappy politician")
