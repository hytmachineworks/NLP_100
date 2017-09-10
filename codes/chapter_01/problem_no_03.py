# -*- coding: utf-8 -*-
"""
create on : 2017/07/30
project name : NLP_100
file name : problem_no_03 

problem : 「パトカー」＋「タクシー」の文字を先頭から交互に連結して文字列「パタトクカシーー」を得よ．
"""


def problem_no_03(patrol_string, taxi_string):
    """Get a new string from two strings

    :param patrol_string: given first string
    :param taxi_string: given second string
    :return: new connected string
    """

    new_string = "".join([patrol + taxi for patrol, taxi in zip(patrol_string, taxi_string)])

    return new_string


if __name__ == "__main__":
    a_string = "パトカー"
    b_string = "タクシー"
    print(problem_no_03(a_string, b_string))
