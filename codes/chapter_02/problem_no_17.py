# coding = utf-8
"""
create on : 2017/08/31
project name : NLP_100
file name : problem_no_17 

This problem using hightemp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 1列目の文字列の種類（異なる文字列の集合）を求めよ．
          確認にはsort, uniqコマンドを用いよ．

make sure by bash command
cut -f 1 hightemp.txt | sort | uniq
"""

import csv
from pprint import pprint

HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_17():
    """ read hightemp.txt
        and get unique strings in 1st row.

    :return: unique strings in 1st row.  list
    """

    with open(HIGHTEMP_TEXT_PATH, mode="r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        first_row_data = [row[0] for row in reader]

    first_row_data_uniq = sorted(list(set(first_row_data)))

    return first_row_data_uniq

if __name__ == '__main__':
    pprint(problem_no_17())
