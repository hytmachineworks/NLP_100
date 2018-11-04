# coding = utf-8
"""
create on : 2018/11/04
project name : NLP_100
file name : problem_no_79

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : ロジスティック回帰モデルの分類の閾値を変化させることで，
          適合率-再現率グラフを描画せよ．
"""
import pandas as pd
import matplotlib.pyplot as plt

from problem_no_77 import execute_predict_scores


def calc_precision_recall_curve(df, div=100):
    """ draw accuracy recall curve

    :return: message
    """

    column_list = list(df.columns)

    cut_off_list = [i / div for i in range(div + 1)]

    accuracy_list = []
    recall_list = []

    for cut_off in cut_off_list:

        del df["predict"]

        df["predict"] = df["probability"].apply(lambda x:
                                                1 if x >= cut_off else 0)

        df = df[column_list]

        predict_dict = execute_predict_scores(df)

        accuracy_list.append(predict_dict["Accuracy"])
        recall_list.append(predict_dict["Recall"])

    plt.figure(figsize=(5, 5))

    plt.plot(accuracy_list, recall_list)

    plt.xlabel("Accuracy")
    plt.ylabel("Recall")
    plt.savefig("./Accuracy_Recall.png")
    plt.show()

    return "draw Accuracy Recall curve"


def problem_no_79():
    """ draw accuracy recall curve from predict tab separated data

    :return: message
    """

    df = pd.read_csv("./predict.txt", sep="\t")

    print(calc_precision_recall_curve(df))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_79())
