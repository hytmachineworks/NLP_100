# coding = utf-8
"""
create on : 2018/12/21
project name : NLP_100
file name : problem_no_91

This problem using questions-words.txt
This file is available at
"http://download.tensorflow.org/data/questions-words.txt".
This file NOT include this repository.
If you need file, please get above web site.

problem : 単語アナロジーの評価データ"questions-words.txt"をダウンロードせよ．
          このデータ中で": "で始まる行はセクション名を表す．
          例えば，": capital-common-countries"という行は，
          "capital-common-countries"というセクションの開始を表している．
          ダウンロードした評価データの中で，"family"というセクションに含まれる
          評価事例を抜き出してファイルに保存せよ．

"""
import re


def pickup_search_section(f, search_section):
    """ find out section items

    :param f: file object
    :param search_section: search section name string
    :return: section line list
    """

    flag = False

    re_family = re.compile(r"^: {section}".format(section=search_section))
    re_section_start = re.compile(r"^: ")

    section_list = []

    for line in f:

        if re_family.match(line):
            flag = True

            print("section start", line)

        elif flag and re_section_start.match(line):
            flag = False

            print("section end")

        elif flag:
            section_list.append(line)

            print(line)

    return section_list


def problem_no_91():
    """ pick up family section and save file

    :return: message string
    """

    with open("./questions-words.txt", mode="r", encoding="utf8") as file_read:
        analogy_list = pickup_search_section(file_read, "family")

    with open("./analogy_family.txt", mode="w", encoding="utf8") as file_write:
        file_write.writelines(analogy_list)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_91())
