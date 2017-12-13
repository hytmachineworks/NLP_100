# coding = utf-8
"""
create on : 2017/12/13
project name : NLP_100
file name : problem_no_52 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 51の出力を入力として受け取り，Porterのステミングアルゴリズムを適用し，
          単語と語幹をタブ区切り形式で出力せよ．
          Pythonでは，Porterのステミングアルゴリズムの実装として
          stemmingモジュールを利用するとよい．

"""
from stemming.porter2 import stem
from problem_no_51 import split_all_sentence_word


def problem_no_52():
    """ get all word and its stem output

    :return: message
    """

    words = split_all_sentence_word()

    word_list = [word for word in words.split("\n") if len(word)]

    print("word\tstem_word")

    for surface_word in word_list:
        stem_buff = stem(surface_word)

        print(surface_word+"\t"+stem_buff)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_52())
