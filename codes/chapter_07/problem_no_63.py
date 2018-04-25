# coding = utf-8
"""
create on : 2018/04/08
project name : NLP_100
file name : problem_no_63 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）の
          リストを検索するためのデータベースを構築せよ．
          さらに，ここで構築したデータベースを用い，アーティスト名から
          タグと被タグ数を検索せよ．
"""

import gzip
import json
import random

from problem_no_60 import set_all_data
from problem_no_61 import get_target_data


def get_artist_tag_data(key_str, db=1):
    """ get artist tag information dict

    :param key_str: key strings of artist name
    :param db: database number
    :return: artist tag information dict
    """

    value = get_target_data(key_str, db=db)

    tag_value = json.loads(value) if value else {}

    return tag_value


def set_artist_tag_data(key_value_dict, db=1):
    """ set artist tag information to redis server

    :param key_value_dict: artist tag information
    :param db: database number
    :return: message
    """

    key_value_data = {key: json.dumps(key_value_dict[key])
                      for key in key_value_dict.keys()}

    set_all_data(key_value_data, db=db)

    return "set all artist tag datas"


def get_artist_tag_dict():
    """ get artist tag information dict

    :return: artist tag information dict
    """

    with gzip.open("./artist.json.gz", mode="rt", encoding="utf-8") as js:
        all_json_data = js.readlines()

    artist_data = [json.loads(json_data) for json_data in all_json_data]

    key_value_dict = {}

    for artist in artist_data:
        key = artist["name"]

        if key in key_value_dict.keys():
            buff_value_dict = key_value_dict[key]

        else:
            buff_value_dict = {}

        if "tags" in artist.keys():
            tag_dict = {tag["value"]: tag["count"] for tag in artist["tags"]}

        else:
            tag_dict = {}

        for tag_key in tag_dict.keys():
            if tag_key in buff_value_dict.keys():
                buff_value_dict[tag_key] += tag_dict[tag_key]

            else:
                buff_value_dict[tag_key] = tag_dict[tag_key]

        key_value_dict[key] = buff_value_dict

    return key_value_dict


def problem_no_63():
    """ set artist tag data and get tag info

    :return: message
    """

    db = 1

    key_value_dict = get_artist_tag_dict()

    print(set_artist_tag_data(key_value_dict, db=db))

    key_list = list(key_value_dict.keys())

    random.shuffle(key_list)

    search_key_list = key_list[:50]

    for key_str in search_key_list:
        print("search :{}".format(key_str))

        print(key_value_dict[key_str])

        value = get_artist_tag_data(key_str, db=db)

        print(value)

        print("-"*10)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_63())
