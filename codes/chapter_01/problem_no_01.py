# -*- coding: utf-8 -*-
"""
create on : 2017/07/30
project name : NLP_100
file name : problem_no_01

problem : 文字列"stressed"の文字を逆に（末尾から先頭に向かって）並べた文字列を得よ．
"""


def problem_no_01(target_string):
    """ get reversed strings

    :param target_string: given strings
    :return: reversed string
    """
    new_string = target_string[::-1]

    return new_string


if __name__ == '__main__':
    print(problem_no_01("stresssed"))
