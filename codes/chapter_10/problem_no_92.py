# coding = utf-8
"""
create on : 2018/12/21
project name : NLP_100
file name : problem_no_92 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
and questions-words.txt
This first file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/",
And next file is avalable at
"http://download.tensorflow.org/data/questions-words.txt".
This file NOT include this repository.
If you need file, please get above web sites.

problem : 91で作成した評価データの各事例に対して，
          vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
          そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
          求めた単語と類似度は，各事例の末尾に追記せよ．
          このプログラムを85で作成した単語ベクトル，90で作成した単語ベクトルに対して
          適用せよ．

"""
from problem_no_86 import load_x_vector_svd_result
from problem_no_86 import search_t_word_index
from problem_no_89 import vector_most_similar
from problem_no_90 import word_convert_to_vector_model


def problem_no_92():
    """ analory by given 3 words

    :return: message string
    """

    x_vector = load_x_vector_svd_result(norm=True)

    corpus_file_path = "../chapter_09/en_wiki_corpus_mod.txt"
    model_file_path = "./en_wiki.model"
    model = word_convert_to_vector_model(corpus_file_path, model_file_path)

    with open("./analogy_family.txt", mode="r", encoding="utf8") as file_read:
        analogy_list = file_read.readlines()

    word2vec_word_list = model.wv.index2entity

    x_vector_list = []
    word2vec_list = []

    for line in analogy_list:
        analogy = line[:-1].split(" ")

        print("-----------------------------")
        print(analogy[3])

        # x vector word exist check
        pos_list_x_vector = [pos_word for pos_word in [analogy[1], analogy[2]]
                             if search_t_word_index(pos_word)]

        neg_list_x_vector = [neg_word for neg_word in [analogy[0]]
                             if search_t_word_index(neg_word)]

        if not pos_list_x_vector and not neg_list_x_vector:
            result_x_vector = [("", "")]

        else:

            print("x_vector")
            result_x_vector = vector_most_similar(positive=pos_list_x_vector,
                                                  negative=neg_list_x_vector,
                                                  topn=1, x_vector=x_vector,
                                                  stdout=False)

        print(result_x_vector)

        print("- - - - -")

        # word2vec word exist check
        pos_list_word2vec = [pos_word for pos_word in [analogy[1], analogy[2]]
                             if pos_word in word2vec_word_list]

        neg_list_word2vec = [neg_word for neg_word in [analogy[0]]
                             if neg_word in word2vec_word_list]

        if not pos_list_x_vector and not neg_list_x_vector:
            result_word2vec = [("", "")]

        else:
            print("word2vec")

            result_word2vec = model.wv.most_similar(positive=pos_list_word2vec,
                                                    negative=neg_list_word2vec,
                                                    topn=1)

            print(result_word2vec)

        x_vector_word = result_x_vector[0][0]
        x_vector_cos = str(result_x_vector[0][1])
        x_vector_result = " ".join(analogy + [x_vector_word, x_vector_cos])
        word2vec_word = result_word2vec[0][0]
        word2vec_cos = str(result_word2vec[0][1])
        word2vec_result = " ".join(analogy + [word2vec_word, word2vec_cos])

        x_vector_list.append(x_vector_result + "\n")
        word2vec_list.append(word2vec_result + "\n")

        print("\n\n")

    filename = "./analogy_family_x_vector.txt"
    with open(filename, mode="w", encoding="utf8") as f_x_vector:
        f_x_vector.writelines(x_vector_list)

    filename = "./analogy_family_word2vec.txt"
    with open(filename, mode="w", encoding="utf8") as f_word2vec:
        f_word2vec.writelines(word2vec_list)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_92())
