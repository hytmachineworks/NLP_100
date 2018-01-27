# coding = utf-8
"""
create on : 2018/01/14
project name : NLP_100
file name : problem_no_58 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）に基づき，
          「主語 述語 目的語」の組をタブ区切り形式で出力せよ．
          ただし，主語，述語，目的語の定義は以下を参考にせよ．

            述語: nsubj関係とdobj関係の子（dependant）を持つ単語
            主語: 述語からnsubj関係にある子（dependent）
            目的語: 述語からdobj関係にある子（dependent）
"""
import re

from problem_no_53 import get_nlp_soup


def get_dependent(dependence_soup, type_name):
    """ get all dependent of explicit type

    :param dependence_soup: sentence's dependence soup item
    :param type_name: dependence type name
    :return: dependence item tuple
    """

    def idx_string(dep_soup, tag):
        dep_tag = dep_soup.find(tag)

        if dep_tag:
            dep_idx = dep_tag.get("idx")
            dep_string = dep_tag.string

            dep_tuple = (dep_idx, dep_string)

            return dep_tuple

        else:
            return None

    dependence = dependence_soup.find_all("dep", attrs={"type": type_name})

    if dependence:
        dependence_list = [{"govennor": idx_string(dep, "governor"),
                            "dependent": idx_string(dep, "dependent")}
                           for dep in dependence]

        return dependence_list

    else:
        return []


def get_subject_predicate_object(soup_item):
    """ get subject predicate object from sentence

    :param soup_item: sentence of soup
    :return: subject predicate object list
    """

    def get_object(nsubj_list, dobj_list):
        """ find object

        :param nsubj_list: nsubj dependence items list
        :param dobj_list: dobj dependence item list
        :return: object items object item list
        """
        nsubj_items = [nsubj_dic["govennor"] for nsubj_dic in nsubj_list]
        dobj_items = [dobj_dic["govennor"] for dobj_dic in dobj_list]

        objct_items = list(set(nsubj_items) & set(dobj_items))

        return objct_items

    def get_subject_predicate(nsubj_list, dobj_list, obj_list):
        """ find subject predicate items

        :param nsubj_list: nsubj dependence items list
        :param dobj_list: dobj dependence items list
        :param obj_list: object item list
        :return: subject predicate item list
        """
        subject_predicate_object_list = []

        for obj in obj_list:
            subj_item = [subj["dependent"] for subj in nsubj_list
                         if subj["govennor"] == obj][0]

            pred_item = [dob["dependent"] for dob in dobj_list
                         if dob["govennor"] == obj][0]

            buff = [subj_item[1], pred_item[1], obj[1]]

            subject_predicate_object_list.append("\t".join(buff))

        return subject_predicate_object_list

    dependences = soup_item.find("dependencies",
                                 attrs={"type": "collapsed-dependencies"})

    nsubj = get_dependent(dependences, "nsubj")
    dobj = get_dependent(dependences, "dobj")

    object_list = []

    if nsubj and dobj:
        object_list = get_object(nsubj, dobj)

    if object_list:
        subj_pred_obj_list = get_subject_predicate(nsubj, dobj, object_list)

        return subj_pred_obj_list

    return None


def problem_no_58():
    """ get all subject predicate object list

    :return: subject predicate object list strings
    """
    soup = get_nlp_soup()

    id_re = re.compile(r"[0-9]*")

    sentence_soup_list = soup.find_all("sentence", attrs={"id": id_re})

    subj_pred_obj_list = []

    for sentence_soup in sentence_soup_list:
        subj_pred_obj = get_subject_predicate_object(sentence_soup)

        if subj_pred_obj:
            subj_pred_obj_list.extend(subj_pred_obj)

    return "\n".join(subj_pred_obj_list)


if __name__ == "__main__":
    print(problem_no_58())
