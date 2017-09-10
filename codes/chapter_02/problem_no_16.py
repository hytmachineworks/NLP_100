# coding = utf-8
"""
create on : 2017/08/22
project name : NLP_100
file name : problem_no_16 

This problem using hightemp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 自然数Nをコマンドライン引数などの手段で受け取り，
          入力のファイルを行単位でN分割せよ．
          同様の処理をsplitコマンドで実現せよ．

make sure by bash command
N=7
split --number=l/$N -d --additional-suffix=.txt hightemp.txt hightemp_cmd_
"""

import sys

HIGHTEMP_TEXT_PATH = "./hightemp.txt"


def problem_no_16():
    """ Visible rows get by command line argument.
        And output input rows to last row data.

    :return: message string
    """

    with open(HIGHTEMP_TEXT_PATH, mode="r", encoding="utf-8") as f:
        hightemp_all_list = f.readlines()

    # print(hightemp_all_list)

    args = sys.argv

    if len(args) == 1:
        return "Not found command line argument! Please input argument"

    try:
        split_no = int(args[1])

    except Exception as error_message:
        print(error_message)
        return "Invalid command line argument! Please retry correct numbers."

    hightemp_bytes = [len(hightemp.encode()) for hightemp in hightemp_all_list]
    hightemp_total_length = len("".join(hightemp_all_list).encode())

    hightemp_ave = sum(hightemp_bytes) / len(hightemp_all_list)

    hightemp_div_bytes = hightemp_total_length / split_no
    hightemp_div_lines = len(hightemp_all_list) // split_no

    hightemp_div_datas = []
    diviation_list = []

    yojo_lines = (len(hightemp_all_list) - hightemp_div_lines * split_no)
    lest_bytes = hightemp_ave * yojo_lines
    add_count = 0
    buff_byte = 0.0
    buff_line = ""
    counter = 0
    for line_no, hightemp_byte in enumerate(hightemp_bytes):

        if counter == hightemp_div_lines:
            before_value = buff_byte - float(hightemp_div_bytes)
            current_value = before_value + float(hightemp_byte)
            # print("before_value :", before_value)
            # print("current_value :", current_value)

            diff = current_value + before_value
            border = lest_bytes / split_no
            # print("before + current :", diff, "border_line :", border)

            if split_no - len(hightemp_div_datas) - 1 == 0:
                adj = 1.001
            else:
                adj = 1.0

            finished_lines = len(hightemp_all_list) - line_no
            unfinish_div = (split_no - len(hightemp_div_datas) - adj)

            current_div_row = finished_lines / unfinish_div
            # print("current_div_rows", current_div_row)

            next_div_row = (finished_lines - 1) / unfinish_div
            # print("next_div_rows", next_div_row)

            print("no_" + str(len(hightemp_div_datas)+1) + "_data" + "\n")

            if (float(hightemp_div_lines) < next_div_row and diff < border)\
                    or current_div_row - next_div_row == 1.0:

                buff_byte += float(hightemp_byte)
                buff_line += hightemp_all_list[line_no]
                counter += 1
                add_count += 1
                diviation_list.append(current_value)
                hightemp_div_datas.append(buff_line)

                print(buff_line + "\n")

                lest_bytes -= current_value

                buff_byte = 0.0
                buff_line = ""
                counter = 0

            else:
                hightemp_div_datas.append(buff_line)
                diviation_list.append(before_value)

                print(buff_line + "\n")

                lest_bytes -= before_value

                buff_byte = 0.0
                buff_line = ""
                counter = 0

                buff_byte += float(hightemp_byte)
                buff_line += hightemp_all_list[line_no]
                counter += 1
        else:

            buff_byte += float(hightemp_byte)
            buff_line += hightemp_all_list[line_no]
            counter += 1

    if buff_line:
        print("no_" + str(len(hightemp_div_datas)+1) + "_data" + "\n")
        hightemp_div_datas.append(buff_line)
        print(buff_line + "\n")

    for file_no, hightemp_div in enumerate(hightemp_div_datas):
        file_name = "./hightemp_py_" + str(file_no).zfill(2) + ".txt"
        with open(file_name, mode="w", encoding="utf-8") as f:
            f.write(hightemp_div)

    return "Output process complete"


if __name__ == "__main__":
    print(problem_no_16())
