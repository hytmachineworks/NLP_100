# coding = utf-8
"""
create on : 2017/10/01
project name : NLP_100
file name : problem_no_33 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : サ変接続の名詞をすべて抽出せよ．

"""
from pprint import pprint

from problem_no_30 import get_neko_morpheme_list
from problem_no_31 import get_value_from_morpheme_sentence


def problem_no_33():
    """ get all 'サ変接続' noun base list from
        morphological analysis at problem no.30

    :return: all noun list
    """

    morpheme_list = get_neko_morpheme_list()

    all_noun_list = []

    for morpheme in morpheme_list:
        all_noun_list += get_value_from_morpheme_sentence(morpheme,
                                                          pos="名詞",
                                                          pos1="サ変接続",
                                                          key="base")

    return all_noun_list


if __name__ == "__main__":
    pprint(problem_no_33())
