# coding = utf-8
"""
create on : 2018/12/14
project name : NLP_100
file name : problem_no_86 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 85で得た単語の意味ベクトルを読み込み，"United States"のベクトルを表示せよ．
          ただし，"United States"は内部的には"United_States"と
          表現されていることに注意せよ．

"""
import datetime
import sqlite3
import os

import numpy as np
from numpy import load


def load_x_vector_svd_result(norm=False):
    """ load x vector svd result matrix

    :return: x vector matrix numpy matrix
    """

    pwd = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/"

    x_vector_file = load(pwd + "x_vector_svd.npz")

    x_vector = x_vector_file["arr_0"]

    if norm:
        norm_array = np.linalg.norm(x_vector, axis=1)
        norm_x_vector = x_vector / norm_array[:, np.newaxis]

        return norm_x_vector

    return x_vector


def search_t_word_index(search_str):
    """ find t word index number

    :param search_str: to search word string
    :return: t word index int
    """

    pwd = os.path.dirname(os.path.abspath(__file__)).replace("\\", "/") + "/"

    sqlite_path = pwd + "en_wiki_data.sqlite"

    with sqlite3.connect(sqlite_path) as conn:

        cur = conn.cursor()

        sql = "SELECT t_idx FROM t_word_index WHERE t_word = '{word}';"

        cur.execute(sql.format(word=search_str))

        t_word_index_fetch = cur.fetchone()

    if t_word_index_fetch:
        t_word_index = t_word_index_fetch[0]

    else:
        t_word_index = None

    return t_word_index


def word_vec(search_str, x_vector=load_x_vector_svd_result()):
    """ find a word vector from x vector

    :param search_str: to search word string
    :param x_vector: x vector numpy matrix
    :return: word vector numpy array
    """

    t_word_index = search_t_word_index(search_str)

    if t_word_index:
        result_vector = x_vector[t_word_index]

    else:
        result_vector = np.zeros(300)

    return result_vector


def problem_no_86():
    """ find a word vector "United States"

    :return: message string
    """

    start = datetime.datetime.now()
    print("start datetime :", start)

    x_vector = load_x_vector_svd_result()

    x = word_vec("United_States", x_vector=x_vector)
    print(x)

    # print("calculate reduce dimension finish")

    end = datetime.datetime.now()
    print("end datetime :", end)

    elapse = end - start
    print("elapsed time", elapse)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_86())
