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


def problem_no_89():
    """ calculate vec("Spain") - vec("Madrid") + vec("Athens")
        most relative words

    :return: message string
    """

    x_vector = load_x_vector_svd_result(norm=True)
    vec_spain = word_vec("Spain", x_vector)
    vec_madrid = word_vec("Madrid", x_vector)
    vec_athens = word_vec("Athens", x_vector)

    calc_vec = vec_spain - vec_madrid + vec_athens
    calc_vec_norm = calc_vec / np.linalg.norm(calc_vec)

    word_list = ["Spain", "Madrid", "Athens"]

    result_list = calculate_cos_dist_most_common(word_list,
                                                 calc_vec_norm, x_vector)

    print('vec("Spain") - vec("Madrid") + vec("Athens") most relative words\n')

    for word, cos_dist in result_list:
        print(word, cos_dist)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_89())
