# coding = utf-8
"""
create on : 2017/10/03
project name : NLP_100
file name : problem_no_40 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

preparation : 夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを
              使って係り受け解析し，その結果をneko.txt.cabochaという
              ファイルに保存せよ．
              このファイルを用いて，以下の問に対応するプログラムを実装せよ．

command : cabocha -f1 neko.txt > neko.txt.cabocha

problem : 形態素を表すクラスMorphを実装せよ．このクラスは表層形（surface），
          基本形（base），品詞（pos），品詞細分類1（pos1）を
          メンバ変数に持つこととする．
          さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
          各文をMorphオブジェクトのリストとして表現し，
          3文目の形態素列を表示せよ．

"""
import re


class Morph:
    """ store morphological analysis result from CaboCha """

    def __init__(self, morpheme):
        """ initialize and clean up morphological analysis result

        :param morpheme: morphological analysis result from CaboCha
        """

        if morpheme.strip("\n"):
            surface_feature = morpheme.split("\t")
            surface = surface_feature[0]
            feature_string = surface_feature[1]
            feature = feature_string.split(",")
        else:
            surface = None
            feature = [None] * 9

        self.surface = surface
        self.base = feature[6]
        self.pos = feature[0]
        self.pos1 = feature[1]


def problem_no_40():
    """ use CaboCha result made from neko.txt store analysis result

    :return: message
    """

    with open("./neko.txt.cabocha", mode="r", encoding="utf-8") as f:
        neko_cabocha = f.read().replace("\u3000", " ")

    neko_sentences = neko_cabocha.split("EOS\n")

    neko_morph = [[Morph(morph) for morph in sentence.strip("\n").split("\n")
                   if not re.match(r"^[*].*", morph)]
                  for sentence in neko_sentences]

    print("show morpheme result sentence no.3")

    morph_format = "{surface}\t{base},{pos},{pos1}"

    for morph in neko_morph[3]:
        print(morph_format.format(surface=morph.surface,
                                  base=morph.base,
                                  pos=morph.pos,
                                  pos1=morph.pos1))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_40())
