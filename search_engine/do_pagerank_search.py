# Searches a certain query for pagerank
import json
import gzip

class SearchResult:
    """
    Class that holds search results
    """
    def __init__(self, title: str, doi: str, pagerank: int = 0):
        self.title = title
        self.doi = doi
        self.pagerank = pagerank


def do_pagerank_search(filename, query, max_results):
    """
    Search with a query in the list of documents, order results using pagerank
    :param filename: Name of the JSON file
    :param query: the query to look for
    :param max_results: the maximum amount of results to show
    :return: list of items ordered by pagerank
    """
    if ".gz" in filename:
        data = json.load(gzip.open(filename, "rb"))
    else:
        data = json.load(open(filename))
    results = []

    query_words = query.lower().split()

    for paper in data:
        title = "_NO_TITLE_"
        if paper["title"]:
            title = paper['title'][0]  # title is in a list in the data
        title_words = title.lower().split()

        if all(word in title_words for word in query_words):
            search_res = SearchResult(title, paper["doi"], paper["score"])
            results.append(search_res)

    # Sort results list (highest ranking first)
    results.sort(key=lambda x: x.pagerank, reverse=True)

    return results[:max_results]
