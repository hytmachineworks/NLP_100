# coding = utf-8
"""
create on : 2018/12/02
project name : NLP_100
file name : problem_no_84

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 83の出力を利用し，単語文脈行列Xを作成せよ．
          ただし，行列Xの各要素Xtcは次のように定義する．

          ・f(t,c)≥10ならば，Xtc=PPMI(t,c)=max{logN×f(t,c)f(t,∗)×f(∗,c),0}
          ・f(t,c)<10ならば，Xtc=0

          ここで，PPMI(t,c)はPositive Pointwise Mutual Information
          （正の相互情報量）と呼ばれる統計量である．なお，行列Xの行数・列数は
          数百万オーダとなり，行列のすべての要素を主記憶上に載せることは無理なので
          注意すること．幸い，行列Xのほとんどの要素は0になるので，
          非0の要素だけを書き出せばよい．

"""
import math
import sqlite3

import numpy as np
from scipy.sparse import save_npz
from scipy.sparse import coo_matrix

from tqdm import tqdm


def n_value(sqlite_path):
    """ return word pair count N

    :param sqlite_path: sqlite file path string
    :return: count N int
    """

    with sqlite3.connect(sqlite_path) as conn:

        cur = conn.cursor()

        sql = "select * from n;"

        cur.execute(sql)

        result = cur.fetchone()

        n = result[0]

    return n


def ppmi_insert_to_sqlite(sqlite_path, n):
    """ insert ppmi data to sqlite

    :param sqlite_path: sqlite file path string
    :param n: all word pairs count
    :return: message string
    """

    with sqlite3.connect(sqlite_path) as conn:
        cur = conn.cursor()

        sql_master = "select name from sqlite_master"
        cur.execute(sql_master)
        table_list = [table[0] for table in cur.fetchall()]

        if "ppmi" in table_list:
            return "calculate ppmi already finished..."

        else:
            sql_create = "CREATE TABLE ppmi " \
                         "(t_word text, c_word text, ppmi_value real);"
            cur.execute(sql_create)

        sql = "select " \
              "f_t_c.t_word, f_t_c.c_word, f_t_c.count as f_t_c_value, " \
              "f_t.count as f_t_value, f_c.count as f_c_value " \
              "from f_t_c " \
              "inner join f_t on f_t_c.t_word = f_t.t_word " \
              "inner join f_c on f_t_c.c_word = f_c.c_word;"

        cur.execute(sql)

        cur_write = conn.cursor()

        i = 0

        for t_word, c_word, f_t_c, f_t, f_c in tqdm(cur):

            if f_t_c < 10:
                continue

            ppmi = math.log2(((n * f_t_c) / (f_t * f_c)))

            if ppmi > 0:
                i += 1
                cur_write.execute("INSERT INTO ppmi VALUES (?,?,?);",
                                  (t_word, c_word, ppmi))

        conn.commit()

        print("ppmi items :", i)

    return "calculate ppmi finished"


def calc_t_word_c_word_index(sqlite_path):
    """ calculate t_word and c_word index for COO matrix

    :param sqlite_path: sqlite path
    :return: message
    """

    with sqlite3.connect(sqlite_path) as conn:
        cur = conn.cursor()

        sql_master = "select name from sqlite_master"
        cur.execute(sql_master)
        table_list = [table[0] for table in cur.fetchall()]

        print("insert t_word_index start")

        if "t_word_index" in table_list:
            print("t word index already calculated")

        else:
            sql_t_create = "CREATE TABLE t_word_index " \
                           "(t_idx INTEGER, t_word TEXT)"
            cur.execute(sql_t_create)

            sql_t_word = "SELECT DISTINCT t_word FROM ppmi"
            cur.execute(sql_t_word)
            t_word_tuple = cur.fetchall()
            t_word_tuple_list = [(i, t_word[0])
                                 for i, t_word in enumerate(t_word_tuple)]

            sql_t_insert = "INSERT INTO t_word_index " \
                           "(t_idx, t_word) VALUES(?, ?);"

            cur.executemany(sql_t_insert, t_word_tuple_list)

            conn.commit()

            print("insert t_word_index finish")

        print("insert c_word_index start")

        if "c_word_index" in table_list:
            print("c word index already calculated")

        else:
            sql_c_create = "CREATE TABLE c_word_index " \
                           "(c_idx INTEGER, c_word TEXT)"
            cur.execute(sql_c_create)

            sql_c_word = "SELECT DISTINCT c_word FROM ppmi"
            cur.execute(sql_c_word)
            c_word_tuple = cur.fetchall()
            c_word_tuple_list = [(i, c_word[0])
                                 for i, c_word in enumerate(c_word_tuple)]

            sql_c_insert = "INSERT INTO c_word_index" \
                           " (c_idx, c_word) VALUES(?, ?);"

            cur.executemany(sql_c_insert, c_word_tuple_list)

            conn.commit()

            print("insert c_word_index finish")

    return "insert t word and c word index finish"


def create_word_vector_x(sqlite_path):
    """ calculate word vector x as sparse matrix from sqlite data

    :param sqlite_path: sqlite file path
    :return: message string
    """

    print("loading ppmi calc data start...")

    with sqlite3.connect(sqlite_path) as conn:
        cur = conn.cursor()

        sql_row = "SELECT COUNT(*) as row FROM t_word_index"
        cur.execute(sql_row)

        row_count = cur.fetchone()[0]

        sql_col = "SELECT COUNT(*) as col FROM c_word_index"
        cur.execute(sql_col)

        col_count = cur.fetchone()[0]

        sql_x = "SELECT t_word_index.t_idx AS t, " \
                "c_word_index.c_idx AS c, ppmi.ppmi_value AS ppmi_val " \
                "FROM ppmi " \
                "LEFT JOIN t_word_index on " \
                "t_word_index.t_word = ppmi.t_word " \
                "LEFT JOIN c_word_index on " \
                "c_word_index.c_word = ppmi.c_word"

        cur.execute(sql_x)

        print("\nmake COO data\n")

        row_list = []
        col_list = []
        data_list = []

        for t, c, ppmi in tqdm(cur):
            row_list.append(t)
            col_list.append(c)
            data_list.append(ppmi)

    row = np.array(row_list)
    col = np.array(col_list)
    data = np.array(data_list)

    print("\nmake COO finish\n")

    print("make array")

    sparse_matrix = coo_matrix((data, (row, col)),
                               shape=(row_count, col_count))

    save_npz("./x_vector.npz", sparse_matrix)

    return "calculate word_vector_x"


def problem_no_84():
    """ calculate word vector x using with sqlite

    :return: message string
    """

    sqlite_path = "./en_wiki_data.sqlite"

    n = n_value(sqlite_path)

    # calculate ppmi
    print(ppmi_insert_to_sqlite(sqlite_path, n))

    # crate index
    print(calc_t_word_c_word_index(sqlite_path))

    # create word vector X
    print(create_word_vector_x(sqlite_path))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_84())
