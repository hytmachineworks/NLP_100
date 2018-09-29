# coding = utf-8
"""
create on : 2018/09/02
project name : NLP_100
file name : problem_no_70 

This problem using rt-polaritydata.tar.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 文に関する極性分析の正解データを用い，
          以下の要領で正解データ（sentiment.txt）を作成せよ．

            rt-polarity.posの各行の先頭に"+1 "という文字列を追加する
            （極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
            rt-polarity.negの各行の先頭に"-1 "という文字列を追加する
            （極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）

          上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
          sentiment.txtを作成したら，正例（肯定的な文）の数と
          負例（否定的な文）の数を確認せよ．
"""
import re
import random

from chardet.universaldetector import UniversalDetector

# These two files contains rt-polaritydata.tar.gz, NOT include this repository.
# If you need file, please get above web site(sea above docstrings).
POS_FILE_PATH = "./rt-polaritydata/rt-polarity.pos"
NEG_FILE_PATH = "./rt-polaritydata/rt-polarity.neg"


def file_encoding_detect(file_path):
    """ detect text file encoding

    :param file_path: file path string
    :return: encoding string
    """

    detector = UniversalDetector()

    with open(file_path, mode="rb") as f:
        read_data = f.readlines()

    for line_data in read_data:
        detector.feed(line_data)

        if detector.done:
            break

    detector.close()

    detect_result = detector.result

    if detect_result["encoding"]:
        detect_encoding = detect_result["encoding"]

    else:
        raise KeyError("Expected file is not text file!!!")

    return detect_encoding


def problem_no_70():
    """
    Read pos and neg file and make shuffled line file
    and verify before after counts.

    :return: message
    """

    print("read from each pos file and neg file")

    file_list = [POS_FILE_PATH, NEG_FILE_PATH]

    text_line_list = []
    original_dict = {}

    for file in file_list:

        file_encoding = file_encoding_detect(file)

        add_strings = '"+1"' if re.match(r".*pos$", file) else '"-1"'

        with open(file, mode="r", encoding=file_encoding) as f:
            read_data = f.readlines()

        original_dict[file[-3:]] = len(read_data)

        print(file[-3:], len(read_data))

        text_line_list += [add_strings + " " + line for line in read_data]

    shuffle_text_list = random.sample(text_line_list, len(text_line_list))

    # all line data write to new text file
    with open("./sentiment.txt", mode="w", encoding="utf-8") as f:
        f.writelines(shuffle_text_list)

    # read lines from make file
    with open("./sentiment.txt", mode="r", encoding="utf-8") as f:
        read_from_file_line_list = f.readlines()

    # pos and neg line counts from shuffled list
    print("Count up pos lines and neg lines")
    pos_line = 0
    neg_line = 0

    for text_line in read_from_file_line_list:
        if re.match(r'^"\+1".*$', text_line):
            pos_line += 1

        else:
            neg_line += 1

    output_str = "total:{total}\npos:{pos}\nneg:{neg}"
    print(output_str.format(total=str(pos_line+neg_line),
                            pos=str(pos_line),
                            neg=str(neg_line)))

    # verify pos and neg line counts between original and shuffled one
    if original_dict["pos"] == pos_line and original_dict["neg"] == neg_line:
        print("verify count succeed!!!")

    else:
        raise ValueError("verify count failure!!!")

    return "program finished"


if __name__ == "__main__":
    print(problem_no_70())
