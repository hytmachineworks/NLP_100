# coding = utf-8
"""
create on : 2017/09/24
project name : NLP_100
file name : problem_no_30 

This problem using neko.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
          ただし，各形態素は表層形（surface），基本形（base），品詞（pos），
          品詞細分類1（pos1）をキーとするマッピング型に格納し，
          1文を形態素（マッピング型）のリストとして表現せよ．
          第4章の残りの問題では，ここで作ったプログラムを活用せよ．

"""
import glob
import json

from tqdm import tqdm
import MeCab

NEKO_TXT_MECAB_PATH = "./neko.txt.mecab"
SURFACE = "surface_form"
FEATURE_LIST = ["part_of_speech",  # 品詞
                "part_of_speech_subcategory1",  # 品詞細分類1
                "part_of_speech_subcategory2",  # 品詞細分類2
                "part_of_speech_subcategory3",  # 品詞細分類3
                "conjugation_form",  # 活用型
                "conjugation",  # 活用形
                "lexical_form",  # 原形
                "yomi",  # 読み
                "pronunciation"]  # 発音


def morphological_analysis_parse(surface, feature, nlp):
    """ parse morphological analysis result

    :param surface: surface form string
    :param feature: feature contents string
    :param nlp: nlp 100 or no boolean
    :return: morphological analysis result dictionary
    """

    if surface:
        morph_dic = {SURFACE: surface}
        feature_split = feature.split(",")

        for f_key, f_value in zip(FEATURE_LIST, feature_split):
            morph_dic[f_key] = f_value

    else:
        morph_dic = {}

    if nlp is True and morph_dic:
        nlp_morph_dic = {"surface": morph_dic["surface_form"],
                         "base": morph_dic["lexical_form"],
                         "pos": morph_dic["part_of_speech"],
                         "pos1": morph_dic["part_of_speech_subcategory1"]}

        return nlp_morph_dic

    return morph_dic


def morphological_analysis(tagger, sentence, nlp=False):
    """ morphological analysis given sentence

    :param tagger: MeCab tagger object
    :param sentence: given sentence string
    :param nlp: nlp 100 or no boolean
    :return: morphological analysis result list by sentence
    """

    morpheme = tagger.parseToNode(sentence)

    morpheme_result = []

    while morpheme:
        surface = morpheme.surface
        feature = morpheme.feature

        morpheme_dic = morphological_analysis_parse(surface, feature, nlp)

        if morpheme_dic:
            morpheme_result.append(morpheme_dic)

        morpheme = morpheme.next

    return morpheme_result


def morphological_analysis_main(text, nlp):
    """ morphological analysis given text

    :param text: given text List
    :param nlp: nlp 100 or no boolean
    :return: morphological analysis result list by text
    """

    tagger = MeCab.Tagger()

    neko_morph_list = []

    for t in tqdm(text):
        morph = morphological_analysis(tagger, t, nlp=nlp)
        neko_morph_list.append(morph)

    return neko_morph_list


def neko_morpheme():
    """ Morphological analysis data is given by neko.txt,
        and save json file

    :return: result message
    """

    neko_txt_mecab = glob.glob(NEKO_TXT_MECAB_PATH)

    if neko_txt_mecab:
        return "already exists morphological_analysis result"

    neko_path = "./neko.txt"
    with open(neko_path, mode="r", encoding="utf-8") as f:
        original_text = f.read()

    text_split = original_text.split("\n")

    text = [t.strip("　") for t in text_split if t]

    neko_morph_list = morphological_analysis_main(text, nlp=True)

    with open(NEKO_TXT_MECAB_PATH, mode="w", encoding="utf-8") as f:
        json.dump(neko_morph_list, f, ensure_ascii=False)

    return "morphological_analysis complete"


def get_neko_morpheme_list():
    """ load morphological analysis data

    :return: morphological analysis result list data
    """

    with open(NEKO_TXT_MECAB_PATH, mode="r", encoding="utf-8") as f:
        neko_morpheme_list = json.load(f)

    return neko_morpheme_list


def problem_no_30():
    """ morphological analysis text and store List and result dict data

    :return: morphological analysis result list data
    """
    print(neko_morpheme())
    morpheme_result = get_neko_morpheme_list()

    return morpheme_result


if __name__ == "__main__":
    print(problem_no_30())
