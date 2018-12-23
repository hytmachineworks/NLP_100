# coding = utf-8
"""
create on : 2018/12/23
project name : NLP_100
file name : problem_no_99 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 96の単語ベクトルに対して，ベクトル空間をt-SNEで可視化せよ．

"""
from matplotlib import pyplot as plt
from sklearn.manifold import TSNE
from numpy import load

from problem_no_97 import get_country_cluster


def problem_no_99():
    """ Vector space visualization by t-SNE

    :return: message string
    """
    country_vector = load("./country_vector.npy")

    x_tsne = TSNE(n_components=2).fit_transform(country_vector)

    country_cluster = get_country_cluster()

    color_dict = {0: "b", 1: "g", 2: "r", 3: "y", 4: "m"}

    color_list = [color_dict[cluster] for cluster in country_cluster]

    plt.figure(figsize=(10, 10))
    plt.title("Country word vector / t-SNE")
    plt.xlabel("component 1")
    plt.ylabel("conponent 2")
    plt.scatter(x_tsne[:, 0], x_tsne[:, 1], c=color_list)
    plt.tight_layout()

    plt.savefig("country_tsne.png", format="png", dpi=300)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_99())
