# coding = utf-8
"""
create on : 2018/12/16
project name : NLP_100
file name : problem_no_88 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 85で得た単語の意味ベクトルを読み込み，
          "England"とコサイン類似度が高い10語と，その類似度を出力せよ

"""
import sqlite3

import numpy as np

from problem_no_86 import load_x_vector_svd_result
from problem_no_86 import word_vec


def get_t_word(t_word_index, sqlite_path):
    """ get t word index from sqlite database

    :param t_word_index: search word index integer
    :param sqlite_path: sqlite file path string
    :return: t word string
    """

    with sqlite3.connect(sqlite_path) as conn:
        cur = conn.cursor()

        sql = "SELECT t_word FROM t_word_index WHERE t_idx = {idx};"

        cur.execute(sql.format(idx=t_word_index))

        t_word = cur.fetchone()[0]

    return t_word


def calculate_cos_dist_most_common(search_word_list, given_vector, x_vector):
    """ calculate and find most common 10 words

    :param search_word_list: search word list
    :param given_vector: given word normalized vector
    :param x_vector: normalized word vector x
    :return: most common word and cos distance list
    """

    sqlite_path = "./en_wiki_data.sqlite"

    cos_dist_array = np.dot(x_vector, given_vector)

    sort_indexs = np.argsort(cos_dist_array)[::-1]

    most_common_list = []

    for t_idx in sort_indexs[:10 + len(search_word_list)]:
        t_word = get_t_word(t_idx, sqlite_path)
        cos_dist = cos_dist_array[t_idx]

        if t_word not in search_word_list:
            most_common_list.append((t_word, cos_dist))

    return most_common_list[:10]


def problem_no_88():
    """ search most relative word with England

    :return: message string
    """

    target_word = "England"

    x_vector = load_x_vector_svd_result(norm=True)
    vec_england = word_vec(target_word, x_vector)

    result_list = calculate_cos_dist_most_common([target_word],
                                                 vec_england, x_vector)

    print(target_word, "most relative words\n")
    for word, cos_dist in result_list:
        print(word, cos_dist)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_88())
