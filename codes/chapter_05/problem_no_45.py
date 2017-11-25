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


def predicate_analysis(chunk_sentence, arg_flag=False):
    """ get predicate analysis from chunk sentence

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

    def get_argument(chunk_phrase):
        """ get argument from chunk phrase

        :param chunk_phrase:chunk phrase class chunk
        :return: argument string
        """

        phrase_list = [morph.surface for morph in chunk_phrase.morphs
                       if morph.pos != "記号"]

        argument_string = "".join(phrase_list)

        return argument_string

    def predicate_data_to_dict(all_dict, predicate_value, data_value):
        """ update predicate analysis data dictionary

        :param all_dict: current dictionary dict
        :param predicate_value: predicate base form string
        :param data_value: data form string
        :return: updated dictionary dict
        """

        dict_keys = all_dict.keys()

        if predicate_value not in dict_keys:
            all_dict[predicate_value] = [data_value]

        else:
            value_list = all_dict[predicate_value]
            new_list = sorted([data_value] + value_list, key=lambda x: x[0])
            all_dict[predicate_value] = new_list

        return all_dict

    predicate_data_dict = {}

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

        if predicate and case and not arg_flag:
            dict_value = (case, "")
            predicate_data_dict = predicate_data_to_dict(predicate_data_dict,
                                                         predicate, dict_value)

        elif predicate and case and arg_flag:
            argument = get_argument(chunk)
            dict_value = (case, argument)
            predicate_data_dict = predicate_data_to_dict(predicate_data_dict,
                                                         predicate, dict_value)

    def dict_to_string(dict_key):
        """ get a case and argument string

        :param dict_key: key string
        :return: case and argument string
        """

        if not dict_key:
            return []

        data_value = predicate_data_dict[dict_key]

        case_list = [data[0] for data in data_value]
        arg_list = [data[1] for data in data_value]

        return_string = " ".join(case_list)

        if arg_flag:
            return_string += "\t" + " ".join(arg_list)
            return return_string

        return return_string

    predicate_case = [predicate+"\t"+dict_to_string(predicate)
                      for predicate in predicate_data_dict.keys()]

    predicate_case_string = "\n".join(predicate_case)

    return predicate_case_string


def problem_no_45():
    """ get all predicate and case list

    :return: message
    """

    neko_chunk_list = get_neko_chunk_list()

    predicate_case_list = [predicate_analysis(neko_chunk)
                           for neko_chunk in neko_chunk_list
                           if predicate_analysis(neko_chunk)]

    with open("./neko_predicate_case.txt", mode="w", encoding="utf-8") as f:
        f.write("\n".join(predicate_case_list))

    print(predicate_case_list)

    return "program finished"


if __name__ == "__main__":
    print(problem_no_45())
