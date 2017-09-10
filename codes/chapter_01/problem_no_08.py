# -*- coding: utf-8 -*-
"""
create on : 2017/08/15
project name : NLP_100
file name : problem_no08 

problem : 与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．
            英小文字ならば(219 - 文字コード)の文字に置換
            その他の文字はそのまま出力
          この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(text):
    """ crypt text by alphabet or not.

    :param text: given text
    :return: crypt text
    """

    cipher_list = [str(219 - ord(t))
                   if t.isalpha() and t.islower() else t
                   for t in text]

    cipher_strings = "".join(cipher_list)

    return cipher_strings


def problem_no_08():
    """ test code for function cipher
    :return: message string
    """
    original_text = "Special cases aren't special enough to break the rules."
    print("original_text : ", original_text)

    crypt = cipher(original_text)
    print("crypt text : ", crypt)

    return "complete"


if __name__ == "__main__":
    print(problem_no_08())
