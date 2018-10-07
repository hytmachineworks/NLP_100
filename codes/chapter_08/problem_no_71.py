# coding = utf-8
"""
create on : 2018/09/30
project name : NLP_100
file name : problem_no_71 

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
          さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，
          それ以外は偽を返す関数を実装せよ．
          さらに，その関数に対するテストを記述せよ．
"""
import nltk
from nltk.corpus import stopwords

from pprint import pprint


def get_stopwords_list(file="./sentiment.txt", except_list=None):
    """ get stop words list from nltk and document

    :param file: document file path string
    :param except_list: except char from stop word list string
    :return: stop words list list
    """

    # get stopwords from NLTK
    nltk.download("stopwords")
    nltk_stopwords_list = stopwords.words("english")

    # get stopwords from document(numeric and sign)
    with open(file, mode="r", encoding="utf-8") as f:
        whole_document = f.read()

    all_except_list = ["\n", " "] + except_list if except_list else ["\n", " "]

    for except_char in all_except_list:
        whole_document = whole_document.replace(except_char, "")

    all_char_list = sorted(list(set(list(whole_document))))

    all_sign_list = [char.lower() for char in all_char_list
                     if not char.isalnum()]

    # concat nltk and document stop words
    stopwords_list = nltk_stopwords_list + all_sign_list

    return stopwords_list


def is_stopwords(word, stop_words_list=get_stopwords_list()):
    """ To verify given word is stop words or not

    :param word: check word string
    :param stop_words_list: stop words list list
    :return: verify result boolean
    """

    stopwords_or_not = True if word.lower() in stop_words_list else False

    return stopwords_or_not


def problem_no_71():
    """ make a stop word list and test verify function

    :return: message
    """

    # get stop words list
    stop_words_list = get_stopwords_list()
    pprint(stop_words_list)

    # verify stop word or not
    check_word_list = ["1", "AM", "s", "am", "'", "HYT", "machine", "works"]
    for word in check_word_list:
        print(word, is_stopwords(word, stop_words_list))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_71())
