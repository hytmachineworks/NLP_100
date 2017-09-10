# coding = utf-8
"""
create on : 2017/09/06
project name : NLP_100
file name : problem_no_22 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．

"""

from problem_no_21 import get_country_category_line_list
import re


def problem_no_22():
    """ find all category name

    :return: category names list
    """

    category_lines = get_country_category_line_list()

    category_names = []

    for line_data in category_lines:
        start = re.search(r"^\[\[Category:", line_data).end()
        end = re.search(r"(\|.*)?\]\]$", line_data).start()
        category_names.append(line_data[start: end])

    return category_names


if __name__ == '__main__':
    print(problem_no_22())
