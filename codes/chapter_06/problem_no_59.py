# coding = utf-8
"""
create on : 2018/01/27
project name : NLP_100
file name : problem_no_59 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : Stanford Core NLPの句構造解析の結果（S式）を読み込み，
          文中のすべての名詞句（NP）を表示せよ．
          入れ子になっている名詞句もすべて表示すること．
"""
import re
import regex

from problem_no_53 import get_nlp_soup


def get_all_np_list(parse_tree):
    """ find all np string form parse structure tree

    :param parse_tree: parse structure tree
    :return: np string list
    """

    nested_re_str = r"(?<rec>\([-A-Z]+ (?:[^()]+|(?&rec))*\))"

    def get_noun_string(np_string):
        """ np item to np string

        :param np_string: np item
        :return: np string
        """

        pos_list = re.findall(r"\([^()]*?\)", np_string)

        surface_list = [str(pos.split(" ")[1])[:-1] for pos in pos_list]

        surface_string = " ".join(surface_list)

        for replace_from, replace_to in [("-LRB-", "("), ("-RRB-", ")")]:
            surface_string = surface_string.replace(replace_from, replace_to)

        return surface_string

    def get_all_np_items(np_string):
        """ parse np include items to np item

        :param np_string: include np parse structure tree string
        :return: np item string list
        """

        np_items_dict = {0: [np_string]}

        np_count = len(re.findall(r"\(NP", np_item))

        for i in range(np_count):

            np_re_target_list = np_items_dict[i]

            np_depth_item_list = []

            for np_re_target in np_re_target_list:

                np_re_string = np_re_target[3:]

                np_nested_list = regex.findall(nested_re_str, np_re_string)
                np_nested_list = [np_nested for np_nested in np_nested_list
                                  if "(NP" in np_nested]

                np_depth_item_list += np_nested_list

            if np_depth_item_list:
                np_items_dict[i+1] = np_depth_item_list

            else:
                break

        np_items_list = []

        for key_no in np_items_dict.keys():
            np_items_list += np_items_dict[key_no]

        all_np_items = [np_item_str for np_item_str in np_items_list
                        if np_item_str[:3] == "(NP"]

        return all_np_items

    parse_tree_string = parse_tree.string.replace("\n", "")

    nested_items = regex.findall(nested_re_str, parse_tree_string)

    only_np_include_items = [nested_item for nested_item in nested_items
                             if "(NP" in nested_item]

    all_np_item_str_list = []

    for np_item in only_np_include_items:

        np_item_str_list = [get_noun_string(np_item_string)
                            for np_item_string in get_all_np_items(np_item)]

        all_np_item_str_list += np_item_str_list

    return all_np_item_str_list


def problem_no_59():
    """ get all np items from parse tree

    :return: message
    """

    soup = get_nlp_soup()

    all_parse_tree = soup.find_all("parse")

    for parse_tree in all_parse_tree:

        print("\nprint parse structure tree")
        print(parse_tree.string)
        print("---\nprint np items")

        sentence_np = get_all_np_list(parse_tree)
        print("\n".join(sentence_np))

    return "program_finished"


if __name__ == "__main__":
    print(problem_no_59())
