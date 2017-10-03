# coding = utf-8
"""
create on : 2017/10/03
project name : NLP_100
file name : problem_no_37 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 出現頻度が高い10語とその出現頻度を
          グラフ（例えば棒グラフなど）で表示せよ．

"""
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from problem_no_36 import get_word_count_list


def word_count_list_to_dataframe(start=0, end=0):
    """ word count list convert to dataframe

    :param start: slicing list start point
    :param end:  slicing list end point
    :return: dataframe
    """

    word_count_list = get_word_count_list()

    if end:
        word_count_list_slice = word_count_list[start: end]

    else:
        word_count_list_slice = word_count_list[start:]

    df = pd.DataFrame(word_count_list_slice, columns=["単語", "頻度"])

    return df


def problem_no_37():
    """ draw bar plot of word frequency

    :return: message
    """

    df_word_count = word_count_list_to_dataframe(end=10)

    sns.barplot(x="単語", y="頻度", data=df_word_count, palette="viridis")

    plt.title("「吾輩は猫である」における単語頻度 上位10個")

    plt.tight_layout()

    # plt.show()
    plt.savefig("./problem_no_37.png")

    plt.close()

    return "draw bar plot"


if __name__ == "__main__":
    print(problem_no_37())
