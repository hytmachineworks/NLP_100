# coding = utf-8
"""
create on : 2017/08/17
project name : NLP_100
file name : problem_no_13 

This problem using hightemp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 12で作ったcol1.txtとcol2.txtを結合し，
          元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
          確認にはpasteコマンドを用いよ．

makesure by bash command
$ paste col1.txt col2.txt
"""

from codes.chapter_02.problem_no_12 import problem_no_12

HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_13():
    """ combine col1.txt and col2.txt
        and separate with tab string between both columns

    :return: message string
    """

    # 12の課題を実行し、col1.txtとcol2.txtを作成
    print(problem_no_12())

    with open("./col1.txt", mode="r", encoding="utf-8") as f:
        col1_data = f.readlines()

    with open("./col2.txt", mode="r", encoding="utf-8") as f:
        col2_data = f.readlines()

    col_data = [col1.replace("\n", "\t") + col2
                for col1, col2 in zip(col1_data, col2_data)]

    with open("./col.txt", mode="w", encoding="utf-8") as f:
        f.writelines(col_data)

    return "combine complete"

if __name__ == '__main__':
    print(problem_no_13())
