# coding = utf-8
"""
create on : 2018/12/19
project name : NLP_100
file name : problem_no_90

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 81で作成したコーパスに対してword2vecを適用し，単語ベクトルを学習せよ．
          さらに，学習した単語ベクトルの形式を変換し，86-89のプログラムを動かせ．

"""
import os

from gensim.models import word2vec
import logging


def word_convert_to_vector_model(text_file_path, output_file_path):
    """ corpus text convert to gensim model

    :param text_file_path: corpus text file path
    :param output_file_path: output model path string
    :return: learned model gensim model
    """

    if os.path.isfile(output_file_path):
        print("already exist model file")
        return word2vec.Word2Vec.load(output_file_path)

    # for visible information
    logging.basicConfig(format="%(asctime)s : %(levelname)s : %(message)s",
                        level=logging.INFO)

    sentences = word2vec.LineSentence(text_file_path)
    model = word2vec.Word2Vec(sentences, size=300, min_count=10, window=5)

    model.save(output_file_path)

    print("Learning finished, output model file '{}'".format(output_file_path))

    return model


def problem_no_90():
    """ use word2vec solve problem no.86 to 89

    :return: message string
    """

    corpus_file_path = "../chapter_09/en_wiki_corpus_mod.txt"
    model_file_path = "./en_wiki.model"

    model = word_convert_to_vector_model(corpus_file_path, model_file_path)

    print("\n\nproblem no.86 -----------")
    print(model.wv["United_States"])

    print("\n\nproblem no.87 -----------")
    print("cos similarity between United States with U.S")
    print(model.wv.n_similarity(["United_States"], ["U.S"]))

    print("\n\nproblem no.88 -----------")
    results = model.wv.most_similar(positive=["England"], topn=10)
    for result in results:
        print(result)

    print("\n\nproblem no.89 -----------")
    results = model.wv.most_similar(positive=["Spain", "Athens"],
                                    negative=["Madrid"],
                                    topn=10)
    for result in results:
        print(result)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_90())
