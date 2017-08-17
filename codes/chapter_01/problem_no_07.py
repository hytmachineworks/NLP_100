# coding = utf-8
"""
create on : 2017/08/15
project name : NLP_100
file name : problem_no_07 

problem : 引数x, y, zを受け取り「x時のyはz」という文字列を返す関数を実装せよ．
          さらに，x=12, y="気温", z=22.4として，実行結果を確認せよ．

"""


def make_strings_by_x_y_z(x, y, z):
    """ get x y z parameters, return "x時のyはz" strings
    :param x: hours int
    :param y: keyword string
    :param z: value int
    :return: template strings
    """

    template_strings = "{0}時の{1}は{2}".format(x, y, z)

    return template_strings


def problem_no_07():
    """ test function make_string_by_x_y_z

    :return: function result string
    """
    x = 12
    y = "気温"
    z = 22.4

    return make_strings_by_x_y_z(x, y, z)

if __name__ == '__main__':
    print(problem_no_07())
