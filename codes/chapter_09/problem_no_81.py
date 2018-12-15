# coding = utf-8
"""
create on : 2018/11/18
project name : NLP_100
file name : problem_no_81 

This problem using enwiki-20150112-400-r10-105752.txt.bz2
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : 英語では，複数の語の連接が意味を成すことがある．
          例えば，アメリカ合衆国は"United States"，イギリスは"United Kingdom"と
          表現されるが，"United"や"States"，"Kingdom"という単語だけでは，
          指し示している概念・実体が曖昧である．
          そこで，コーパス中に含まれる複合語を認識し，複合語を1語として扱うことで，
          複合語の意味を推定したい．
          しかしながら，複合語を正確に認定するのは大変むずかしいので，
          ここでは複合語からなる国名を認定したい．

          インターネット上から国名リストを各自で入手し，80のコーパス中に出現する
          複合語の国名に関して，スペースをアンダーバーに置換せよ．
          例えば，"United States"は"United_States"，
          "Isle of Man"は"Isle_of_Man"になるはずである．

"""
import json
import os
import re

import certifi
import urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm


def get_html_data(url):
    """ get html from given url

    :param url: target site url string
    :return: html string
    """

    http = urllib3.PoolManager(cert_reqs="CERT_REQUIRED",
                               ca_certs=certifi.where())
    r = http.request("GET", url)

    if r.status != 200:
        raise IOError("http request failure")

    data = r.data.decode()

    return data


def country_dict_from_wikipedia():
    """ get country dict from wikipedia

    :return: country name dict
    """

    def rename_to_true_name(wiki_string):
        """ wikipedia notation to true name

        :param wiki_string: wikipedia notation country name
        :return: ture country name
        """

        if "," in wiki_string:
            print("find ,")

        split_data = wiki_string.split(",")

        true_data = " ".join(split_data[::-1]).strip()

        return true_data

    url = "https://en.wikipedia.org/wiki/List_of_sovereign_states"
    data = get_html_data(url)

    soup = BeautifulSoup(data, "html5lib")

    table = soup.find("table", attrs={"class": "sortable wikitable"})

    row_list = table.find_all("tr")

    aliases = {}
    country = {}

    for row in row_list:
        print("------------------")
        col = row.find("td")

        if not col:
            print("none item!!!")
            continue

        elif col["style"] == "text-align:center;":
            print("skipped !!!")
            continue

        display_none = row.find("span",
                                attrs={"style": "display:none"})
        if display_none:
            display_none.extract()

        sup_ref = row.find("sup", attrs={"class": "reference"})

        if sup_ref:
            sup_ref.extract()

        row_data = col.text.strip()

        print(row_data)

        if " → " in row_data:
            alias_key = row_data.split(" → ")
            alias = rename_to_true_name(alias_key[0].strip())
            key = rename_to_true_name(alias_key[1].strip())

            print("alias", alias)
            print("key", key)

            aliases[alias] = key

        elif " – " in row_data:
            key_value = row_data.split(" – ")
            key = rename_to_true_name(key_value[0].strip())
            value = rename_to_true_name(key_value[1].strip())

            print("key", key)
            print("value", value)

            country[key] = value

        else:
            true_name = rename_to_true_name(row_data)
            print("key", true_name)
            print("value", true_name)

            country[true_name] = true_name

    # apply alias names
    for alias_key in aliases.keys():

        if alias_key in country.keys():
            continue

        country_key = aliases[alias_key]

        country[alias_key] = country[country_key]

    # fill full name
    country_values = list(country.values())

    for country_value in country_values:
        if country_value not in country.keys():
            country[country_value] = country_value

    return country


def dependent_territory_dict():
    """ get dependent territory dict from wikipedia

    :return: dependent territory name dict
    """

    url = "https://en.wikipedia.org/wiki/Dependent_territory"
    data = get_html_data(url)

    soup = BeautifulSoup(data, "html5lib")

    tables = soup.find_all("table",
                           attrs={"class": "wikitable sortable"})

    dependent = {}

    for table in tables:
        print("\ntable ----------")

        rows = table.find_all("tr")

        for row in rows:

            if row.find("td"):
                dependent_text = row.find("td").text.strip()
                result = re.sub(r"\[[0-9]*?\]", "", dependent_text)

            else:
                continue

            if result not in dependent.keys():
                dependent[result] = result
                print(result)

            else:
                print("already exist", result)

    return dependent


def get_country_dict(json_path="./country.json", from_json=True):
    """ get country and dependent territory dict from wikipedia

    :param json_path: save json file path string
    :param from_json: load from json
    :return: country name and dependent territory name dict
    """

    # load from json but not exist json file make a new file
    if os.path.exists(json_path) and from_json:
        with open(json_path, mode="r", encoding="utf-8") as json_load:
            all_country_dict = json.load(json_load)

        return all_country_dict

    # get country data
    country_dict = country_dict_from_wikipedia()

    # get dependent territory data
    dependent_dict = dependent_territory_dict()

    all_country_dict = {}

    all_country_dict.update(dependent_dict)
    all_country_dict.update(country_dict)

    # save dictionary to json file
    with open(json_path, mode="w", encoding="utf-8") as json_dump:
        json.dump(all_country_dict, json_dump)

    return all_country_dict


def get_country_list(compund=True):
    """ get country name data list

    :param compund: compound word only boolean
    :return: country name list
    """

    country_dict = get_country_dict()
    country_keys = list(country_dict.keys())

    char_list = [")", "(", ",", "."]

    strip_char_list = []

    for country in country_keys:

        mod_country = country

        for char in char_list:
            mod_country = mod_country.replace(char, "")

        strip_char_list.append(mod_country)

    if not compund:
        return strip_char_list

    compound_list = [match for match in strip_char_list if " " in match]

    return compound_list


def problem_no_81():
    """ replace country full name words to concatenate with _

    :return: message string
    """

    country_list = get_country_list()

    with open("./en_wiki_corpus.txt", mode="r", encoding="utf-8") as f:
        corpus_org = f.readlines()

    corpus_data = []

    for corpus in tqdm(corpus_org):

        corpus_mod = corpus.replace("\n", "")

        match_list = [country for country in country_list
                      if country in corpus_mod]

        if match_list:  # find a country
            sort_match_list = sorted(match_list, key=lambda x: len(x))

            for match in sort_match_list[::-1]:
                country_words = match.replace(" ", "_")

                corpus_mod = corpus_mod.replace(match, country_words)

        reduce_corpus = [token for token in corpus_mod.split(" ")
                         if len(token) >= 3 and (token.isalpha()
                                                 or token.isnumeric())]

        corpus_data.append(" ".join(reduce_corpus) + "\n")

    with open("./en_wiki_corpus_mod.txt", mode="w", encoding="utf-8") as f:
        f.writelines(corpus_data)

    return "program_finished"


if __name__ == "__main__":
    print(problem_no_81())
