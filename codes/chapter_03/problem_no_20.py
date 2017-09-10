# coding = utf-8
"""
create on : 2017/09/03
project name : NLP_100
file name : problem_no_20 

This problem using jawiki-country.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : Wikipedia記事のJSONファイルを読み込み，
          「イギリス」に関する記事本文を表示せよ．
          問題21-29では，ここで抽出した記事本文に対して実行せよ．

"""

import gzip
import json


def get_country_info(target_country="イギリス", listed=False):
    """ get a country information from gzip json file

    :param listed: output string change to list split by linefeed
    :param target_country: find out country
    :return: country information string
    """

    json_file_path = "./jawiki-country.json.gz"

    with gzip.open(json_file_path, mode="rt", encoding="utf-8") as js:
        all_json_data = js.readlines()

    text = ""

    for json_data in all_json_data:
        if json.loads(json_data)["title"] == target_country:
            text = json.loads(json_data)["text"]
            break

    if not text:
        error_message = target_country
        error_message += "と言う国は登録されていません。"
        raise KeyError(error_message)

    if listed:
        line_splited_text = text.split("\n")
        return line_splited_text

    return text


def problem_no_20():
    """ read a gzip json file
        and find out "イギリス" country information.

    :return: "イギリス" country information.
    """

    target_country = "イギリス"

    return get_country_info(target_country)


if __name__ == '__main__':
    print(problem_no_20())
