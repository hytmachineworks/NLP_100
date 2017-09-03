# coding = utf-8
"""
create on : 2017/09/02
project name : NLP_100
file name : problem_no_18 

This problem using hightemp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 各行を3コラム目の数値の逆順で整列せよ
         （注意: 各行の内容は変更せずに並び替えよ）．
          確認にはsortコマンドを用いよ
          （この問題はコマンドで実行した時の結果と合わなくてもよい）．

make sure by bash command
sort -n -r -k 3 hightemp.txt
"""

import csv
from pprint import pprint

HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_18():
    """ read hightemp.txt and sorted by column #3.

    :return: sorted data. list
    """

    with open(HIGHTEMP_TEXT_PATH, mode="r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        tsv_data = [row for row in reader]

    sorted_data = sorted(tsv_data, key=lambda x: x[2], reverse=True)

    return sorted_data

if __name__ == '__main__':
    pprint(problem_no_18())
