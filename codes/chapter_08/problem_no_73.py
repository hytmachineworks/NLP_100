# coding = utf-8
"""
create on : 2018/10/07
project name : NLP_100
file name : problem_no_73 

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 72で抽出した素性を用いて，ロジスティック回帰モデルを学習せよ．

"""
import pickle

from chapter_08_lm import SentimentModel


def problem_no_73():
    """ load document, fit to logistic regression and save model

    :return: message
    """
    # get logistic regression model
    sentiment_model = SentimentModel("./sentiment.txt",
                                     get_pos_list=None,
                                     min_word_length=3)

    # save model to pickle
    with open("./logistic.pickle", mode="bw") as f:
        pickle.dump(sentiment_model, f)

    print("logistic regression and save model finish")

    return "program finished"


if __name__ == "__main__":
    print(problem_no_73())
