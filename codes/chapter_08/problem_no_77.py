# coding = utf-8
"""
create on : 2018/10/28
project name : NLP_100
file name : problem_no_77

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 76の出力を受け取り，予測の正解率，正例に関する適合率，再現率，
          F1スコアを求めるプログラムを作成せよ．
"""
import pandas as pd


def execute_predict_scores(df):
    """ calculate model performance data

    :param df: logistic regresson result dataframe
    :return: dict
    """

    # True Positive count
    t_p = df[(df["predict"] == 1) & (df["actual"] == 1)].shape[0]

    # True Negative count
    t_n = df[(df["predict"] == 0) & (df["actual"] == 0)].shape[0]

    # False Positive count
    f_p = df[(df["predict"] == 1) & (df["actual"] == 0)].shape[0]

    # False Negative count
    f_n = df[(df["predict"] == 0) & (df["actual"] == 1)].shape[0]

    acurracy = (t_p + t_n) / (t_p + t_n + f_p + f_n)

    precision = t_p / (t_p + f_p)

    recall = t_p / (t_p + f_n)

    f_score = (2 * recall * precision) / (recall + precision)

    result_dict = {"Accuracy": acurracy,
                   "Precision": precision,
                   "Recall": recall,
                   "F score": f_score}

    return result_dict


def problem_no_76():
    """ calculate model performance data from tsv data

    :return: message string
    """

    df = pd.read_csv("./predict.txt", sep="\t")

    print(execute_predict_scores(df))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_76())
