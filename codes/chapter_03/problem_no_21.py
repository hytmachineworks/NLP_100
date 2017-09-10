# coding = utf-8
"""
create on : 2017/09/06
project name : NLP_100
file name : problem_no_21 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 記事中でカテゴリ名を宣言している行を抽出せよ．

"""

from problem_no_20 import get_country_info
import re
from pprint import pprint


def get_country_category_line_list():
    """ find a line definition of category name

    :return: find lines list
    """

    country_info = get_country_info(listed=True)

    category_def_line = [line_data for line_data in country_info
                         if re.match(r"^\[\[Category:.*\]\]$", line_data)]

    return category_def_line


def problem_no_21():
    """ find a line definition of category name

    :return: find lines list
    """

    return get_country_category_line_list()


if __name__ == "__main__":
    pprint(problem_no_21())
