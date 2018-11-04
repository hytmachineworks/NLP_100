# coding = utf-8
"""
create on : 2018/10/28
project name : NLP_100
file name : problem_no_78 

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 76-77の実験では，学習に用いた事例を評価にも用いたため，正当な評価とは言えない．
          すなわち，分類器が訓練事例を丸暗記する際の性能を評価しており，
          モデルの汎化性能を測定していない．そこで，5分割交差検定により，
          極性分類の正解率，適合率，再現率，F1スコアを求めよ．
"""
import random

from chapter_08_lm import SentimentModel
from problem_no_74 import predict_model
from problem_no_76 import predict_result_to_dataframe
from problem_no_77 import execute_predict_scores


def cross_validation(sentences_list, div=5):
    """ k-fold cross validation

    :param sentences_list: all sentence list
    :param div: divide k components
    :return: (total result dict, individual result list) tuple
    """

    def get_test_data(given_divide_list, train_no):
        provide_train_data = []

        for index_no in range(div):
            if index_no != train_no:
                provide_train_data.extend(given_divide_list[index_no])

        return provide_train_data

    random.seed(0)

    random.shuffle(sentences_list)

    divide_list = [[] for _ in range(div)]

    for i, sentence in enumerate(sentences_list):
        divide_list[i % div].append(sentence)

    predict_result = []

    acurracy = 0
    precision = 0
    recall = 0
    f_score = 0

    for number in range(div):
        train_data = divide_list[number]
        test_data = get_test_data(divide_list, number)

        # get logistic regression model
        sentiment_model = SentimentModel(train_data,
                                         get_pos_list=None,
                                         min_word_length=3)

        predict_list = predict_model(test_data, sentiment_model, std_io=False)

        df = predict_result_to_dataframe(predict_list)

        predict_dict = execute_predict_scores(df)

        acurracy += predict_dict["Accuracy"]
        precision += predict_dict["Precision"]
        recall += predict_dict["Recall"]
        f_score += predict_dict["F score"]

        predict_result.append(predict_dict)

    total_result_dict = {"Accuracy": acurracy / div,
                         "Precision": precision / div,
                         "Recall": recall / div,
                         "F score": f_score / div}

    return total_result_dict, predict_result


def problem_no_78():
    """ 5-fold cross validation of logistic regression model

    :return: message
    """

    with open("./sentiment.txt", mode="r", encoding="utf-8") as f:
        sentences_list = f.readlines()

    total_result_dict, predict_result = cross_validation(sentences_list)

    for i, result in enumerate(predict_result):
        print("try no.{}".format(str(i)))
        print("Accuracy ", result["Accuracy"])
        print("Precision", result["Precision"])
        print("Recall   ", result["Recall"])
        print("F score  ", result["F score"])
        print("")

    print("average result")
    print("Accuracy ", total_result_dict["Accuracy"])
    print("Precision", total_result_dict["Precision"])
    print("Recall   ", total_result_dict["Recall"])
    print("F score  ", total_result_dict["F score"])

    return "program finished"


if __name__ == "__main__":
    print(problem_no_78())
