# coding = utf-8
"""
create on : 2018/01/08
project name : NLP_100
file name : problem_no_56.py 

This problem using nlp.txt
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : Stanford Core NLPの共参照解析の結果に基づき，
          文中の参照表現（mention）を代表参照表現（representative mention）に
          置換せよ．ただし，置換するときは，「代表参照表現（参照表現）」のように，
          元の参照表現が分かるように配慮せよ．
"""
from problem_no_50 import get_all_sentences
from problem_no_53 import get_nlp_soup


def replace_representative_mention(sentence_list, coreference_list):
    """ replace mention to representative mention from all sentences

    :param sentence_list: original sentence list
    :param coreference_list: coreference Beautiful soup list
    :return:
    """

    def replace_mention(sentence_origin_list, mention_soup_list):
        """ replace mention to representative mention

        :param sentence_origin_list: original sentence list
        :param mention_soup_list: a representation mention Beautiful soup list
        :return: replaced sentence list
        """

        sentence_replace_list = sentence_origin_list.copy()

        representative_mention = mention_soup_list[0].find("text").string

        for mention_soup in mention_soup_list[1:]:
            mention = mention_soup.find("text").string
            sentence_no = int(mention_soup.find("sentence").string)

            replace_str = representative_mention + "(" + mention + ")"
            replace_sentence = sentence_replace_list[sentence_no-1]

            buff = replace_sentence.replace(mention, replace_str)
            sentence_replace_list[sentence_no - 1] = buff

        return sentence_replace_list

    replace_sentence_list = sentence_list.copy()

    coreference_soup_list = [coreference.find_all("mention")
                             for coreference in coreference_list]

    for coreference_soup in coreference_soup_list:
        replace_sentence_list = replace_mention(replace_sentence_list,
                                                coreference_soup)

    return replace_sentence_list


def problem_no_56():
    """ get replace mention to representative mention

    :return: message
    """
    sentence_list = get_all_sentences(mode="list")

    soup = get_nlp_soup()

    coreference_list = soup.find("coreference").find_all("coreference")

    replaced_list = replace_representative_mention(sentence_list,
                                                   coreference_list)

    print("\n".join(replaced_list))

    return "program finished"


if __name__ == "__main__":
    print(problem_no_56())
