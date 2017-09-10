# coding = utf-8
"""
create on : 2017/09/06
project name : NLP_100
file name : problem_no_23 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 記事中に含まれるセクション名とそのレベル
          （例えば"== セクション名 =="なら1）を表示せよ．

"""

from problem_no_20 import get_country_info
import re
from pprint import pprint


def section_info(section_markup_text):
    """ remove section markup
        and return section name and level

    :param section_markup_text:
    :return: list
    """

    section_level = len(re.match(r"^==*", section_markup_text).group()) - 1
    markup = "=" * (section_level + 1)
    section_name = section_markup_text.replace(markup, "")

    return [section_level, section_name]


def get_section_name_and_level_list():
    """ find a section line and get name and level
        from a country info

    :return: section info list
    """

    country_info = get_country_info(listed=True)

    section_info_list = [section_info(line_data) for line_data in country_info
                         if re.match(r"^==.*==$", line_data)]

    return section_info_list


def problem_no_23():
    """ find a section line and get name and level
        from a country info

    :return: section info list
    """

    return get_section_name_and_level_list()


if __name__ == "__main__":
    pprint(problem_no_23())
