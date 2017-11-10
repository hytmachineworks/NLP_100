# coding = utf-8
"""
create on : 2017/11/08
project name : NLP_100
file name : problem_no_43

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 名詞を含む文節が，動詞を含む文節に係るとき，
          これらをタブ区切り形式で抽出せよ．
          ただし，句読点などの記号は出力しないようにせよ．
"""
from problem_no_41 import get_neko_chunk_list
from problem_no_42 import source_and_destination


def problem_no_43():
    """ get all source and destination only include verb phrase pairs

    :return: message
    """
    neko_chunk_list = get_neko_chunk_list()

    for neko_chunk in neko_chunk_list:

        src_dst_list = source_and_destination(neko_chunk,
                                              dst_pos_include="動詞")

        if src_dst_list:

            print("<-- split sentence")

            output_string = "\n".join(src_dst_list)
            # print_string = output_string.replace("\t", " => ")
            print(output_string)

            print("split sentence -->\n")

    return "program finished"


if __name__ == "__main__":
    print(problem_no_43())
