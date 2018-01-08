# coding = utf-8
"""
create on : 2017/12/09
project name : NLP_100
file name : problem_no_50 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : (. or ; or : or ? or !) → 空白文字 → 英大文字というパターンを
          文の区切りと見なし，入力された文書を1行1文の形式で出力せよ．

"""
import re


def get_all_sentences():
    """ process to 1 row 1 sentence text from given text

    :return: processed sentence text
    """
    with open("./nlp.txt", mode="r", encoding="utf-8") as f:
        nlp_txt = f.read()

    sentence_list = re.findall(r"[A-Z].*?[.;:?!](?=[^\S]\s*[A-Z]?)", nlp_txt)

    return "\n".join(sentence_list)


def problem_no_50():
    """ process to 1 row 1 sentence text from given text

    :return: message
    """

    print(get_all_sentences())

    return "program finished"


if __name__ == "__main__":
    print(problem_no_50())
