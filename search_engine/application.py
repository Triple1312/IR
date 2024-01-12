from flask import Flask, render_template
from do_pagerank_search import do_pagerank_search

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/search/<string:query>")
def search(query=None):
    search_results = do_pagerank_search(filename="data/test_data.json", query=query)
    print(search_results)
    return render_template("search_results.html", search_query=query, results=search_results)
