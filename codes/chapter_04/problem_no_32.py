# coding = utf-8
"""
create on : 2017/10/01
project name : NLP_100
file name : problem_no_32 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 動詞の原形をすべて抽出せよ．

"""
from pprint import pprint

from problem_no_30 import get_neko_morpheme_list
from problem_no_31 import get_verb_from_morpheme_sentence


def problem_no_32():
    """ get all verb' base list from  morphological analysis at problem no.30

    :return: all verb list
    """

    morpheme_list = get_neko_morpheme_list()

    all_verb_list = []

    for morpheme in morpheme_list:
        all_verb_list += get_verb_from_morpheme_sentence(morpheme, key="base")

    return all_verb_list


if __name__ == "__main__":
    pprint(problem_no_32())
