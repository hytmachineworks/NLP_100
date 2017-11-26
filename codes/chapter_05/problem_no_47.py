# coding = utf-8
"""
create on : 2017/11/25
project name : NLP_100
file name : problem_no_47 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 動詞のヲ格にサ変接続名詞が入っている場合のみに着目したい．
          46のプログラムを以下の仕様を満たすように改変せよ．

          ・「サ変接続名詞+を（助詞）」で構成される文節が動詞に係る場合のみを対象とする
          ・述語は「サ変接続名詞+を+動詞の基本形」とし，文節中に複数の動詞があるときは，
          　最左の動詞を用いる
　　　　　　・述語に係る助詞（文節）が複数あるときは，すべての助詞をスペース区切りで
　　　　　　　辞書順に並べる
　　　　　　・述語に係る文節が複数ある場合は，すべての項をスペース区切りで並べる
　　　　　　　（助詞の並び順と揃えよ）

          make sure command written in problem_no_47.cmd

"""
from problem_no_41 import get_neko_chunk_list
from problem_no_45 import predicate_analysis


def problem_no_47():
    """ get all predicate mining result list

    :return: message
    """

    neko_chunk_list = get_neko_chunk_list()

    predicate_case_list = [predicate_analysis(neko_chunk, True, True)
                           for neko_chunk in neko_chunk_list
                           if predicate_analysis(neko_chunk, True, True)]

    with open("./neko_predicate_mining.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(predicate_case_list))

    print(predicate_case_list)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_47())
