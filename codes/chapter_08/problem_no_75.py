# coding = utf-8
"""
create on : 2018/10/27
project name : NLP_100
file name : problem_no_75 

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 73で学習したロジスティック回帰モデルの中で，
          重みの高い素性トップ10と，重みの低い素性トップ10を確認せよ．
"""

import pickle
import numpy as np
import pandas as pd


def problem_no_75():
    """ logistic regression models coef analysis

    :return: message
    """

    with open("./logistic.pickle", mode="br") as f:
        sentiment_model = pickle.load(f)

    model = sentiment_model.model

    # get coef array
    coef_array = np.append([sentiment_model.word_list], model.coef_, axis=0).T

    # to dataframe
    df = pd.DataFrame(coef_array, columns=["feature", "coef"])
    df["coef"] = df["coef"].apply(lambda x: float(x))  # change str to float

    print("\nHigh weight coef top 10")
    print(df.nlargest(10, "coef"))

    print("\nLow weight coef top 10")
    print(df.nsmallest(10, "coef"))

    return "program finished"


if __name__ == '__main__':
    print(problem_no_75())
