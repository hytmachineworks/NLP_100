# coding = utf-8
"""
create on : 2018/12/22
project name : NLP_100
file name : problem_no_93 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
and questions-words.txt
This first file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/",
And next file is avalable at
"http://download.tensorflow.org/data/questions-words.txt".
This file NOT include this repository.
If you need file, please get above web sites.

problem : 92で作ったデータを用い，各モデルのアナロジータスクの正解率を求めよ．

"""
import pandas as pd


def calculate_accuracy(filename):
    """ calculate analogy accuracy

    :param filename: analogy output file path string
    :return: accuracy rate float
    """

    df = pd.read_csv(filename, sep=" ", encoding="utf8", header=None)
    df.columns = ["neg_1", "pos_1", "pos2", "answer", "analogy", "cos_dist"]

    df["T_or_F"] = df[["answer", "analogy"]].apply(
        lambda x: True if x[0] == x[1] else False, axis=1)

    s_accuracy = df.groupby("T_or_F").size()

    true_count = s_accuracy[True]
    false_count = s_accuracy[False]

    accuracy = true_count / (true_count + false_count)

    return accuracy


def problem_no_93():
    """ calculate analogy accuracy by x vector and word2vec

    :return:
    """

    filename = "./analogy_family_x_vector.txt"
    print("x_vector accuracy :", calculate_accuracy(filename))

    filename = "./analogy_family_word2vec.txt"
    print("word2vec accuracy :", calculate_accuracy(filename))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_93())
