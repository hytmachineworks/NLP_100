# coding = utf-8
"""
create on : 2017/11/18
project name : NLP_100
file name : problem_no_45

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 今回用いている文章をコーパスと見なし，
          日本語の述語が取りうる格を調査したい．
          動詞を述語，動詞に係っている文節の助詞を格と考え，
          述語と格をタブ区切り形式で出力せよ．

          makesure command written in problem_no_45.cmd

"""
from problem_no_41 import get_neko_chunk_list
from problem_no_42 import chunk_include_pos_detect


def get_predicate_and_case(chunk_sentence):
    """ get predicate and case from chunk sentence

    :param chunk_sentence: phrase class of chunk list
    :return: predicate and case string
    """

    def get_predicate_or_case(chunk_phrase, mode):
        """ get morpheme base form form chunk phrase

        :param chunk_phrase: phrase class of chunk
        :param mode: predicate or case string
        :return: morpheme base form string
        """

        target_pos = "動詞" if mode == "predicate" else "助詞"

        phrase_list = [morph.base for morph in chunk_phrase.morphs
                       if morph.pos == target_pos]

        target_index = 0 if mode == "predicate" else -1

        get_item_base = phrase_list[target_index]

        return get_item_base

    def predicate_case_to_dict(all_dict, predicate_value, case_value):
        """ update predicate and case dictionary

        :param all_dict: current dictionary dict
        :param predicate_value: predicate base form string
        :param case_value: case base form string
        :return: updated dictionary dict
        """

        dict_keys = all_dict.keys()

        if predicate_value not in dict_keys:
            all_dict[predicate_value] = [case_value]

        else:
            value_list = all_dict[predicate_value]
            all_dict[predicate_value] = sorted([case_value] + value_list)

        return all_dict

    predicate_case_dict = {}

    for chunk in chunk_sentence:

        dst = chunk.dst

        if dst != -1:
            src_flag = chunk_include_pos_detect(chunk, detect_pos="助詞")
            dst_flag = chunk_include_pos_detect(chunk_sentence[dst],
                                                detect_pos="動詞")
        else:
            src_flag = False
            dst_flag = False

        if src_flag and dst_flag:
            case = get_predicate_or_case(chunk, "case")
            predicate = get_predicate_or_case(chunk_sentence[dst], "predicate")

        else:
            case = ""
            predicate = ""

        if predicate and case:
            predicate_case_dict = predicate_case_to_dict(predicate_case_dict,
                                                         predicate, case)

    predicate_case = [predicate+"\t"+" ".join(predicate_case_dict[predicate])
                      for predicate in predicate_case_dict.keys()]

    predicate_case_string = "\n".join(predicate_case)

    return predicate_case_string


def problem_no_45():
    """ get all predicate and case list

    :return: message
    """

    neko_chunk_list = get_neko_chunk_list()

    predicate_case_list = [get_predicate_and_case(neko_chunk)
                           for neko_chunk in neko_chunk_list
                           if get_predicate_and_case(neko_chunk)]

    with open("./neko_predicate_case.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(predicate_case_list))

    print(predicate_case_list)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_45())
