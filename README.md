# Twitter Sentiment

The aim of this project is to find out daily what the overall sentiment of tweets that day is.

### First Steps
I started by first working on the sentiment analysis. I found a dataset of 1.6 million labelled tweets which show whether they are positive or negative. I took the first 500,000 positive tweets and 500,000 negative tweets to reduce the file size. I also removed unnecessary columns to further bring the file size down to something which can be uploaded to serves more easily later.

### Regression
My initial approach in sentiment analysis used a naive Bayes classifier however the accuracy was only 70% and so I changed my approach to logistic regression to try and achieve better results. I split the training and test data in a 70:30 split respectively. I have little experience using machine learning techniques practically and so I decided to start with a simple one: linear regression. I found that better results of accuracy were achieved of ~80% and so I decided that as tweets are quite an unpredictable text-form, this is good enough for now.

### Streaming
The Twitter API makes it very easy to constantly observe tweets based on different parameters such as usernames, locations, keywords etc. I used 400 of the [500 most frequently used words on Twitter](http://techland.time.com/2009/06/08/the-500-most-frequently-used-words-on-twitter/) to track as many common tweets as possible to form an unbiased set of data to evaluate sentiment from. These tweets require pre-processing such as removing links, usernames and punctuation however I found that removing stop-words slightly reduced the accuracy, so I kept the words as they were. Each cleaned tweet is then passed to the trained model which predicts the sentiment of the tweet and stores the result. The program runs for a number of hours and tweets the percentage of tweets it deemed as positive and what the 4 most common words were (after cleaning out some stop words).

Overall not a difficult project, but an interesting one with loads of small intricate things I had to learn through trial and error.

**Total coding time:** 16 hrs 5 mins (Training 1.6 million tweets over and over makes the world go in slow motion)