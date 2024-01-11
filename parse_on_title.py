import os
import json
import gzip

DOCUMENTS_LOCATION = "crossref"

def parse_on_title():
    dois = []
    keywords = [" turing", " dfa", "state machine", "epilep"]
    for filename in os.listdir(DOCUMENTS_LOCATION):
        papers = json.loads(gzip.open(DOCUMENTS_LOCATION + "/" + filename, 'r').read())["items"]
        print(filename)
        for pap in papers:
            if pap["is-referenced-by-count"] < 3:
                continue
            title = pap["title"]
            if len(title) == 0:
                continue
            title = title[0].lower()
            for word in keywords:
                if word in title:
                    if "DOI" in pap:
                        dois.append(pap["DOI"])

    open("doilist_" + keywords[0] + ".json", "wb").write(json.dumps(dois).encode("utf-8"))


if __name__ == '__main__':
    parse_on_title()