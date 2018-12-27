import csv
import TweetHandler
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split



class LogisticRegressionClassifier:
    training_values = []
    training_outputs = []
    test_values = []
    test_outputs = []

    tweetCorpus = []

    REPLACE_NO_SPACE = re.compile(r"(\.)|(\;)|(\:)|(\!)|(\')|(\?)|(\,)|(\")|(\()|(\))|(\[)|(\])")
    REPLACE_WITH_SPACE = re.compile(r"(<br\s*/><br\s*/>)|(\-)|(\/)")

    def preprocess_data(self, data):
        data = [self.REPLACE_NO_SPACE.sub("", line.lower()) for line in str(data).lower()]
        data = [self.REPLACE_WITH_SPACE.sub(" ", line) for line in data]
        data = [re.sub("^@?(\w){1,15}$", "", line) for line in data]

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
        self.training_values = self.preprocess_data(self.training_values)
        self.training_outputs = [0 if i < 640000 else 1 for i in range(1280000)]

        self.test_values = self.tweetCorpus[640000:800000]
        self.test_values.extend(self.tweetCorpus[1440000:1600000])
        self.test_values = self.preprocess_data(self.test_values)
        self.test_outputs = [0 if i < 160000 else 1 for i in range(320000)]

        # print(len(self.test_values))
        # print(len(self.training_values))
        #
        # print()

        cv = CountVectorizer(binary=True)
        cv.fit(self.training_values)
        X = cv.transform(self.training_values)
        X_test = cv.transform(self.test_values)

        # print(self.test_values)
        # print(self.training_values)
        # print(self.test_outputs)
        # print(self.training_outputs)
        X_train, X_val, y_train, y_val = train_test_split(
            X, self.training_outputs, train_size=0.80
        )
        #
        # for c in [0.01, 0.05, 0.25, 0.5, 1]:
        #     lr = LogisticRegression(C=c)
        #     lr.fit(X_train, y_train)
        #     print("Accuracy for C=%s: %s"
        #           % (c, accuracy_score(y_val, lr.predict(X_val))))

        final_model = LogisticRegression(C=0.5)
        final_model.fit(X, self.training_outputs)
        print("Final Accuracy: %s"
              % accuracy_score(self.test_outputs, final_model.predict(X_test)))



if __name__ == "__main__":
    l = LogisticRegressionClassifier()