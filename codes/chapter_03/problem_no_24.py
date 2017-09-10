# coding = utf-8
"""
create on : 2017/09/10
project name : NLP_100
file name : problem_no_24 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 記事から参照されているメディアファイルをすべて抜き出せ

"""

from problem_no_20 import get_country_info
import re
from pprint import pprint


def get_all_media_file_list():
    """ find all media file list

    :return: linked media file list
    """

    country_info = get_country_info(listed=True)

    all_media_file_list = []

    for item in country_info:

        direct_file = re.match(r".* = [_ .,0-9a-zA-Z]*\.[0-9a-zA-Z]{3}$", item)
        titled_file = re.match(r"(File|ファイル):.*\]", item)

        if direct_file:
            direct_file_text = direct_file.group()

            direct_repl = re.match(r".* = ", direct_file_text)
            direct_file_name = direct_file_text.replace(direct_repl.group(), "")

            all_media_file_list.append(direct_file_name)

        elif titled_file:
            titled_file_text = titled_file.group()

            titled_file_head = re.match(r"(File|ファイル):", titled_file_text)
            titled_file_name = titled_file_text.replace(titled_file_head.group(), "")

            titled_file_foot = re.search(r"\|.*\]", titled_file_text)
            titled_file_name = titled_file_name.replace(titled_file_foot.group(), "")

            all_media_file_list.append(titled_file_name)

    return all_media_file_list


def problem_no_24():
    """ find all media file list

    :return: linked media file list
    """

    return get_all_media_file_list()


if __name__ == "__main__":
    pprint(problem_no_24())
