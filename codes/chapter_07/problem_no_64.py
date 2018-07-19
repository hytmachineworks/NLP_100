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


def connect_to_mongodb(db_name, collection_name, host="localhost", port=27017):
    """ connect to mongodb

    :param db_name: database name string
    :param collection_name: collection name string
    :param host: host address string
    :param port: mongodb port no int
    :return:
    """

    client = MongoClient(host, port)

    db = client[db_name]

    collection = db[collection_name]

    return client, db, collection


def problem_no_64():
    """ create db, collection and insert data and make multi index

    :return: message
    """

    db_name = "artist_db"
    collection_name = "artist_col"

    client, db, collection = connect_to_mongodb(db_name, collection_name)

    # reset database
    client.drop_database(db)
    del db, collection

    client, db, collection = connect_to_mongodb(db_name, collection_name)

    artist_data = read_json_data_to_dict("./artist.json.gz")

    result = collection.insert_many(artist_data)
    print(result)

    field_list = ["name", "aliases.name", "tags.value", "rating.value"]

    for field in field_list:
        print("create index on ", field)
        print(collection.create_index([(field, ASCENDING)]))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_64())
