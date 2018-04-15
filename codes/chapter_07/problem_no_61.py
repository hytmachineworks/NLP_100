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


def get_target_data(key_str, pool, r):
    """ get individual datas

    :param key_str: key string
    :param pool: connection pool
    :param r: redis instance
    :return: none
    """

    command_name = "GET"
    connection = pool.get_connection(command_name)

    try:
        connection.send_command(command_name, key_str)
        return_value = connection.read_response()

    except (ConnectionError, TimeoutError) as e:
        connection.disconnect()
        if not connection.retry_on_timeout and isinstance(e, TimeoutError):
            raise
        connection.send_command(command_name)

        return r.parse_response(connection, command_name)

    finally:
        pool.release(connection)

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

        pool, r = get_redis_connection()

        value = get_target_data(key_str, pool, r)

        print("area is {}".format(value))

        print("-"*10)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_61())
