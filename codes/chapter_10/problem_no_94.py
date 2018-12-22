# coding = utf-8
"""
create on : 2018/12/22
project name : NLP_100
file name : problem_no_94 

This problem using enwiki-20150112-400-r10-105752.txt.bz2 and wordsim353.zip
This first file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/",
And next file is avalable at
"http://www.cs.technion.ac.il/~gabr/resources/data/wordsim353/".
This file NOT include this repository.
If you need file, please get above web sites.

problem : The WordSimilarity-353 Test Collectionの評価データを入力とし，
          1列目と2列目の単語の類似度を計算し，各行の末尾に類似度の値を追加する
          プログラムを作成せよ．
          このプログラムを85で作成した単語ベクトル，
          90で作成した単語ベクトルに対して適用せよ．

"""
import zipfile

from problem_no_86 import load_x_vector_svd_result
from problem_no_86 import search_t_word_index
from problem_no_87 import two_words_similarity
from problem_no_90 import word_convert_to_vector_model


def problem_no_94():
    with zipfile.ZipFile("./wordsim353.zip", mode="r") as zp:

        with zp.open("combined.csv", ) as fp:
            word_sim_list = fp.readlines()

    header = word_sim_list[0].decode(encoding="utf8").rstrip() + ",cos_dist\n"

    x_vector = load_x_vector_svd_result(norm=True)

    corpus_file_path = "../chapter_09/en_wiki_corpus_mod.txt"
    model_file_path = "./en_wiki.model"
    model = word_convert_to_vector_model(corpus_file_path, model_file_path)

    word2vec_word_list = model.wv.index2entity
    x_vector_list = [header]
    word2vec_list = [header]

    for line in word_sim_list[1:]:
        word_sim = line.decode(encoding="utf8").rstrip().split(",")
        word_a, word_b, score = word_sim
        print(word_a, word_b, score)

        if not search_t_word_index(word_a) or not search_t_word_index(word_b):
            result_x_vector = ""

        else:
            result_x_vector = two_words_similarity(word_a, word_b, x_vector)

        print(result_x_vector)

        x_vector_str = ",".join([word_a, word_b, score, str(result_x_vector)])
        x_vector_list.append(x_vector_str + "\n")

        if word_a not in word2vec_word_list \
                or word_b not in word2vec_word_list:
            result_word2vec = ""

        else:
            print("word2vec")

            result_word2vec = model.wv.n_similarity([word_a], [word_b])

            print(result_word2vec)

        word2vec_str = ",".join([word_a, word_b, score, str(result_word2vec)])
        word2vec_list.append(word2vec_str + "\n")

        print("\n\n")

    filename = "./wordsim353_x_vector.txt"
    with open(filename, mode="w", encoding="utf8") as f_x_vector:
        f_x_vector.writelines(x_vector_list)

    filename = "./wordsim353_word2vec.txt"
    with open(filename, mode="w", encoding="utf8") as f_word2vec:
        f_word2vec.writelines(word2vec_list)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_94())
