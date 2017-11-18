# coding = utf-8
"""
create on : 2017/11/11
project name : NLP_100
file name : problem_no_44

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 与えられた文の係り受け木を有向グラフとして可視化せよ．
          可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
          また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""
import networkx as nx

from problem_no_41 import get_neko_chunk_list
from problem_no_42 import source_and_destination


def problem_no_44():
    """ show sentence chunking by digraph

    :return: message
    """

    target_sentence_no = 8

    neko_chunk_list = get_neko_chunk_list()

    neko_chunk = neko_chunk_list[target_sentence_no - 1]

    src_dst_list = source_and_destination(neko_chunk)

    all_edges = [(src_dst.split("\t")[0], src_dst.split("\t")[1])
                 for src_dst in src_dst_list]

    g = nx.DiGraph()
    g.add_edges_from(all_edges)

    a_graph = nx.nx_agraph.to_agraph(g)

    a_graph.node_attr.update(fontname="MS Gothic")
    a_graph.layout("dot")
    a_graph.draw("neko.png")

    return "program finished"


if __name__ == "__main__":
    print(problem_no_44())
