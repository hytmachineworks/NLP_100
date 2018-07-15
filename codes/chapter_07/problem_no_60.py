# coding = utf-8
"""
create on : 2018/02/21
project name : NLP_100
file name : problem_no_60 

This problem using artist.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : Key-Value-Store (KVS) を用い，アーティスト名（name）から
          活動場所（area）を検索するためのデータベースを構築せよ．
"""
import time

import gzip
import json
import redis
from tqdm import tqdm


def get_redis_connection(host="localhost", port=6379, db=0):
    """ get redis connection pool and redis instance

    :param host: host name or ip address
    :param port: specify port number
    :param db: database number
    :return: connection pool and redis instance
    """

    pool = redis.ConnectionPool(host=host, port=port, db=db)
    r = redis.StrictRedis(connection_pool=pool)

    return pool, r


def set_all_data(key_value_dict, host="127.0.0.1", port=6379, db=0):
    """ set all key value datas

    :param key_value_dict: set to db datas(key value dictionary)
    :param host: host name or ip address
    :param port: specify port number
    :param db: database number
    :return: none
    """

    start = time.time()

    key_list = list(key_value_dict.keys())

    pool, r = get_redis_connection(host=host, port=port, db=db)

    for key in tqdm(key_list):
        r.set(key, key_value_dict[key])

    end = time.time()

    print(end-start)

    print("set all data finished")


def read_json_data_to_dict(json_path):
    """ read json file to create dictionary data

    :param json_path: json file paht
    :return: dictionary data
    """

    with gzip.open(json_path, mode="rt", encoding="utf-8") as js:
        all_json_data = js.readlines()

    artist_data = [json.loads(json_data) for json_data in all_json_data]

    return artist_data


def create_key_value_dict_from_json(json_path):
    """ create key value dict from json file

    :param json_path: json file path
    :return: key value dict
    """

    artist_data = read_json_data_to_dict(json_path)

    key_value_dict = {}

    for artist in artist_data:

        artist_keys = artist.keys()
        key_value_keys = key_value_dict.keys()

        key = artist["name"]

        if "area" not in artist_keys and key not in key_value_keys:
            key_value_dict[key] = "N/A"

        elif "area" in artist_keys and key not in key_value_keys:
            value = artist["area"]
            key_value_dict[key] = value

        elif "area" in artist_keys and key_value_dict[key] == "N/A":
            value = artist["area"]

            key_value_dict[key] = value

        elif "area" in artist_keys and key_value_dict[key] != "N/A":
            value = key_value_dict[key] + "_" + artist["area"]
            key_value_dict[key] = value

    return key_value_dict


def problem_no_60():
    """ set all artist data (data format as JSON) to Radis db

    :return:
    """

    db_no = 0

    key_value_dict = create_key_value_dict_from_json("./artist.json.gz")

    # clear_db(db=db_no)

    set_all_data(key_value_dict=key_value_dict, db=db_no)

    return "program_finished"


if __name__ == "__main__":
    print(problem_no_60())
