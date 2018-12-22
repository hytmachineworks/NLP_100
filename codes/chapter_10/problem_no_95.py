# coding = utf-8
"""
create on : 2018/12/22
project name : NLP_100
file name : problem_no_95 

This problem using enwiki-20150112-400-r10-105752.txt.bz2 and wordsim353.zip
This first file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/",
And next file is avalable at
"http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/".
This file NOT include this repository.
If you need file, please get above web sites.

problem : 94で作ったデータを用い，各モデルが出力する類似度のランキングと，
          人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．

"""

import pandas as pd
from scipy.stats import spearmanr


def calculate_spearmanr(filename):
    """ calculate spearman R

    :param filename: data csv file name string
    :return: r value float, p value float
    """

    df = pd.read_csv(filename, encoding="utf8").dropna()

    r_value, p_value = spearmanr(df[["Human (mean)", "cos_dist"]])

    return r_value, p_value


def problem_no_95():
    """ calculate spearmans R between human and cos distance

    :return: message string
    """

    filename = "./wordsim353_x_vector.csv"
    r_value, p_value = calculate_spearmanr(filename)
    print("spearmanR:", r_value, "p-Value", p_value)

    filename = "./wordsim353_word2vec.csv"
    r_value, p_value = calculate_spearmanr(filename)
    print("spearmanR:", r_value, "p-Value", p_value)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_95())
