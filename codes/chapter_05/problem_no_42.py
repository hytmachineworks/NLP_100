# coding = utf-8
"""
create on : 2017/11/08
project name : NLP_100
file name : problem_no_42 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 係り元の文節と係り先の文節のテキストを
          タブ区切り形式ですべて抽出せよ．
          ただし，句読点などの記号は出力しないようにせよ．
"""
from problem_no_41 import get_neko_chunk_list


def chunk_include_pos_detect(chunk_phrase, detect_pos):
    """ check phrase include specify pos

    :param chunk_phrase: search phrase include pos class chunk
    :param detect_pos: specify pos string
    :return: detect result boolean
    """

    phrase_pos_list = [morph.pos for morph in chunk_phrase.morphs
                       if morph.pos == detect_pos]

    detect_result = True if phrase_pos_list else False

    return detect_result


def source_and_destination(chunk_sentence, dst_pos_include=""):
    """ get pair of source and destination phrase

    :param chunk_sentence: chunked sentence list
    :param dst_pos_include: destination phrase include assign pos
    :return: None
    """

    def chunk_to_phrase(chunk_phrase):
        """ chunked phrase convert to phrase sting

        :param chunk_phrase: convert chunk phrase
        :return: phrase sting
        """
        phrase_list = [morph.surface for morph in chunk_phrase.morphs
                       if morph.pos != "記号"]

        phrase_string = "".join(phrase_list)
        return phrase_string

    src_dst_list = []
    output_format = "{frm}\t{dst}"

    for chunk in chunk_sentence:

        dst = chunk.dst

        if dst != -1 and dst_pos_include:
            skip_or_not = chunk_include_pos_detect(chunk_sentence[dst],
                                                   dst_pos_include)

        elif dst != -1 and not dst_pos_include:
            skip_or_not = True

        else:
            skip_or_not = False

        if skip_or_not:
            frm_phrase = chunk_to_phrase(chunk)
            dst_phrase = chunk_to_phrase(chunk_sentence[dst])

        else:
            frm_phrase = ""
            dst_phrase = ""

        if frm_phrase and dst_phrase:
            output_buf = output_format.format(frm=frm_phrase, dst=dst_phrase)
            src_dst_list.append(output_buf)

    return src_dst_list


def problem_no_42():
    """ get all source and destination phrase pairs

    :return: message
    """
    neko_chunk_list = get_neko_chunk_list()

    for neko_chunk in neko_chunk_list:

        src_dst_list = source_and_destination(neko_chunk)

        if src_dst_list:

            print("<-- split sentence")

            output_string = "\n".join(src_dst_list)
            # print_string = output_string.replace("\t", " => ")
            print(output_string)

            print("split sentence -->\n")

    return "program finished"


if __name__ == "__main__":
    print(problem_no_42())
