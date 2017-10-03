# coding = utf-8
"""
create on : 2017/10/01
project name : NLP_100
file name : problem_no_36 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．

"""
from pprint import pprint
from collections import Counter

from problem_no_30 import get_neko_morpheme_list


def get_word_count_list():
    """ get word frequency of neko.txt

    :return: frequency list tuple (word, frequency)
    """
    morpheme_list = get_neko_morpheme_list()

    word_list = []

    key = "base"
    spare_key = "surface"

    def get_word_list_from_sentence(sentence):
        """ get word frequency of sentence

        :param sentence: target sentence
        :return: frequency list tuple (word, frequency)
        """
        except_key = "pos"
        except_pos_list = ["助詞", "助動詞", "記号"]

        sentence_words_list = []

        for word in sentence:
            if word[except_key] not in except_pos_list:
                buff = word[key] if not word[key] == "*" else word[spare_key]
                sentence_words_list.append(buff)

        return sentence_words_list

    for morpheme in morpheme_list:
        word_list += get_word_list_from_sentence(morpheme)

    word_counter = Counter(word_list)

    return word_counter.most_common()


def problem_no_36():
    """ get word frequency of neko.txt

    :return: frequency list tuple (word, frequency)
    """

    word_count_list = get_word_count_list()

    return word_count_list


if __name__ == "__main__":
    pprint(problem_no_36())
