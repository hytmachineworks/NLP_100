# coding = utf-8
"""
create on : 2018/11/25
project name : NLP_100
file name : problem_no_83

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 82の出力を利用し，以下の出現分布，および定数を求めよ．

          ・f(t,c): 単語tと文脈語cの共起回数
          ・f(t,∗): 単語tの出現回数
          ・f(∗,c): 文脈語cの出現回数
          ・N: 単語と文脈語のペアの総出現回数

"""
import os
import sqlite3

from tqdm import tqdm


def import_to_sqlite_from_tsv(sqlite_path):
    """ insert all data to sqlite

    :param sqlite_path: sqlite file path string
    :return: message string
    """

    if os.path.exists(sqlite_path):
        return "use exist database"

    print("\ncreate new db and table\n")

    # create database
    with sqlite3.connect(sqlite_path) as conn:
        cur = conn.cursor()

        cur.execute("CREATE TABLE word_pair (t_word text, c_word text)")

        conn.commit()

        print("\ncreate db finished\ninsert_data_start!!!!!!\n")

        with open("./en_wiki_word_pair.txt", mode="r", encoding="utf-8") as f:
            n = 0
            for word_pair in tqdm(f):
                word_pair = word_pair.replace("\n", "")
                word_pair_list = word_pair.split("\t")
                t_word = word_pair_list[0]
                c_word = word_pair_list[1]

                cur.execute("INSERT INTO word_pair VALUES (?,?)",
                            (t_word, c_word))

                n += 1

        conn.commit()

        print("\ninsert_data_finished\n")

        print("\ncalc N\n")
        cur.execute("CREATE TABLE n (n_count integer)")
        cur.execute("INSERT INTO n VALUES (?)", (n,))

        conn.commit()

        print("\nN = {count}\n".format(count=n))

    return "create new database"


def calc_f_t_c(sqlite_path):
    """ calculate f(t, c)

    :param sqlite_path: sqlite file path string
    :return: message string
    """

    print("calculate f(t, c) start")

    with sqlite3.connect(sqlite_path) as conn:
        cur = conn.cursor()

        sql_master = "select name from sqlite_master"

        cur.execute(sql_master)

        table_list = [table[0] for table in cur.fetchall()]

        if "f_t_c" in table_list:
            return "calculate f(t, c) already finished..."

        else:
            sql_create = "CREATE TABLE f_t_c " \
                         "(t_word text, c_word text, count integer);"
            cur.execute(sql_create)

        sql = "select *, count(*) as count from word_pair" \
              " group by t_word, c_word;"
        cur.execute(sql)

        cur_write = conn.cursor()

        for t_word, c_word, count in tqdm(cur):
            cur_write.execute("INSERT INTO f_t_c VALUES (?,?,?);",
                              (t_word, c_word, count))

        conn.commit()

    return "calculate f(t, c) finish"


def calc_f_t_or_f_c(sqlite_path, calc_target):
    """ calculate f(t, *) or f(*, c)

    :param sqlite_path: sqlite file path string
    :param calc_target: calculate target param string
    :return: message string
    """

    message = "t, *" if calc_target == "t" else "*, c"

    table_name = "f_" + calc_target

    write_col = calc_target + "_word"

    print("calculate f(" + message + ") start")

    with sqlite3.connect(sqlite_path) as conn:
        cur = conn.cursor()

        sql_master = "select name from sqlite_master"

        cur.execute(sql_master)

        table_list = cur.fetchall()

        if table_name in table_list:
            return "calculate f(" + message + ") already finished..."

        else:
            sql_create = "CREATE TABLE {table} " \
                         "({col} text," \
                         " count integer);".format(table=table_name,
                                                   col=write_col)
            cur.execute(sql_create)

        sql = "select {col} , count({col}) as count from word_pair" \
              " group by {col};".format(col=write_col)
        cur.execute(sql)

        cur_write = conn.cursor()

        for word, count in tqdm(cur):
            cur_write.execute("INSERT INTO {} VALUES (?,?)".format(table_name),
                              (word, count))

        conn.commit()

    return "calculate f(" + message + ") finish"


def problem_no_83():
    """ calculate word pair parameters

    :return: message string
    """

    sqlite_path = "./en_wiki_data.sqlite"

    # import all collocation data and count N
    print(import_to_sqlite_from_tsv(sqlite_path))

    # calculate f(t, c)
    print(calc_f_t_c(sqlite_path))

    # calculate f(t, *)
    print(calc_f_t_or_f_c(sqlite_path, "t"))

    # calculate f(*, c)
    print(calc_f_t_or_f_c(sqlite_path, "c"))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_83())
