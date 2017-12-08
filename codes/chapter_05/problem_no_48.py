# coding = utf-8
"""
create on : 2017/11/26
project name : NLP_100
file name : problem_no_48 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 文中のすべての名詞を含む文節に対し，その文節から構文木の根に至るパスを抽出せよ．
          ただし，構文木上のパスは以下の仕様を満たすものとする．

          各文節は（表層形の）形態素列で表現する
          パスの開始文節から終了文節に至るまで，各文節の表現を"->"で連結する

"""
from problem_no_41 import get_neko_chunk_list
from problem_no_42 import chunk_include_pos_detect
from problem_no_45 import get_argument_from_chunk

CONNECT = " -> "


def get_phrase_path_from_index(start_index, chunk_sentence):
    """ get a path given start phrase index

    :param start_index: start index integer
    :param chunk_sentence: chunk sentence list
    :return: path string
    """

    path = [get_argument_from_chunk(chunk_sentence[start_index])]

    dst = chunk_sentence[start_index].dst

    while dst != -1:
        current_phrase = get_argument_from_chunk(chunk_sentence[dst])

        path.append(current_phrase)

        dst = chunk_sentence[dst].dst

    path_string = CONNECT.join(path)

    return path_string


def get_phrase_path_list(chunk_sentence):
    """ get all path start with noun position from given chunk sentence

    :param chunk_sentence: chunk sentence list
    :return: path list
    """

    path_list = []

    for index, chunk in enumerate(chunk_sentence):
        phrase_flag = chunk_include_pos_detect(chunk, detect_pos="名詞")

        if phrase_flag:
            path_list.append(get_phrase_path_from_index(index, chunk_sentence))

    return path_list


def problem_no_48():
    """ get all path start with noun position

    :return: message
    """

    neko_chunk_list = get_neko_chunk_list()

    neko_chunk = neko_chunk_list[7]

    neko_path_list = get_phrase_path_list(neko_chunk)

    for neko_path in neko_path_list:
        print(neko_path)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_48())
