# -*- coding: utf-8 -*-

"""
create on 2017/08/17
project name : NLP_100
file name : problem_no_09

This problem using hightemp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 行数をカウントせよ．確認にはwcコマンドを用いよ．

make sure by bash command
$ wc -l hightemp.txt
"""
HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_10():
    """ read hightemp.txt and count its rows

    :return: message string
    """

    with open(HIGHTEMP_TEXT_PATH, mode="r", encoding="utf-8") as f:
        text = f.readlines()

    rows = len(text)

    return "行数は、{}行です".format(rows)


if __name__ == "__main__":
    print(problem_no_10())
