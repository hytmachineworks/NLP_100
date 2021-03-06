# coding = utf-8
"""
create on : 2018/10/27
project name : NLP_100
file name : problem_no_76 

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 学習データに対してロジスティック回帰モデルを適用し，
          正解のラベル，予測されたラベル，予測確率をタブ区切り形式で出力せよ．
"""
import pandas as pd

from problem_no_74 import predict_model


def predict_result_to_dataframe(predict_result):
    """ predict result to pandas dataframe

    :param predict_result: predict result list
    :return: predict result Dataframe
    """
    df = pd.DataFrame(predict_result,
                      columns=["actual", "predict", "probability"])
    return df


def problem_no_76():
    """ predict from sentiment data, output by tsv format

    :return: message
    """

    with open("./sentiment.txt", mode="r", encoding="utf-8") as f:
        all_sentences = f.readlines()

    predict_list = predict_model(all_sentences, std_io=False)
    df = predict_result_to_dataframe(predict_list)

    df.to_csv("./predict.txt", sep="\t", index=False)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_76())
