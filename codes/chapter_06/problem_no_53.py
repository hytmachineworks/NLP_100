# coding = utf-8
"""
create on : 2017/12/13
project name : NLP_100
file name : problem_no_53 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : Stanford Core NLPを用い，入力テキストの解析結果をXML形式で得よ．
          また，このXMLファイルを読み込み，入力テキストを1行1単語の形式で出力せよ．
"""
from bs4 import BeautifulSoup


def get_nlp_soup():

    with open("./nlp.txt.xml", mode="r") as f:
        xml = f.read()

    soup = BeautifulSoup(xml, "xml")

    return soup


def problem_no_53():
    """ tokenize nlp.txt to get result on xml format by Stanford NLP Core,
        and read xml output result get tokenize word.

    :return: tokenize words
    """

    soup = get_nlp_soup()

    words_list = [word.string for word in soup.find_all("word")]

    word = "\n".join(words_list)

    return word


if __name__ == "__main__":
    print(problem_no_53())
