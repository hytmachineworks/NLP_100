# coding = utf-8
"""
create on : 2018/07/15
project name : NLP_100
file name : problem_no_65 

This problem using artist.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : MongoDBのインタラクティブシェルを用いて，"Queen"という
          アーティストに関する情報を取得せよ．
          さらに，これと同様の処理を行うプログラムを実装せよ．

note : MongoDB shell cmds are describe on problem_no_65.cmd
"""
from problem_no_64 import connect_to_mongodb
from pprint import pprint


DB_NAME = "artist_db"
COLLECTION_NAME = "artist_col"


def problem_no_64():
    """ query item name "Queen" by using database

    :return: message
    """

    client, db, collection = connect_to_mongodb(DB_NAME, COLLECTION_NAME)

    for result in collection.find({"name": "Queen"}):
        pprint(result)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_64())
