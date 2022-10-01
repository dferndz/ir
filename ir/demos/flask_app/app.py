from flask import Flask, render_template, request, redirect, url_for
from .utils import get_retrievals, render_retrieval, get_collection


app = Flask(__name__)


@app.route("/")
def hello():
    collection = get_collection(app)
    return render_template("hello.html", collection_dir=collection.dir_path)


@app.route("/indexed/<file_name>")
def get_indexed_document(file_name):
    return render_retrieval(app, file_name)


@app.route("/search")
def search():
    query = request.args.get("q", None)

    if query is None or len(query) == 0:
        return redirect(url_for("hello"))

    retrievals = [
        {"doc": doc, "score": score} for doc, score in get_retrievals(app, query)
    ]

    return render_template(
        "search_results.html", retrievals=retrievals, len=len(retrievals)
    )
