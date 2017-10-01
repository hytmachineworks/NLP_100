# coding = utf-8
"""
create on : 2017/10/01
project name : NLP_100
file name : problem_no_34 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 2つの名詞が「の」で連結されている名詞句を抽出せよ．

"""
from pprint import pprint

from problem_no_30 import get_neko_morpheme_list


def get_noun_phrase(morpheme_list, no):
    """ get 'の' between noun and noun phrase

    :param morpheme_list: sentence morpheme list
    :param no: find 'の' index no
    :return: noun phrase
    """
    before = morpheme_list[no - 1]
    current = morpheme_list[no]
    after = morpheme_list[no + 1]

    phrase = ""

    if before["pos"] == "名詞" and after["pos"] == "名詞":
        phrase = [before["surface"], current["surface"], after["surface"]]

    return phrase


def get_noun_phrase_from_sentence(morpheme_list):
    """ first find a connecter 'の' and find 'の' between noun and noun phrase

    :param morpheme_list: sentence morpheme list
    :return: noun phrase list
    """

    phrase_list = []

    total_count = len(morpheme_list) - 1

    for no, morpheme in enumerate(morpheme_list):
        surface = morpheme["surface"]
        pos1 = morpheme["pos1"]

        phrase = ""

        if surface == "の" and pos1 == "連体化" and no < total_count:
            phrase = get_noun_phrase(morpheme_list, no)

        if phrase:
            phrase_list.append(phrase)

    return phrase_list


def problem_no_34():
    """ first all find a connecter 'の'
        and find 'の' between noun and noun phrase

    :return: all noun phrase list
    """

    morpheme_list = get_neko_morpheme_list()

    all_noun_phrase_list = []

    for morpheme in morpheme_list:
        all_noun_phrase_list += get_noun_phrase_from_sentence(morpheme)

    return all_noun_phrase_list


if __name__ == "__main__":
    pprint(problem_no_34())
