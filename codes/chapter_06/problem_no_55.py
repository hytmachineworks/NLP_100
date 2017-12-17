# coding = utf-8
"""
create on : 2017/12/17
project name : NLP_100
file name : problem_no_55 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 入力文中の人名をすべて抜き出せ．
"""
from problem_no_53 import get_nlp_soup


def problem_no_55():
    """ get all person's name

    :return: name list
    """
    soup = get_nlp_soup()

    tokens_list = soup.find_all("token")

    name_list = [token.find("word").string for token in tokens_list
                 if token.find("NER").string == "PERSON"]

    return name_list


if __name__ == "__main__":
    print(problem_no_55())
