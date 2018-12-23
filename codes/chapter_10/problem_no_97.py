# coding = utf-8
"""
create on : 2018/12/23
project name : NLP_100
file name : problem_no_97 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 96の単語ベクトルに対して，k-meansクラスタリングをクラスタ数k=5として実行せよ．

"""
from pprint import pprint

from sklearn.cluster import KMeans
from numpy import load


def load_country_list():
    """ load country label list

    :return: country label list
    """

    with open("./country_label.txt", mode="r", encoding="utf8") as f:
        country_list = [country.rstrip() for country in f]

    return country_list


def problem_no_97():
    """ clustering 5 cluster by k-means method

    :return: message string
    """

    country_vector = load("./country_vector.npy")

    kmeans = KMeans(n_clusters=5, random_state=0).fit(country_vector)
    country_cluster = list(kmeans.labels_)

    # divide by country cluster
    country_list = load_country_list()

    cluster_list = [[], [], [], [], []]

    for country, cluster in zip(country_list, country_cluster):

        cluster_list[int(cluster)].append(country)

    for i in range(5):

        print("\n\ncluster no.{}".format(str(i)))

        pprint(cluster_list[i])

    return "program finished"


if __name__ == "__main__":
    print(problem_no_97())
