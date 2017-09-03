# coding = utf-8
"""
create on : 2017/09/02
project name : NLP_100
file name : problem_no_19 
problem : 各行の1列目の文字列の出現頻度を求め，
          その高い順に並べて表示せよ．
          確認にはcut, uniq, sortコマンドを用いよ．

make sure by bash command
cut -f 1 hightemp.txt | sort | uniq -c | sort -r
"""

import csv
from collections import Counter
from operator import itemgetter
from pprint import pprint

HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_19():
    """ read hightemp.txt and count up 1st columns string count.
        And sorted by counted values.

    :return: sorted 1st column data and counts. list
    """

    with open(HIGHTEMP_TEXT_PATH, mode="r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        first_row_data = [row[0] for row in reader]

    uniq_count = Counter(first_row_data)

    uniq_data = [[count, unique] for unique, count in uniq_count.most_common()]

    output_data = sorted(uniq_data, key=itemgetter(0, 1), reverse=True)

    return output_data

if __name__ == '__main__':
    pprint(problem_no_19())
