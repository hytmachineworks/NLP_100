# coding = utf-8
"""
create on : 2018/06/24
project name : NLP_100
file name : problem_no_64 

This problem using artist.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : アーティスト情報（artist.json.gz）をデータベースに登録せよ．
          さらに，次のフィールドでインデックスを作成せよ: name,
                                                   aliases.name,
                                                   tags.value,
                                                   rating.value
"""
from pymongo import ASCENDING
from pymongo import MongoClient

from problem_no_60 import read_json_data_to_dict


def problem_no_64():
    """ create db, collection and insert data and make multi index

    :return: message
    """

    db_name = "artist_db"

    client = MongoClient("localhost", 27017)

    db = client[db_name]

    collection = db["artist_col"]

    artist_data = read_json_data_to_dict("./artist.json.gz")

    result = collection.insert_many(artist_data)
    print(result)

    result = collection.create_index([("name", ASCENDING)])
    print(result)

    result = collection.create_index([("aliases.name", ASCENDING)])
    print(result)

    result = collection.create_index([("tags.value", ASCENDING)])
    print(result)

    result = collection.create_index([("rating.value", ASCENDING)])
    print(result)

    for database_name in client.database_names():
        print(database_name)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_64())
