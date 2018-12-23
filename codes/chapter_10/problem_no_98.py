# coding = utf-8
"""
create on : 2018/12/23
project name : NLP_100
file name : problem_no_98 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 96の単語ベクトルに対して，Ward法による階層型クラスタリングを実行せよ．
          さらに，クラスタリング結果をデンドログラムとして可視化せよ．

"""
from matplotlib import pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from numpy import load

from problem_no_97 import load_country_list


def problem_no_98():
    """ clustering by ward method and show its dendrogram

    :return:
    """

    country_vector = load("./country_vector.npy")

    z = linkage(country_vector, "ward")

    # calculate full dendrogram
    plt.figure(figsize=(100, 20))
    plt.title("Country word vector / clustering dendrogram")
    plt.xlabel("country name")
    plt.ylabel("distance")
    dendrogram(z, leaf_rotation=90., leaf_font_size=24,
               labels=load_country_list())
    plt.tight_layout()

    plt.savefig("country_dendrogram.png", format="png", dpi=300)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_98())
