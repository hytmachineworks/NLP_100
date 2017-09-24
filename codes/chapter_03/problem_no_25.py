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
import html
import regex
from pprint import pprint
from problem_no_20 import get_country_info


def get_country_basic_info_text():
    """ find out country basic info from markup string

    :return: find out country basic info text
    """

    country_info = get_country_info()

    pattern = r"(?<group>\{{2}(?:[^{}]+|(?&group))*\}{2})"
    bracket_list = regex.findall(pattern, country_info)

    basic_info_text = ""

    for bracket_text in bracket_list:
        if "{{基礎情報" in bracket_text:
            basic_info_text = bracket_text
            break

    if not basic_info_text:
        raise KeyError("Not found country basic info.")

    basic_info_text = html.unescape(basic_info_text)

    return basic_info_text


def get_country_basic_info_text_to_list(basic_info_text):
    """ get country basic info from text to list

    :param basic_info_text: country basic info text
    :return: country basic info list
    """
    pattern = r"\|[^|[\]=]+=.*?\n(?=[|][^|=[\]]+=|\}\}$)"
    basic_info_split = regex.findall(pattern, basic_info_text, regex.DOTALL)

    country_list = []

    for item in basic_info_split:
        item_split = item.strip("|").split("=")
        item_list = [item_split[0], "=".join(item_split[1:])]
        item_data = [data.strip() for data in item_list]

        country_list.append(item_data)

    return country_list


def get_country_basic_info_text_to_dic(basic_info_text):
    """ get country basic info from text to dictionary

    :param basic_info_text: country basic info text
    :return: country basic info dictionary
    """

    country_list = get_country_basic_info_text_to_list(basic_info_text)
    country_dic = dict(country_list)

    return country_dic


def get_country_basic_info():
    """ get country basic info from gzip file

    :return: country basic info dic
    """

    basic_info_text = get_country_basic_info_text()

    country_dic = get_country_basic_info_text_to_dic(basic_info_text)

    return country_dic


def problem_no_25():
    """ get country basic info from gzip file

    :return: country basic info dic
    """

    return get_country_basic_info()


if __name__ == "__main__":
    pprint(problem_no_25())
