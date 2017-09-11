# coding = utf-8
"""
create on : 2017/09/10
project name : NLP_100
file name : problem_no_25 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，
          辞書オブジェクトとして格納せよ．

"""

from problem_no_20 import get_country_info
import re
from pprint import pprint


def get_country_basic_info():
    """ get country basic info from gzip file

    :return: country basic info dic
    """

    country_info = get_country_info()

    basic_info = re.search(r"{{基礎情報.*☆}}☆",
                           country_info.replace("\n", "☆"))
    basic_info_text = basic_info.group().replace("☆", "\n")

    basic_info_split = re.findall(r"\|[^|=]*=[^=]*\|", basic_info_text)

    country_dic = {}

    for item in basic_info_split:
        item_split = item.strip("|").split("=")
        item_data = [data.strip() for data in item_split]

        country_dic[item_data[0]] = item_data[1]

    return country_dic


def problem_no_25():
    """ get country basic info from gzip file

    :return: country basic info dic
    """

    return get_country_basic_info()


if __name__ == "__main__":
    pprint(problem_no_25())
