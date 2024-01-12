# Searches a certain query for pagerank
import json


class SearchResult:
    """
    Class that holds search results
    """
    def __init__(self, title: str, doi: str, pagerank: int = 0):
        self.title = title
        self.doi = doi
        self.pagerank = pagerank


def do_pagerank_search(filename, query):
    """
    Search with a query in the list of documents, order results using pagerank
    :param filename: Name of the JSON file
    :param query: the query to look for
    :return: list of items ordered by pagerank
    """
    f = open(filename)
    data = json.load(f)
    results = []

    for i in range(len(data)):
        title = data[i]['title']
        if query in title:
            search_res = SearchResult(title, data[i]["doi"], data[i]["pagerank"])
            results.append(search_res)

    # Sort results list (highest ranking first)
    results.sort(key=lambda x: x.pagerank, reverse=True)

    return results
