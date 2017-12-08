# coding = utf-8
"""
create on : 2017/11/26
project name : NLP_100
file name : problem_no_49 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 文中のすべての名詞句のペアを結ぶ最短係り受けパスを抽出せよ．
          ただし，名詞句ペアの文節番号がiiとjj（i<ji<j）のとき，
          係り受けパスは以下の仕様を満たすものとする．

          問題48と同様に，パスは開始文節から終了文節に至るまでの
          各文節の表現（表層形の形態素列）を"->"で連結して表現する
          文節iiとjjに含まれる名詞句はそれぞれ，XとYに置換する
          また，係り受けパスの形状は，以下の2通りが考えられる．

          文節iiから構文木の根に至る経路上に文節jjが存在する場合:
          >文節iiから文節jjのパスを表示

          上記以外で，文節iiと文節jjから構文木の根に至る経路上で共通の文節kkで交わる場合:
          >文節iiから文節kkに至る直前のパスと文節jjから文節kkに至る直前までのパス，
           文節kkの内容を"|"で連結して表示

"""
from itertools import product

from problem_no_41 import get_neko_chunk_list
from problem_no_42 import chunk_include_pos_detect
from problem_no_45 import get_argument_from_chunk

CONNECT = " -> "
CROSS = " | "


def get_noun_to_end_path(start_index, chunk_sentence):
    """ get a path from noun to end phrase

    :param start_index: phrase index on sentence list integer
    :param chunk_sentence: chunk sentence list
    :return: path list shown by index
    """

    path = [start_index]

    dst = chunk_sentence[start_index].dst

    while dst != -1:
        path.append(dst)

        dst = chunk_sentence[dst].dst

    return path


def get_direct_path(x_path, noun_pair, chunk_sentence):
    """ get noun direct path string

    :param x_path: x string path
    :param noun_pair: y and y noun pair list
    :param chunk_sentence: chunk sentence list
    :return: path string
    """

    x_chunk, y_chunk = noun_pair

    x_index, x_phrase, x_noun = x_chunk
    y_index, y_phrase, y_noun = y_chunk

    path = ""

    for chunk_index in x_path:

        if chunk_index == x_index:
            path += x_phrase.replace(x_noun, "X")

        elif chunk_index == y_index:
            path += "Y"
            # path += y_phrase.replace(y_noun, "Y")
            break

        else:
            path += get_argument_from_chunk(chunk_sentence[chunk_index])

        path += CONNECT

    return path


def get_cross_path(xy_path, noun_pair, chunk_sentence):
    """ get noun cross path string

    :param xy_path: x and y string path
    :param noun_pair: y and y noun pair list
    :param chunk_sentence: chunk sentence list
    :return: path string
    """
    x_chunk, y_chunk = noun_pair

    x_index, x_phrase, x_noun = x_chunk
    y_index, y_phrase, y_noun = y_chunk

    x_path, y_path = xy_path
    xy_path_dic = {i: [] for i in range(len(chunk_sentence))}

    for x in x_path:
        xy_path_dic[x].extend("X")

    for y in y_path:
        xy_path_dic[y].extend("Y")

    xy_concat_path = list(set(x_path) | set(y_path))
    cross_list = list(set(x_path) & set(y_path))
    end_index = cross_list[0]

    result_path_index = [xy for xy in xy_concat_path if xy <= end_index]

    path = ""

    for no, chunk_index in enumerate(result_path_index):

        if chunk_index == x_index:
            path += x_phrase.replace(x_noun, "X")

        elif chunk_index == y_index:
            path += y_phrase.replace(y_noun, "Y")

        else:
            path += get_argument_from_chunk(chunk_sentence[chunk_index])

        if chunk_index == end_index:
            break

        elif xy_path_dic[chunk_index] != xy_path_dic[result_path_index[no+1]]:
            path += CROSS

        else:
            path += CONNECT

    return path


def get_noun_phrase_path_list(chunk_sentence, noun_pair_list):
    """ get all noun phrase path cross or direct path on sentence

    :param chunk_sentence: chunk sentence list
    :param noun_pair_list: noun pair list
    :return: path string list
    """

    path_list = []

    for noun_pair in noun_pair_list:

        x_chunk, y_chunk = noun_pair

        x_index, x_phrase, x_noun = x_chunk
        y_index, y_phrase, y_noun = y_chunk

        x_path = get_noun_to_end_path(x_index, chunk_sentence)
        y_path = get_noun_to_end_path(y_index, chunk_sentence)

        if y_index in x_path:
            path_data = get_direct_path(x_path, noun_pair, chunk_sentence)

        else:
            xy_path = (x_path, y_path)
            path_data = get_cross_path(xy_path, noun_pair, chunk_sentence)

        path_list.append(path_data)

    return path_list


def get_all_noun_pare(chunk_sentence):
    """ get all noun x noun pair

    :param chunk_sentence: chunk sentence list
    :return: noun pair list
    """
    noun_list = []

    for index, chunk in enumerate(chunk_sentence):
        phrase_flag = chunk_include_pos_detect(chunk, detect_pos="名詞")

        if phrase_flag:
            phrase_noun_list = [morph.surface for morph in chunk.morphs
                                if morph.pos == "名詞"]

            noun = phrase_noun_list[0]
            argument = get_argument_from_chunk(chunk)

            noun_list.append([index, argument, noun])

    noun_pair_list = [sorted(list(noun_pair), key=lambda x: noun_list.index(x))
                      for noun_pair in product(noun_list, noun_list)
                      if noun_pair[0][0] < noun_pair[1][0]]

    return noun_pair_list


def problem_no_49():
    """ get all path start with noun to direct or cross noun path

    :return: message
    """

    neko_chunk_list = get_neko_chunk_list()

    neko_chunk = neko_chunk_list[7]

    neko_noun_pare = get_all_noun_pare(neko_chunk)

    neko_path_list = get_noun_phrase_path_list(neko_chunk, neko_noun_pare)

    for neko_path in neko_path_list:
        print(neko_path)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_49())
