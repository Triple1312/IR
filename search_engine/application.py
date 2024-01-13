from flask import Flask, render_template
from do_pagerank_search import do_pagerank_search

app = Flask(__name__)

# path to JSON paper data (list with title,doi,score)
paper_data_filepath = "data/test_data.json"

# max results per page
results_per_page = 20


@app.route("/")
def home():
    return render_template("homepage.html")


@app.route("/search/<string:query>")
def search(query=None):
    search_results = do_pagerank_search(filename=paper_data_filepath, query=query, max_results=results_per_page)
    return render_template("search_results.html", search_query=query, results=search_results)
