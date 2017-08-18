# -*- coding: utf-8 -*-

"""
create on 2017/08/17
project : NLP_100
filename : problem_no_11

This problem using hightemp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : タブ1文字につきスペース1文字に置換せよ．
          確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ

make sure by bash command
$ expand -t 1 ./hightemp.txt
"""
HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_11():
    """ replace tab string to space string

    :return: replace tab to space strings
    """

    with open(HIGHTEMP_TEXT_PATH, mode="r", encoding="utf-8") as f:
        text = f.read()

    replace_text = text.replace("\t", " ")

    return replace_text

if __name__ == "__main__":
    print(problem_no_11())
