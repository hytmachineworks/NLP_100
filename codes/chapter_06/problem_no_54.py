# coding = utf-8
"""
create on : 2017/12/17
project name : NLP_100
file name : problem_no_54.py 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : Stanford Core NLPの解析結果XMLを読み込み，
          単語，レンマ，品詞をタブ区切り形式で出力せよ．
"""
from problem_no_53 import get_nlp_soup


def problem_no_54():
    """ get word, lemma, and POS info from xml output

    :return: word. lemma, and POS info text
    """
    soup = get_nlp_soup()

    all_token_list = soup.find_all("token")

    tags = ["word", "lemma", "POS"]

    all_word_list = ["\t".join([token.find(tag).string for tag in tags])
                     for token in all_token_list]

    output_words = "\n".join(all_word_list)

    return output_words


if __name__ == "__main__":
    print(problem_no_54())
