# coding = utf-8
"""
create on : 2018/11/24
project name : NLP_100
file name : problem_no_82

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 81で作成したコーパス中に出現するすべての単語tに関して，
          単語tと文脈語cのペアをタブ区切り形式ですべて書き出せ．
          ただし，文脈語の定義は次の通りとする．

            ・ある単語tの前後d単語を文脈語cとして抽出する
            　（ただし，文脈語に単語tそのものは含まない）
            ・単語tを選ぶ度に，文脈幅dは{1,2,3,4,5}の範囲でランダムに決める．

"""
import os
import random

from tqdm import tqdm


def problem_no_82():
    """ get all word pair list

    :return: message
    """

    output_file_path = "./en_wiki_word_pair.txt"

    if os.path.exists(output_file_path):
        os.remove(output_file_path)

    random.seed(82)

    with open("./en_wiki_corpus_mod.txt", mode="r", encoding="utf-8") as f:
        corpus_data = f.readlines()

    word_dict = {}

    for corpus in tqdm(corpus_data):

        tokens = corpus.replace("\n", "").split(" ")

        corpus_length = len(tokens) - 1

        if corpus_length == 0:
            continue

        token_pair_buff = []

        for i, token in enumerate(tokens):

            if token in word_dict.keys():
                d = word_dict[token]

            else:
                d = random.choice([1, 2, 3, 4, 5])

                word_dict[token] = d

            start = i - d if (i - d) > 0 else 0
            end = i + d

            capture_list = tokens[start: end]

            token_pair = [token + "\t" + capture for capture in capture_list
                          if token != capture]

            if token_pair:
                token_pair_buff.extend("\n".join(token_pair)+"\n")

        with open(output_file_path, mode="a", encoding="utf-8") as f:
            f.writelines(token_pair_buff)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_82())
