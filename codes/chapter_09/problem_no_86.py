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

from numpy import load


def load_x_vector_svd_result():
    """ load x vector svd result matrix

    :return: x vector matrix numpy matrix
    """

    x_vector_file = load("./x_vector_svd.npz")

    x_vector = x_vector_file["arr_0"]

    return x_vector


def word_vec(search_str, x_vector=load_x_vector_svd_result()):
    """ find a word vector from x vector

    :param search_str: to search word string
    :param x_vector: x vector numpy matrix
    :return: word vector numpy array
    """

    sqlite_path = "./en_wiki_data.sqlite"

    with sqlite3.connect(sqlite_path) as conn:

        cur = conn.cursor()

        sql = "SELECT t_idx FROM t_word_index WHERE t_word = '{word}';"

        cur.execute(sql.format(word=search_str))

        t_word_index = cur.fetchone()[0]

    result_vector = x_vector[t_word_index]

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
