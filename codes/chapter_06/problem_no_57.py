# coding = utf-8
"""
create on : 2018/01/08
project name : NLP_100
file name : problem_no_57

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : Stanford Core NLPの係り受け解析の結果（collapsed-dependencies）を
          有向グラフとして可視化せよ．
          可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
          また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""
import networkx as nx

from problem_no_50 import get_all_sentences
from problem_no_53 import get_nlp_soup


def draw_collapsed_dependencies(target):
    """ draw collapsed dependencies

    :param target: given sentence number
    :return: message
    """

    soup = get_nlp_soup()
    sentence_soup = soup.find("sentence", attrs={"id": str(target+1)})
    dependences = sentence_soup.find("dependencies",
                                     attrs={"type": "collapsed-dependencies"})

    dep_list = dependences.find_all("dep")

    all_edge = [(dep.find("governor").string, dep.find("dependent").string)
                for dep in dep_list
                if dep.find("governor").string != dep.find("dependent").string
                and dep.find("dependent").string not in ["!", "?", ",", "."]]

    g = nx.DiGraph()
    g.add_edges_from(all_edge)

    a_graph = nx.nx_agraph.to_agraph(g)

    a_graph.node_attr.update(fontname="MS Gothic")
    a_graph.layout("dot")
    a_graph.draw("dependence.png")

    return "draw collapsed-dependencies"


def problem_no_57():
    """ draw collapsed-dependencies by given sentence number

    :return: message
    """

    target = 0

    sentence_list = get_all_sentences(mode="list")

    print(sentence_list[target])
    print(draw_collapsed_dependencies(target))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_57())
