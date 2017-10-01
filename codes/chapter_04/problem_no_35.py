# coding = utf-8
"""
create on : 2017/10/01
project name : NLP_100
file name : problem_no_35 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．

"""
import re
from pprint import pprint

from problem_no_30 import get_neko_morpheme_list


def get_noun_chain_from_sentence(morpheme_list):
    """ get noun chain phrase from sentence

    :param morpheme_list: morpheme list of sentence
    :return: noun chain phrase list
    """

    noun_list = [morph["surface"] if morph["pos"] == "名詞" else "㌠"
                 for morph in morpheme_list]

    noun_strings = "㌧".join(noun_list)

    re_noun_list = re.findall(r"[^㌠㌧]+㌧[^㌠]+", noun_strings)

    noun_list = [re_noun.strip("㌧").split("㌧") for re_noun in re_noun_list]

    return noun_list


def problem_no_35():
    """ get all noun chain phrases

    :return: all noun chain phrases list
    """

    morpheme_list = get_neko_morpheme_list()

    all_noun_chain = []

    for morpheme in morpheme_list:
        noun_chain = get_noun_chain_from_sentence(morpheme)
        all_noun_chain += noun_chain

    return all_noun_chain


if __name__ == "__main__":
    pprint(problem_no_35())
