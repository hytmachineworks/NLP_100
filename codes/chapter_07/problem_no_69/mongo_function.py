# coding = utf-8
"""
create on : 2018/08/04
project name : NLP_100
file name : mongo_function 

"""
from pymongo import MongoClient

DB_NAME = "artist_db"
COLLECTION_NAME = "artist_col"


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


def decorate_item(result):
    """ decorate search result

    :param result: artist db search result list dict
    :return: dict
    """

    item_dict = {"name": result["name"]}

    if "area" in result:
        area = result["area"]
        item_dict["area"] = area
    else:
        item_dict["area"] = ""

    if "begin" in result and "year" in result["begin"]:
        begin = result["begin"]
        item_dict["begin"] = begin["year"]
    else:
        item_dict["begin"] = ""

    if "end" in result and "year" in result["end"]:
        end = result["end"]
        item_dict["end"] = end["year"]
    else:
        item_dict["end"] = ""

    if "tags" in result:
        tags = result["tags"]
        tag_list = [tag["value"] for tag in tags]
        item_dict["tags"] = ", ".join(tag_list)
    else:
        item_dict["tags"] = ""

    if "rating" in result:
        rating = result["rating"]
        rating_value = rating["count"]
        item_dict["rating_count"] = rating_value
    else:
        item_dict["rating_count"] = 0

    return item_dict


def search_items(category, keyword_str):
    """ search item from artist db

    :param category: search category type string
    :param keyword_str: query string
    :return: sorted search result item list
    """

    cat_dict = {"name": "name",
                "aliases": "name.aliases",
                "area": "area",
                "begin": "begin.year",
                "end": "end.year",
                "tags": "tags.value"}

    client, db, collection = connect_to_mongodb(DB_NAME, COLLECTION_NAME)

    search_data = []

    if category in ["begin", "end"]:
        keyword = int(keyword_str)

    else:
        keyword = keyword_str

    for result in collection.find({cat_dict[category]: keyword}):
        search_data.append(decorate_item(result))

    sorted_data = sorted(search_data,
                         key=lambda x: x["rating_count"],
                         reverse=True)

    return sorted_data


def problem_no_68():
    """ search with 'dance' tag and find top 10 rating count artists

    :return: message
    """

    search_tag = "dance"

    sorted_data = search_items("tags", search_tag)

    for i, data in enumerate(sorted_data[:10]):
        print("#{no} : {name}, {rate}".format(no=str(i+1).rjust(2, " "),
                                              name=data["name"],
                                              rate=data["rating_count"]))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_68())
