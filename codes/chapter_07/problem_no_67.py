# coding = utf-8
"""
create on : 2018/07/21
project name : NLP_100
file name : problem_no_67 

This problem using artist.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 特定の（指定した）別名を持つアーティストを検索せよ．
"""
from problem_no_64 import connect_to_mongodb
from pprint import pprint


DB_NAME = "artist_db"
COLLECTION_NAME = "artist_col"


def problem_no_67(aliase_name):
    """ query artist to have explicit alias name

    :param aliase_name: explicit alias name
    :return: message
    """

    client, db, collection = connect_to_mongodb(DB_NAME, COLLECTION_NAME)

    for result in collection.find({"aliases.name": aliase_name}):
        pprint(result)

    return "program finished"


def main():
    """ input alias name and query artist

    :return: message
    """

    alias_name = "Queen"
    print(problem_no_67(alias_name))


if __name__ == "__main__":
    main()
