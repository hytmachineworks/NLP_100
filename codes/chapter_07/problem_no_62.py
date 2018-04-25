# coding = utf-8
"""
create on : 2018/03/11
project name : NLP_100
file name : problem_no_62

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 60で構築したデータベースを用い，
          活動場所が「Japan」となっているアーティスト数を求めよ．
"""

import time

from problem_no_60 import get_redis_connection
from problem_no_61 import get_target_data


def search_area_artists(area):
    """ search artist from determine area

    :param area: search area string
    :return: search area artist list
    """

    def find_area_artist(start_cur, r):
        """ find area artist

        :param start_cur: start cursor number
        :param r: redis class
        :return: area artist list
        """

        cur, keys = r.scan(start_cur)

        find_artists = [(key.decode(), get_target_data(key.decode(), r=r))
                        for key in keys
                        if get_target_data(key.decode(), r=r) == area]

        return cur, find_artists

    start = time.time()

    area_artists = []

    cursor = 0

    flag = False

    conn_pool, redis = get_redis_connection()

    while not flag:

        cursor, search_value = find_area_artist(cursor, redis)
        area_artists += search_value

        if cursor == 0:
            flag = True

    end = time.time()

    print(end-start)

    return area_artists


def problem_no_62():
    """ find all artist by determine area

    :return: tuple list artist name and area
    """

    artist_name_area_list = search_area_artists(area="Japan")

    return artist_name_area_list


if __name__ == "__main__":
    print(problem_no_62())
