# coding = utf-8
"""
create on : 2018/12/16
project name : NLP_100
file name : problem_no_87 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 85で得た単語の意味ベクトルを読み込み，"United States"と"U.S."の
          コサイン類似度を計算せよ．
          ただし，"U.S."は内部的に"U.S"と表現されていることに注意せよ．

"""
import numpy as np

from problem_no_86 import load_x_vector_svd_result
from problem_no_86 import word_vec


def two_words_similarity(word_a, word_b, x_vector=None):
    """ calculate two words cos distance

    :param word_a: word wants to calc similarity string
    :param word_b: word wants to calc similarity string
    :param x_vector: x_vector numpy array
    :return: cosin distance float
    """

    if x_vector is None:
        x_vector = load_x_vector_svd_result(norm=True)

    vec_united_states = word_vec(word_a, x_vector)
    vec_u_s = word_vec(word_b, x_vector)

    cos_dist = np.dot(vec_united_states, vec_u_s)

    return cos_dist


def problem_no_87():
    """ calculate cos distance between 'Unites States' and 'U.S'

    :return: message string
    """

    print("cos distance :", two_words_similarity("United_States", "U.S"))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_87())
