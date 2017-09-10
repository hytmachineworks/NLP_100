# -*- coding: utf-8 -*-
"""
create on : 2017/08/15
project name : NLP_100
file name : problem_no_09 

problem : スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，
          それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
          ただし，長さが４以下の単語は並び替えないこととする．
          適当な英語の文
          （例えば"I couldn't believe that I could actually understand
          what I was reading : the phenomenal power of the human mind ."）
          を与え，その実行結果を確認せよ．
"""

import random


def shuffle_word(word):
    """ shuffle characters in word, fix first and last character.

    :param word: given word string
    :return: shuffled word string
    """
    population = word[1: -1]
    k = len(population)
    shuffled_word_list = [word[0]] + random.sample(population, k) + [word[-1]]

    shuffled_word = "".join(shuffled_word_list)

    return shuffled_word


def shuffle_sentence(sentence):
    """shuffle words in sentence by function shuffle_word

    :param sentence: given sentence
    :return: shuffled sentence
    """
    word_list = sentence.split(" ")

    shuffled_sentence_list = [word if len(word) <= 4 else shuffle_word(word)
                              for word in word_list]

    shuffled_sentence = " ".join(shuffled_sentence_list)

    return shuffled_sentence


def problem_no_09():
    """ try to shuffle words in sentence and provide new sentence

    :return: message string
    """

    original_message = ("I couldn't believe that I could actually understand "
                        "what I was reading "
                        ": the phenomenal power of the human mind .")

    print("original message : ", original_message)

    for i in range(100):
        shuffled_sentence = shuffle_sentence(original_message)
        print("try no.{0:0>3} : {1}".format(i, shuffled_sentence))

    return "complete"


if __name__ == "__main__":
    print(problem_no_09())
