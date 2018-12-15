# coding = utf-8
"""
create on : 2018/11/04
project name : NLP_100
file name : problem_no_80 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 文を単語列に変換する最も単純な方法は，空白文字で単語に区切ることである．
          ただ，この方法では文末のピリオドや括弧などの記号が単語に含まれてしまう．
          そこで，コーパスの各行のテキストを空白文字でトークンのリストに分割した後，
          各トークンに以下の処理を施し，単語から記号を除去せよ．

        　 ・トークンの先頭と末尾に出現する次の文字を削除: .,!?;:()[]'"
        　 ・空文字列となったトークンは削除

         以上の処理を適用した後，トークンをスペースで連結してファイルに保存せよ．

"""
import bz2
import re

from tqdm import tqdm


def problem_no_80():
    """ strip symbol and remove no word token

    :return:message string
    """

    file_path = "./enwiki-20150112-400-r10-105752.txt.bz2"

    with bz2.open(file_path, mode="r") as f:
        byte_datas = f.readlines()

    re_comp_start = re.compile(r"^[.,!?;:()[\]'\"#@=“”’ —…–（），~：［·+\-«]*")
    re_comp_end = re.compile(r"[.,!?;:()[\]'\"#@=“”’ —…–（），~：［·+\-$»]*$")

    re_html = re.compile(r"[<＜][/a-zA-Z].*?[>＞]")

    corpus_data = []

    for byte_data in tqdm(byte_datas):

        text = byte_data.decode()

        text = re.sub(r"\s", " ", text)
        text = re.sub(r"</?\s?br/?>", " ", text)
        text = text.replace("{", " {")
        text = text.replace("}", "} ")
        text = text.replace("[", " [")
        text = text.replace("]", "] ")
        text = text.replace("(", " (")
        text = text.replace("(", ") ")
        text = text.replace("…", "… ")
        text = text.replace("—", "— ")
        text = text.replace("-", "- ")
        text = text.replace("’", "'")
        text = text.replace("“", '"')
        text = text.replace("”", '"')
        text = text.replace('"', ' " ')
        text = text.replace("$$", "$")
        text = text.replace("$$", "$")
        text = text.replace("$$", "$")
        text = text.replace("$$", "$")

        html_tags = re_html.findall(text)

        for html_tag in html_tags:
            text = text.replace(html_tag, "")

        token_org_list = text.split(" ")

        token_list = []

        for token_org in token_org_list:

            re_start = re_comp_start.match(token_org)
            re_end = re_comp_end.search(token_org)
            re_start_pos = re_start.span()[1]
            re_end_pos = re_end.span()[0]

            result = token_org[re_start_pos: re_end_pos]

            if "http" in result:
                result = ""

            result = re.sub(r"[,.0-9]+", "0000", result)

            if result:
                token_list.append(result)

        if token_list:
            corpus_data.append(" ".join(token_list)+"\n")

    with open("./en_wiki_corpus.txt", mode="w", encoding="utf-8") as f:
        f.writelines(corpus_data)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_80())
