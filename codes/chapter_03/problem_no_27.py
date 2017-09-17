# coding = utf-8
"""
create on : 2017/09/17
project name : NLP_100
file name : problem_no_27 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 26の処理に加えて，テンプレートの値から
          MediaWikiの内部リンクマークアップを除去し，
          テキストに変換せよ

"""
import re
from pprint import pprint

from problem_no_25 import get_country_basic_info_text_to_dic
from problem_no_26 import get_country_basic_info_rm_emphasis
from problem_no_26 import rm_markup


def get_country_basic_info_rm_internal_link():
    """ get country basic info, but remove all emphasis markup,
        and additionally remove internal links.

    :return: country basic info text
    """

    basic_info_original_text = get_country_basic_info_rm_emphasis()

    pattern = r"\[{2}[^\[]+\]{2}"
    bracket_list = re.findall(pattern, basic_info_original_text)

    markup_list = ["[[", "]]"]

    basic_info_text = basic_info_original_text

    for bracket_string in bracket_list:
        removed_string = rm_markup(bracket_string, markup_list)
        removed_string = removed_string.split("|")[-1]

        basic_info_text = basic_info_text.replace(bracket_string,
                                                  removed_string)

    return basic_info_text


def problem_no_27():
    """ get country basic info, but remove all emphasis markup,
        and additionally remove internal links.

    :return: country info dic
    """

    basic_info_text = get_country_basic_info_rm_internal_link()

    country_dic = get_country_basic_info_text_to_dic(basic_info_text)

    return country_dic


if __name__ == "__main__":
    pprint(problem_no_27())
