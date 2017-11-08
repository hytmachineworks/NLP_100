# coding = utf-8
"""
create on : 2017/10/20
project name : NLP_100
file name : problem_no_41

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 40に加えて，文節を表すクラスChunkを実装せよ．
          このクラスは形態素（Morphオブジェクト）のリスト（morphs），
          係り先文節インデックス番号（dst），係り元文節インデックス番号の
          リスト（srcs）をメンバ変数に持つこととする．
          さらに，入力テキストのCaboChaの解析結果を読み込み，
          １文をChunkオブジェクトのリストとして表現し，
          8文目の文節の文字列と係り先を表示せよ．
          第5章の残りの問題では，ここで作ったプログラムを活用せよ．

"""
import re

from problem_no_40 import Morph


class Chunk:
    """ chunking sentence from cabocha result """

    def __init__(self, phrase, srcs):
        """ initialize class and store data

        :param phrase: phrase of sentence string
        :param srcs: source phrase index number int
        """
        phrase_unit = phrase.split("\n")

        dst = re.search(r"(?!\* \d+ )-?\d(?=D)", phrase_unit[0]).group()
        morph_list = [Morph(morph) for morph in phrase_unit[1:]]

        self.dst = int(dst)
        self.srcs = srcs
        self.morphs = morph_list


def sentence_phrase_to_chunk(sentence_list):
    """ sentence devide to phrase and store chunk class

    :param sentence_list: given sentence list
    :return: all sentence chunk list
    """

    chunk_pat = r"\* \d+ -?\d+D \d+/\d+.+?(?=\n\* \d+ -?\d+D \d+/\d+)"
    dst_pat = r"(?!\* \d+ )-?\d(?=D)"

    magic_string = "* 0 0D 0/0 \n"

    all_sentence_chunk = []

    for sentence in sentence_list:

        phrase_list = re.findall(chunk_pat, sentence + magic_string, re.DOTALL)
        dst_list = re.findall(dst_pat, sentence)

        dst_dic = {i_key: [i_dst for i_dst, dst in enumerate(dst_list)
                           if int(dst) == i_key]
                   for i_key in range(len(dst_list))}

        sentence_chunk = [Chunk(phrase, dst_dic[i])
                          for i, phrase in enumerate(phrase_list)]

        all_sentence_chunk.append(sentence_chunk)

    return all_sentence_chunk


def problem_no_41():
    """ use CaboCha result made from neko.txt store chunking result

    :return: message string
    """

    with open("./neko.txt.cabocha", mode="r", encoding="utf-8") as f:
        neko_cabocha = f.read().replace("\u3000", " ")

    neko_sentences = neko_cabocha.split("EOS\n")

    neko_chunk_list = sentence_phrase_to_chunk(neko_sentences)

    print("show morpheme result sentence no.8")

    chunk_format = "index:{index}\t\tphrase:{phrase}\t\tdestination:{dst}"

    for i, chunk in enumerate(neko_chunk_list[7]):
        phrase = " ".join([morph.surface for morph in chunk.morphs])
        print(chunk_format.format(index=i, phrase=phrase, dst=chunk.dst))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_41())
