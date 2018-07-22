# coding = utf-8
"""
create on : 2018/07/22
project name : NLP_100
file name : problem_no_69

This problem using artist.json.gz
This file is available at "http://www.cl.ecei.tohoku.ac.jp/nlp100/".
This file NOT include this repository.
If you need file, please get above web site.

problem : ユーザから入力された検索条件に合致するアーティストの情報を表示する
          Webアプリケーションを作成せよ．アーティスト名，アーティストの別名，
          タグ等で検索条件を指定し，
          アーティスト情報のリストをレーティングの高い順などで整列して表示せよ．
"""
import sys
from pathlib import Path

from flask import Flask, render_template, request, redirect, url_for

sys.path.append(str(Path().cwd().parents[0]))

from problem_no_68 import search_items
# True way add PYTHONPATH this way is cheat.
# not suitable for PEP 8


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    """ driven at accessing to index.html

    :return: rendering index.html
    """

    if request.method == "GET":
        title = "Artist DB"
        message = "Search Artist DB Data"

        return render_template("index.html",
                               title=title,
                               message=message)

    elif request.method == "POST":
        category = request.form["category"]
        keyword = request.form["keyword"]

        title = "Search result : " + category + " " + keyword
        message = "Search result : " + category + " " + keyword

        results = search_items(category, keyword)

        return render_template("index.html",
                               title=title,
                               message=message,
                               results=results,
                               not_found=True if not results else False)
    else:
        return redirect(url_for("index"))


if __name__ == "__main__":
    app.run()
