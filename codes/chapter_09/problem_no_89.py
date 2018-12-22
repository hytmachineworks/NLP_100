# coding = utf-8
"""
create on : 2018/12/16
project name : NLP_100
file name : problem_no_89 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 85で得た単語の意味ベクトルを読み込み，
          vec("Spain") - vec("Madrid") + vec("Athens")を計算し，
          そのベクトルと類似度の高い10語とその類似度を出力せよ．

"""
import numpy as np

from problem_no_86 import load_x_vector_svd_result
from problem_no_86 import word_vec
from problem_no_88 import calculate_cos_dist_most_common


def vector_most_similar(positive=None, negative=None,
                        topn=10, stdout=True, x_vector=None):
    """ calculate most similar word from positive and negative word

    :param positive: positive words string or list
    :param negative: negative words string or list
    :param topn: top most similar words count int
    :param stdout: standard output or not boolean
    :param x_vector: use already loaded x vector numpy array
    :return: similarity word and cos distance tuple list
    """

    if x_vector is None:
        x_vector = load_x_vector_svd_result(norm=True)

    if not positive and not negative:
        raise KeyError("nothing input...")

    positive_list = positive if type(positive) == list else [positive]
    negative_list = negative if type(negative) == list else [negative]

    # calculate positive
    pos_vector_list = [[word_vec(pos_word, x_vector), pos_word, "pos"]
                       for pos_word in positive_list]

    # calculate negative
    neg_vector_list = [[word_vec(neg_word, x_vector), neg_word, "neg"]
                       for neg_word in negative_list]

    vector_list = pos_vector_list + neg_vector_list

    calc_vec = np.zeros(300)

    word_list = []

    message_string = ""

    for vector, word, polarity in vector_list:

        if polarity == "pos":
            calc_vec += vector
            word_list.append(word)
            message_string += '+ vec("{}") '.format(word)

        elif polarity == "neg":
            calc_vec -= vector
            word_list.append(word)
            message_string += '- vec("{}") '.format(word)

    calc_vec_norm = calc_vec / np.linalg.norm(calc_vec)

    result_list = calculate_cos_dist_most_common(word_list, calc_vec_norm,
                                                 x_vector, topn=topn)

    if stdout:
        print(message_string[2:] + "most relative word(s)\n")

        for word, cos_dist in result_list:
            print(word, cos_dist)

    return result_list


def problem_no_89():
    """ calculate vec("Spain") - vec("Madrid") + vec("Athens")
        most relative words

    :return: message string
    """

    vector_most_similar(positive=["Spain", "Athens"], negative="Madrid")

    return "program finished"


if __name__ == "__main__":
    print(problem_no_89())
