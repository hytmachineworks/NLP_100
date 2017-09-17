# coding = utf-8
"""
create on : 2017/09/12
project name : NLP_100
file name : problem_no_26 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 25の処理時に，テンプレートの値からMediaWikiの
          強調マークアップ（弱い強調，強調，強い強調のすべて）
          を除去してテキストに変換せよ

"""
import re
from pprint import pprint

from problem_no_25 import get_country_basic_info_text
from problem_no_25 import get_country_basic_info_text_to_dic


def rm_markup(markup_string, markup_list):
    """ remove markup strings

    :param markup_string: target markup string
    :param markup_list: target markup char
    :return: cleaned strings
    """

    removed_string = markup_string

    for emphasis in markup_list:
        removed_string = removed_string.strip(emphasis)

    return removed_string


def get_country_basic_info_rm_emphasis():
    """ get country basic info, but remove all emphasis markup

    :return: removed country basic info text
    """

    basic_info_original_text = get_country_basic_info_text()

    pattern = r"'{2}[^']+'{2}|'{3}[^']+'{3}|'{5}[^']+'{5}"
    bracket_list = re.findall(pattern, basic_info_original_text)

    basic_info_text = basic_info_original_text

    markup_list = ["'''''", "'''", "''"]

    for bracket_string in bracket_list:
        removed_string = rm_markup(bracket_string, markup_list)
        basic_info_text = basic_info_text.replace(bracket_string,
                                                  removed_string)

    return basic_info_text


def problem_no_26():
    """ get country basic info, but remove all emphasis markup

    :return: country info dic
    """

    basic_info_text = get_country_basic_info_rm_emphasis()

    country_dic = get_country_basic_info_text_to_dic(basic_info_text)

    return country_dic


if __name__ == "__main__":
    pprint(problem_no_26())
