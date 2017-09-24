# coding = utf-8
"""
create on : 2017/09/21
project name : NLP_100
file name : problem_no_29 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : テンプレートの内容を利用し，国旗画像のURLを取得せよ

"""
import json
import requests
from urllib.parse import quote

from problem_no_27 import problem_no_27

BASE_URL = "https://ja.wikipedia.org/w/api.php"


def problem_no_29():
    """get flag image url data from country basic info data

    :return: flag url string
    """

    country_info_dic = problem_no_27()

    flag_file_name = country_info_dic["国旗画像"]

    media_wiki_api = "?action=query&format=json&titles=File:"
    media_wiki_api += quote(flag_file_name)
    media_wiki_api += "&prop=imageinfo&iiprop=url"

    response = requests.get(BASE_URL + media_wiki_api)

    json_string = response.content.decode(encoding="utf-8")

    json_origin_data = json.loads(json_string)

    flag_url = ""
    dict_data = json_origin_data

    while len(flag_url) == 0:

        if isinstance(dict_data, dict):
            dict_keys = list(dict_data)
        else:
            dict_keys = [i for i in range(len(dict_data))]

        for key in dict_keys:
            buff = dict_data[key]

            if "url" in str(buff):
                dict_data = buff
                break

            if key == "url":
                flag_url = dict_data[key]
                break

    return flag_url


if __name__ == "__main__":
    print(problem_no_29())
