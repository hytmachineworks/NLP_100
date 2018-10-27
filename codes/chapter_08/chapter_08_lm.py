# coding = utf-8
"""
create on : 2018/10/27
project name : NLP_100
file name : chapter_08_lm 

get logistic legression model from sentence
"""

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression

from problem_no_72 import get_feature_from_document


class SentimentModel:
    """ Logistic Regression from sentence text
    """

    def __init__(self, filename, get_pos_list, min_word_length):
        """ initialize class

        :param filename: file name string
        :param get_pos_list: get part of speech if None get everything list
        :param min_word_length: minimum word lenth int
        """

        feature_list = get_feature_from_document(filename,
                                                 get_pos_list,
                                                 min_word_length)

        sentiment_review_array = [[sentiment, " ".join(review)]
                                  for sentiment, review in feature_list]

        df = pd.DataFrame(sentiment_review_array,
                          columns=["sentiment", "review"])

        y_train = df.loc[:, "sentiment"].values

        reviews = df.loc[:, "review"].values

        vectorized = CountVectorizer()
        x_data = vectorized.fit_transform(reviews)
        x_trains = x_data.toarray()

        # logistic regression
        logit_reg = LogisticRegression(solver="lbfgs")
        logit_reg.fit(x_trains, y_train)

        self.model = logit_reg
        self.x_trains = x_trains
        self.y_trains = y_train
        self.word_list = vectorized.get_feature_names()

        self.get_pos_list = get_pos_list
        self.min_word_length = min_word_length
