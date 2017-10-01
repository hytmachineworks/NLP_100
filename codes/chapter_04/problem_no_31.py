# coding = utf-8
"""
create on : 2017/09/30
project name : NLP_100
file name : problem_no_31 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 動詞の表層形をすべて抽出せよ．

"""
from pprint import pprint

from problem_no_30 import get_neko_morpheme_list


def get_value_from_morpheme_sentence(morpheme_list,
                                     pos, pos1="", key="surface"):
    """ find all pos value from morpheme list

    :param morpheme_list: morphological analysis result
    :param pos: find pos type
    :param pos1: add condition's pos1
    :param key: select return value's key
    :return: value list
    """

    if pos1:
        verb_list = [morpheme[key] for morpheme in morpheme_list
                     if morpheme["pos"] == pos and morpheme["pos1"] == pos1]

    else:
        verb_list = [morpheme[key] for morpheme in morpheme_list
                     if morpheme["pos"] == pos]

    return verb_list


def get_verb_from_morpheme_sentence(morpheme_list, key="surface"):
    """ find all verbs from morpheme list

    :param morpheme_list: morphological analysis result
    :param key: select return value's key
    :return: verb list
    """

    verb_list = get_value_from_morpheme_sentence(morpheme_list,
                                                 pos="動詞", key=key)

    return verb_list


def problem_no_30():
    """ get all verb list from  morphological analysis at problem no.30

    :return: all verb list
    """

    morpheme_list = get_neko_morpheme_list()

    all_verb_list = []

    for morpheme in morpheme_list:
        all_verb_list += get_verb_from_morpheme_sentence(morpheme)

    return all_verb_list


if __name__ == "__main__":
    pprint(problem_no_30())
