# coding = utf-8
"""
create on : 2017/09/17
project name : NLP_100
file name : problem_no_28 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 27の処理に加えて，テンプレートの値から
          MediaWikiマークアップを可能な限り除去し，
          国の基本情報を整形せよ．

"""
import re

from problem_no_25 import get_country_basic_info_text_to_list
from problem_no_27 import get_country_basic_info_rm_internal_link


def get_country_basic_info_rm_all_markup():
    """ get country basic info, but remove all emphasis markup,
        additionally remove internal links,
        and further more remove all markups.

    :return: country basic info text
    """

    basic_info_original_text = get_country_basic_info_rm_internal_link()

    lf_pattern = r"<br ?/>"
    lf_list = re.findall(lf_pattern, basic_info_original_text)
    lf_list = list(set(lf_list))

    basic_info_rm_lf = basic_info_original_text
    for lf in lf_list:
        basic_info_rm_lf = basic_info_rm_lf.replace(lf, "\n")

    basic_info_rm_lf = basic_info_rm_lf.replace("\n\n", "\n")

    template_pattern = r"\{{2}[^{}]+?\}{2}"
    template_list = re.findall(template_pattern, basic_info_rm_lf, re.DOTALL)

    basic_info_rm_temp = basic_info_rm_lf
    for template in template_list:
        temp_buff = template.split("|")[-1]
        temp_buff = temp_buff[:-2]
        basic_info_rm_temp = basic_info_rm_temp.replace(template, temp_buff)

    href_pattern = r"\[[^\[]+\]"
    href_list = re.findall(href_pattern, basic_info_rm_temp, re.DOTALL)

    href_text_pattern = r" .*"
    basic_info_rm_href = basic_info_rm_temp
    for href_text in href_list:
        href_buff = href_text[1:-1]
        href_text_search = re.search(href_text_pattern, href_buff)
        href_str = href_text_search.group().strip(" ")
        basic_info_rm_href = basic_info_rm_href.replace(href_text, href_str)

    header_pattern = r"\*+[^*]*?\n"
    header_list = re.findall(header_pattern, basic_info_rm_href)

    header_mark_pattern = r"\*+"
    basic_info_rm_header = basic_info_rm_href
    for header in header_list:
        re_header = re.match(header_mark_pattern, header)
        header_buff = re_header.group()

        header_str = " " * (len(header_buff) - 1) + "･"
        header_replace = header.replace(header_buff, header_str)

        basic_info_rm_header = basic_info_rm_header.replace(header,
                                                            header_replace)

    ref_pattern = r"<ref[^<>/]*>.*?</ref>"
    ref_list = re.findall(ref_pattern, basic_info_rm_header, re.DOTALL)

    reference_list = []
    basic_info_rm_ref = basic_info_rm_header
    for no, ref in enumerate(ref_list):
        no_mark = "[注"+str(no+1).zfill(2)+"]"

        ref_buff = ref.replace("</ref>", "")
        ref_buff = ref_buff.replace("\n", "\n ")

        ref_name_pattern = r"<ref[^<>]*?>"
        re_name = re.match(ref_name_pattern, ref_buff)

        basic_info_rm_ref = basic_info_rm_ref.replace(ref, no_mark)

        ref_buff = ref_buff.replace(re_name.group(), no_mark)
        reference_list.append(ref_buff.strip())

        if "name" in re_name.group():
            name_pattern = re_name.group().replace(">", "[^<>]*?/>")
            name_ref = re.search(name_pattern, basic_info_rm_ref)

        else:
            name_ref = ""

        if name_ref:
            basic_info_rm_ref = basic_info_rm_ref.replace(name_ref.group(),
                                                          no_mark)

    basic_info = basic_info_rm_ref.replace("<references />",
                                           "\n".join(reference_list))

    return basic_info


def get_prettify_text(basic_info_text):
    """ get prettify basic country text

    :param basic_info_text: country basic info text
    :return: prettify basic country info text
    """
    basic_info_list = get_country_basic_info_text_to_list(basic_info_text)

    prettify_text = ""

    for title, contents in basic_info_list:
        prettify_text += "|" + title + "|\n  "\
                         + contents.replace("\n", "\n ") + "\n"

    return prettify_text.strip("\n")


def problem_no_28():
    """ get country basic info, but remove all emphasis markup,
        additionally remove internal links,
        and further more remove all markups.

    :return: country info dic
    """

    basic_info_text = get_country_basic_info_rm_all_markup()
    country_info_text = get_prettify_text(basic_info_text)

    return country_info_text


if __name__ == "__main__":
    print(problem_no_28())
