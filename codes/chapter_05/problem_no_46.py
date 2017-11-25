# coding = utf-8
"""
create on : 2017/11/19
project name : NLP_100
file name : problem_no_46 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 45のプログラムを改変し，述語と格パターンに続けて項
          （述語に係っている文節そのもの）をタブ区切り形式で出力せよ．
          45の仕様に加えて，以下の仕様を満たすようにせよ．

          項は述語に係っている文節の単語列とする（末尾の助詞を取り除く必要はない）
          述語に係る文節が複数あるときは，助詞と同一の基準・順序でスペース区切りで並べる

"""
from problem_no_41 import get_neko_chunk_list
from problem_no_45 import predicate_analysis


def problem_no_46():
    """ get predicate, case and argument

    :return: message
    """

    neko_chunk_list = get_neko_chunk_list()

    neko_chunk = neko_chunk_list[7]

    predicate_case_list = predicate_analysis(neko_chunk, arg_flag=True)

    print(predicate_case_list)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_46())
