# coding = utf-8
"""
create on : 2018/12/22
project name : NLP_100
file name : problem_no_96 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : word2vecの学習結果から，国名に関するベクトルのみを抜き出せ．

"""
import numpy as np
from numpy import save

from tqdm import tqdm

from problem_no_81 import get_country_list
from problem_no_90 import word_convert_to_vector_model


def problem_no_96():
    """ pick up only country word vector

    :return: message string
    """

    corpus_file_path = "../chapter_09/en_wiki_corpus_mod.txt"
    model_file_path = "./en_wiki.model"
    model = word_convert_to_vector_model(corpus_file_path, model_file_path)

    word2vec_word_list = model.wv.index2entity

    char_list = [")", "(", ",", "."]

    country_list = [country.replace(" ", "_")
                    for country in get_country_list(compund=False)]

    word2vec_country_list = []

    print("search country start ...............\n\n")

    for word in tqdm(word2vec_word_list):

        mod_word = word

        for char in char_list:
            mod_word = mod_word.replace(char, "")

        if mod_word in country_list:
            word2vec_country_list.append(word)

    print("\nsearch country finished ----------\n\n")

    print("create country vector start ........\n\n")

    vector_list = []

    for word2vec_country in tqdm(word2vec_country_list):
        vector = model.wv.get_vector(word2vec_country)
        vector_list.append(vector)

    country_vector_array = np.vstack(tuple(vector_list))

    print("create country vector finished -----\n\n")

    save("./country_vector.npy", country_vector_array)
    with open("./country_label.txt", mode="w", encoding="utf8") as f:
        f.write("\n".join(word2vec_country_list))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_96())
