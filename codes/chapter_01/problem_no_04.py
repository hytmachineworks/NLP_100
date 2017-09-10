# -*- coding: utf-8 -*-
"""
create on : 2017/07/30
project name : NLP_100
file name : problem_no_04 

problem : "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
           という文を単語に分解し，各単語の（アルファベットの）文字数を先頭から出現順に並べたリストを作成せよ．
"""


def problem_no_04(target_sentence):
    """ Exchage sentence to word length list

    :param target_sentence: given sentence
    :return: word length list
    """
    replace_char = [",", "."]
    replaced_sentence = target_sentence

    for rep_char in replace_char:
        replaced_sentence = replaced_sentence.replace(rep_char, "")

    word_list = replaced_sentence.split(" ")

    word_length_list = [len(word) for word in word_list]

    return word_length_list


if __name__ == '__main__':
    given_sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    print(problem_no_04(given_sentence))

