# coding = utf-8
"""
create on : 2018/03/11
project name : NLP_100
file name : problem_no_61 

This problem using artist.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 60で構築したデータベースを用い，
          特定の（指定された）アーティストの活動場所を取得せよ．
"""
import random

from problem_no_60 import get_redis_connection
from problem_no_60 import create_key_value_dict_from_json


def get_target_data(key_str, r=None, db=0):
    """ get individual datas

    :param key_str: key string
    :param r: redis instance
    :param db: database number
    :return: none
    """

    if not r:
        pool, r = get_redis_connection(db=db)

    return_value = r.get(key_str)

    return return_value.decode()


def problem_no_61():
    """ get artist area from database by artist name

    :return: message
    """

    key_value_dict = create_key_value_dict_from_json("./artist.json.gz")
    key_list = list(key_value_dict.keys())

    random.shuffle(key_list)

    search_key_list = key_list[:10]

    for key_str in search_key_list:
        print("search :{}".format(key_str))

        value = get_target_data(key_str, db=0)

        print("area is {}".format(value))

        print("-"*10)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_61())
