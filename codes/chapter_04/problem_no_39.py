# coding = utf-8
"""
create on : 2017/10/03
project name : NLP_100
file name : problem_no_39 


This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 単語の出現頻度順位を横軸，その出現頻度を縦軸として，
          両対数グラフをプロットせよ．

"""
import matplotlib.pyplot as plt

from problem_no_37 import word_count_list_to_dataframe


def problem_no_39():
    """ draw scatter plot of frequency and rank of words

    :return: message
    """

    df_word_count = word_count_list_to_dataframe().reset_index(drop=False)

    df_word_count["Rank"] = df_word_count["index"].apply(lambda x: x + 1)
    del df_word_count["index"]

    plt.scatter(x=df_word_count["Rank"],
                y=df_word_count["頻度"])

    plt.title("「吾輩は猫である」における単語の発現頻度 x 順位")

    plt.xscale("log")
    plt.xlabel("単語の発現頻度の順位")

    plt.yscale("log")
    plt.ylabel("単語の発現頻度")

    plt.tight_layout()

    # plt.show()
    plt.savefig("./problem_no_39.png")

    plt.close()

    return "draw scatter plot"


if __name__ == "__main__":
    print(problem_no_39())
