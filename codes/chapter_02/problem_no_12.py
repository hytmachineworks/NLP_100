# -*- coding: utf-8 -*-

"""
create on 2017/08/17
project : NLP_100
filename : problem_no_12

This problem using hightemp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 各行の1列目だけを抜き出したものをcol1.txtに，
          2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．
          確認にはcutコマンドを用いよ．

make sure by bash command
$ cut -f 1 ./hightemp.txt
$ cut -f 2 ./hightemp.txt
"""
import csv

HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_12():
    """ divide 2 files from hightemp.txt by columns 1 and 2.
        and write text files to col1.txt and col2.txt

    :return: message string
    """
    with open(HIGHTEMP_TEXT_PATH, mode="r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        tsv_data = [row for row in reader]

    print(tsv_data)

    col1_list = [c1[0]+"\n" for c1 in tsv_data]
    with open("./col1.txt", mode="w", encoding="utf-8") as f:
        f.writelines(col1_list)

    col2_list = [c1[1]+"\n" for c1 in tsv_data]
    with open("./col2.txt", mode="w", encoding="utf-8") as f:
        f.writelines(col2_list)

    return "divide file complete"

if __name__ == "__main__":
    print(problem_no_12())
