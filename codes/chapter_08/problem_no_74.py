# coding = utf-8
"""
create on : 2018/10/13
project name : NLP_100
file name : problem_no_74 

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 73で学習したロジスティック回帰モデルを用い，
          与えられた文の極性ラベル（正例なら"+1"，負例なら"-1"）と，
          その予測確率を計算するプログラムを実装せよ．
"""

import pickle
import random

import numpy as np

from problem_no_72 import sentence_preprocesser


def predict_model(sentence_list):

    if not sentence_list:
        raise ValueError("list is vacant")

    with open("./logistic.pickle", mode="br") as f:
        sentiment_model = pickle.load(f)

    model = sentiment_model.model

    # change to sentence to feature and label
    get_pos_list = sentiment_model.get_pos_list
    min_word_length = sentiment_model.min_word_length

    x_test_list = []
    y_tests = []

    for i, sentence in enumerate(sentence_list):

        label, feature_list = sentence_preprocesser(sentence,
                                                    get_pos_list,
                                                    min_word_length)

        x_test = [1 if word in feature_list else 0
                  for word in sentiment_model.word_list]

        x_test_list.append(x_test)

        y_tests.append(label)

        # check model prediction
        print("no. {}".format(str(i)))
        print("\nsentence : {}".format(sentence))
        print("check prediction")
        print("predict : {}".format(model.predict(np.array([x_test]))[0]))
        print("actual  : {}".format(label))

    x_tests = np.array(x_test_list)

    # check model score
    print("\nPredicted probability : {}".format(model.score(x_tests, y_tests)))


def problem_no_73():

    pick_up_sentence = 10

    with open("./sentiment.txt", mode="r", encoding="utf-8") as f:
        all_sentences = f.readlines()

    random.shuffle(all_sentences)

    select_sentences = all_sentences[:pick_up_sentence]

    predict_model(select_sentences)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_73())
