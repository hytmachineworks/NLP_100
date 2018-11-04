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


def predict_model(sentence_list, sentiment_model=None, std_io=True):
    """ predict sentence used by model

    :param sentence_list: predict sentence list
    :param sentiment_model: use pickle or model directly SentimentModel Class
    :param std_io: print standard io boolean
    :return: predict list
    """

    if not sentence_list:
        raise ValueError("list is vacant")

    if not sentiment_model:
        with open("./logistic.pickle", mode="br") as f:
            sentiment_model = pickle.load(f)

    model = sentiment_model.model

    # change to sentence to feature and label
    get_pos_list = sentiment_model.get_pos_list
    min_word_length = sentiment_model.min_word_length

    x_test_list = []
    y_tests = []
    pred_list = []
    proba_list = []

    for i, sentence in enumerate(sentence_list):

        label, feature_list = sentence_preprocesser(sentence,
                                                    get_pos_list,
                                                    min_word_length)

        x_test = [1 if word in feature_list else 0
                  for word in sentiment_model.word_list]

        x_test_list.append(x_test)
        y_tests.append(label)

        pred = model.predict(np.array([x_test]))[0]
        pred_list.append(pred)

        proba = model.predict_proba([x_test])[0][1]
        proba_list.append(proba)

        if std_io:
            # check model prediction
            print("\nno. {}".format(str(i)))
            print("sentence : {}".format(sentence))
            print("check prediction")
            print("predict : {}".format(pred))
            print("actual  : {}".format(label))
            # check model score
            print("Predicted probability label is 1 : {}".format(proba))

    x_tests = np.array(x_test_list)

    if std_io:
        # check model score
        print("\nover all predicted probability"
              " : {}".format(model.score(x_tests, y_tests)))

    return [[act, predict, probable]
            for act, predict, probable in zip(y_tests, pred_list, proba_list)]


def problem_no_73():

    pick_up_sentence = 10

    with open("./sentiment.txt", mode="r", encoding="utf-8") as f:
        all_sentences = f.readlines()

    random.shuffle(all_sentences)

    select_sentences = all_sentences[:pick_up_sentence]

    predict_list = predict_model(select_sentences)

    print(predict_list)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_73())
