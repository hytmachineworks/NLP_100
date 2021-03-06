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

          make sure command written in problem_no_45.cmd

"""
from problem_no_41 import get_neko_chunk_list
from problem_no_42 import chunk_include_pos_detect


def get_argument_from_chunk(chunk_phrase):
    """ get argument from chunk phrase

    :param chunk_phrase:chunk phrase class chunk
    :return: argument string
    """

    phrase_list = [morph.surface for morph in chunk_phrase.morphs
                   if morph.pos != "記号"]

    argument_string = "".join(phrase_list)

    return argument_string


def predicate_analysis(chunk_sentence, arg_flag=False, mining=False):
    """ get predicate analysis from chunk sentence

    :param chunk_sentence: phrase class of chunk list
    :param arg_flag: include argument ore not boolean
    :param mining: mining data special case boolean
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
    mining_predicate_list = []

    for chunk in chunk_sentence:

        dst = chunk.dst

        predicate_flag = False

        if dst != -1 and not mining:
            src_flag = chunk_include_pos_detect(chunk, detect_pos="助詞")
            dst_flag = chunk_include_pos_detect(chunk_sentence[dst],
                                                detect_pos="動詞")
        elif dst != -1 and mining:
            predicate_flag = chunk_include_pos_detect(chunk,
                                                      detect_pos="助詞",
                                                      base="を")

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

        if predicate and case and not arg_flag and not mining:
            dict_value = (case, "")
            predicate_data_dict = predicate_data_to_dict(predicate_data_dict,
                                                         predicate, dict_value)

        elif predicate and case and arg_flag and not predicate_flag:
            argument = get_argument_from_chunk(chunk)
            dict_value = (case, argument)
            predicate_data_dict = predicate_data_to_dict(predicate_data_dict,
                                                         predicate, dict_value)

        elif predicate and case and mining and predicate_flag:
            argument = get_argument_from_chunk(chunk)
            mining_predicate = {"argument": argument,
                                "case": case,
                                "arg_pred": argument+predicate,
                                "predicate": predicate}
            mining_predicate_list.append(mining_predicate)

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

    if not mining:
        predicate_case = [predicate
                          + "\t"+dict_to_string(predicate)
                          for predicate in predicate_data_dict.keys()]

    elif mining and mining_predicate_list:
        predicate_list = list(predicate_data_dict.keys())

        predicate_case = [mining_dict["arg_pred"]
                          + "\t"+dict_to_string(mining_dict["predicate"])
                          for mining_dict in mining_predicate_list
                          if mining_dict["predicate"] in predicate_list]

    else:
        predicate_case = ""

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
