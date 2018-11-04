# coding = utf-8
"""
create on : 2018/10/01
project name : NLP_100
file name : problem_no_72

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．
          素性としては，レビューからストップワードを除去し，
          各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""
import re

import nltk
from nltk import wordpunct_tokenize, pos_tag
from nltk.stem.lancaster import LancasterStemmer

from problem_no_70 import pos_neg_check
from problem_no_71 import get_stopwords_list

nltk.download("averaged_perceptron_tagger")

STOPWORDS_LIST = get_stopwords_list()


def sentence_preprocesser(sentence, get_pos_list, min_word_length,
                          stopwords_list=STOPWORDS_LIST):
    """ change sentence to feature list

    :param sentence: sentence string
    :param get_pos_list: get part of speech if None get everything list
    :param min_word_length: minimum word lenth int
    :param stopwords_list: stop words list list
    :return: sentence feature list list
    """

    label = pos_neg_check(sentence)

    # change to lower case
    lower_sentence = sentence[5:].lower()

    # lemmatize and remove stop words
    tokenized_sentence = wordpunct_tokenize(lower_sentence)

    stemmer = LancasterStemmer()

    feature_list = []

    for token, tag in pos_tag(tokenized_sentence):
        stem = stemmer.stem(token)

        # check pos
        if get_pos_list and tag in get_pos_list:
            continue

        # check stopwords
        if stem in stopwords_list:
            continue

        # check word length
        if len(stem) < min_word_length:
            continue

        # change all numeric to 0.0
        feature_list.append(re.sub(r"^(-1)?[0-9]+[.]?[0-9]*?$", "0.0", stem))

    return label, feature_list


def get_feature_from_sentence_list(sentence_list,
                                   get_pos_list=None, min_word_length=3):
    """ get feature list from text file

    :param sentence_list: sentence string list
    :param get_pos_list: get part of speech if None get everything list
    :param min_word_length: minimum word lenth int
    :return: feature list list
    """

    feature_list = [sentence_preprocesser(sentence,
                                          get_pos_list=get_pos_list,
                                          min_word_length=min_word_length)
                    for sentence in sentence_list]

    return feature_list


def problem_no_72():
    """ make feature list from given text file

    :return: message string
    """

    with open("./sentiment.txt", mode="r", encoding="utf-8") as f:
        all_sentences = f.readlines()

    feature_list = get_feature_from_sentence_list(all_sentences)

    for feature in feature_list:
        print(feature)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_72())
