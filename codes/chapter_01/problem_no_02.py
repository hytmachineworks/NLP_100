# -*- coding: utf-8 -*-
"""
create on : 2017/07/30
project name : NLP_100
file name : problem_no_02 

problem : 「パタトクカシーー」という文字列の1,3,5,7文字目を
           取り出して連結した文字列を得よ．
"""


def problem_no_02(target_string):
    """Get slicing string by skipping a character.

    :param target_string: given string
    :return: new sliced string
    """
    new_strings = target_string[::2]
    return new_strings


if __name__ == "__main__":
    print(problem_no_02("パタトクカシーー"))
