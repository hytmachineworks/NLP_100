# coding = utf-8
"""
create on : 2017/12/13
project name : NLP_100
file name : problem_no_51 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 空白を単語の区切りとみなし，50の出力を入力として受け取り，
          1行1単語の形式で出力せよ．ただし，文の終端では空行を出力せよ

"""

from problem_no_50 import get_all_sentences


def split_all_sentence_word():
    """ split all word by line feed,
    and split sentence by additional line feed

    :return: word output
    """

    sentence_text = get_all_sentences()

    sentence_list = sentence_text.split("\n")

    word_list = [sentence.replace(" ", "\n") for sentence in sentence_list]

    word_text = "\n\n".join(word_list)

    return word_text


def problem_no_51():
    """ get all word output

    :return: message
    """

    print(split_all_sentence_word())

    return "program finished"


if __name__ == "__main__":
    print(problem_no_51())
