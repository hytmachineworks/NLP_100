# coding = utf-8
"""
create on : 2017/08/06
project name : NLP_100
file name : problem_no_06 

problem : "paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，それぞれ, XとYとして求め，
          XとYの和集合，積集合，差集合を求めよ．さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""

from codes.chapter_01.problem_no_05 import generate_n_gram


def problem_no_06():
    """ calculate bi-gram sets
    :return: result message
    """

    x_string = "paraparaparadise"
    y_string = "paragraph"

    x = set(generate_n_gram(x_string, 2))
    y = set(generate_n_gram(y_string, 2))

    set_add = x | y
    set_and = x & y

    set_diff_x = x - y

    set_diff_y = y - x

    check_bi_gram = {"se"}

    if x.issuperset(check_bi_gram):
        se_contains_x = "'se'は、xに含まれます。"
    else:
        se_contains_x = "'se'は、xに含まれません。"

    if y.issuperset(check_bi_gram):
        se_contains_y = "'se'は、yに含まれます。"
    else:
        se_contains_y = "'se'は、yに含まれません。"

    return_message = "xとyの和集合 : {}\n".format(set_add)
    return_message += "xとyの積集合 : {}\n".format(set_and)
    return_message += "xとyの差集合(x-y) : {}\n".format(set_diff_x)
    return_message += "xとyの差集合(y-x) : {}\n\n".format(set_diff_y)
    return_message += se_contains_x + "\n"
    return_message += se_contains_y

    return return_message

if __name__ == '__main__':
    print(problem_no_06())
