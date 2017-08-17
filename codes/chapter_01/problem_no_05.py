# -*- coding: utf-8 -*-
"""
create on : 2017/07/30
project name : NLP_100
file name : problem_no_05 

problem : 与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
          "I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def generate_n_gram(target_sequence, n):
    """get n-gram from sequence
    :param target_sequence: given sequence (string or list)
    :param n: determine n-gram's n (2 = bi-gram, 3 = tri-gram, etc)
    :return: calculate n-gram by list
    """
    sequence_length = len(target_sequence)
    n_gram = [target_sequence[index_no: index_no + n] for index_no in range(sequence_length)]

    return n_gram


def problem_no_05(target_sequence):
    """calculate bi-gram from given sequence
    :param target_sequence: given sequence
    :return: calculate result
    """
    string_bi_gram = generate_n_gram(target_sequence, 2)

    word_list = target_sequence.split(" ")
    word_bi_gram = generate_n_gram(word_list, 2)

    return "単語bi-gram : {}\n文字bi-gram : {}".format(word_bi_gram, string_bi_gram)

if __name__ == '__main__':
    print(problem_no_05("I am an NLPer"))
