# coding = utf-8
"""
create on : 2018/07/21
project name : NLP_100
file name : problem_no_68 

This problem using artist.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : "dance"というタグを付与されたアーティストの中で
          レーティングの投票数が多いアーティスト・トップ10を求めよ．
"""
from problem_no_69.mongo_function import problem_no_68

# Please sea all program file "./problem_no_69/mongo_function.py
# this modify is to applove for pep8 on problem no.68,69.

if __name__ == "__main__":
    print(problem_no_68())
