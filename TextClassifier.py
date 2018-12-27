from textblob import TextBlob
from textblob.classifiers import NaiveBayesClassifier
import csv


class TextClassifier:
    tweetCorpus = []
    training = []
    test = []
    cl = None

    def __init__(self):
        print('Text classifier created')
        with open('Utils/training.csv', encoding='utf-8', errors='ignore') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            line_count = 0
            for row in csv_reader:
                try:
                    if row[0] == "0":
                        self.tweetCorpus.append((row[5], 'neg'))
                    elif row[0] == "4":
                        self.tweetCorpus.append((row[5], 'pos'))

                    line_count += 1
                except UnicodeDecodeError:
                    continue

        # There are 1.6 million but only using 5,000 as the naive classifier struggles
        self.training = self.tweetCorpus[:3500]
        self.training.extend(self.tweetCorpus[800000:803500])
        self.test = self.tweetCorpus[3500:5000]
        self.test.extend(self.tweetCorpus[803500:805000])
        print(len(self.training))
        print(len(self.test))
        print('Starting Training')
        self.cl = NaiveBayesClassifier(self.training)
        print(self.cl.accuracy(self.test))

    def classify(self, text):
        return self.cl.classify(text)
