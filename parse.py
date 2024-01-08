import gzip
import json
import os
from typing import List

from paper import Paper, DOI
DOCUMENTS_LOCATION = "crossref"


def parse(filename):
    parsed_papers: List[Paper] = []
    papers = json.loads(gzip.open(filename, 'r').read())["items"]
    for pap in papers:
        if pap["is-referenced-by-count"] == 0:
            continue
        references = []  # [ref["DOI"] for ref in papi["reference"]]
        if "reference" in pap:
            for ref in pap["reference"]:
                if "DOI" in ref:
                    references.append(ref["DOI"])
        parsed_papers.append(Paper(pap["DOI"], pap["title"], pap["is-referenced-by-count"], references))
    return parsed_papers


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    for f in os.listdir(DOCUMENTS_LOCATION):
        print(f)
        papers = parse(DOCUMENTS_LOCATION + "/" + f)
        jpapers = [p.__dict__ for p in papers]
        w = json.dumps(jpapers)
        open("parsed/" + f + "_parsed.json.gz", "wb").write(gzip.compress(w.encode("utf-8")))

