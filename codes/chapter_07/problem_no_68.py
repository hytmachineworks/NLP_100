# coding = utf-8
"""
create on : 2018/07/21
project name : NLP_100
file name : problem_no_68 

This problem using artist.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : "dance"というタグを付与されたアーティストの中で
          レーティングの投票数が多いアーティスト・トップ10を求めよ．
"""
from problem_no_64 import connect_to_mongodb


DB_NAME = "artist_db"
COLLECTION_NAME = "artist_col"


def problem_no_68():
    """ search with 'dance' tag and find top 10 rating count artists

    :return: message
    """

    search_tag = "dance"

    client, db, collection = connect_to_mongodb(DB_NAME, COLLECTION_NAME)

    search_data = []

    for result in collection.find({"tags.value": search_tag}):
        name = result["name"]

        if "rating" in result:
            rating = result["rating"]
            rating_value = rating["count"]
            search_data.append({"name": name, "rating_count": rating_value})

    sorted_data = sorted(search_data,
                         key=lambda x: x["rating_count"],
                         reverse=True)

    for i, data in enumerate(sorted_data[:10]):
        print("#{no} : {name}, {rate}".format(no=str(i+1).rjust(2, " "),
                                              name=data["name"],
                                              rate=data["rating_count"]))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_68())
