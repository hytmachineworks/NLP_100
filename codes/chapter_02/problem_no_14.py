# coding = utf-8
"""
create on : 2017/08/18
project name : NLP_100
file name : problem_no_14 

This problem using hightemp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 自然数Nをコマンドライン引数などの手段で受け取り，
          入力のうち先頭のN行だけを表示せよ．
          確認にはheadコマンドを用いよ．

make sure by bash command
$ head -n 5 hightemp.txt
# ex. 5rows
"""

import csv
import sys

HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_14():
    """ Visible rows get by command line argument.
        And output 1st row to input rows data.

    :return: message string
    """

    with open(HIGHTEMP_TEXT_PATH, mode="r", encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file, delimiter="\t")
        tsv_data = [row for row in reader]

    args = sys.argv

    if len(args) == 1:
        return "Not found command line argument! Please input argument"

    try:
        output_rows = int(args[1])

    except Exception as error_message:
        print(error_message)
        return "Invalid command line argument! Please retry correct numbers."

    for row_data in tsv_data[: output_rows]:
        print("\t".join(row_data))

    return "Output process complete"

if __name__ == '__main__':
    print(problem_no_14())
