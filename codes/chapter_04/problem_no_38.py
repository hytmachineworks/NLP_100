# coding = utf-8
"""
create on : 2017/10/03
project name : NLP_100
file name : problem_no_38 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 単語の出現頻度のヒストグラム
          （横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を
          棒グラフで表したもの）を描け．

"""
import seaborn as sns
import matplotlib.pyplot as plt

from problem_no_37 import word_count_list_to_dataframe


def problem_no_38():
    """ draw histogram of frequency words

    :return: message
    """

    df_word_count = word_count_list_to_dataframe()

    sns.distplot(df_word_count["頻度"], kde=False)

    plt.title("「吾輩は猫である」における単語の発現頻度")

    plt.yscale("log")
    plt.ylabel("単語の個数")

    plt.tight_layout()

    # plt.show()
    plt.savefig("./problem_no_38.png")

    plt.close()

    return "draw histogram"


if __name__ == "__main__":
    print(problem_no_38())

