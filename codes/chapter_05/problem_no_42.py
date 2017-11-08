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


def source_and_destination(chunk_sentence):
    """ get pair of source and destination phrase

    :param chunk_sentence: chunked sentence list
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

    for chunk in chunk_sentence:

        dst = chunk.dst

        if dst != -1:
            frm_phrase = chunk_to_phrase(chunk)
            dst_phrase = chunk_to_phrase(chunk_sentence[dst])

            output_format = "{frm}\t{dst}"

            print(output_format.format(frm=frm_phrase, dst=dst_phrase))


def problem_no_42():
    """ get all source and destination phrase pairs

    :return: message
    """
    neko_chunk_list = get_neko_chunk_list()

    for neko_chunk in neko_chunk_list:

        if neko_chunk:

            print("<-- split sentence")

            source_and_destination(neko_chunk)

            print("split sentence -->\n")

    return "program finished"


if __name__ == "__main__":
    print(problem_no_42())
