import gzip
import json
import os

filename = "doilist_ turing.json"

search_papers: [str] = json.dumps(open(filename, "r").read())
new_papers: [str] = []


for f in os.listdir("parsed_3"):
    if f.endswith(".json.gz"):
        print(f)
        fstream = json.loads(gzip.open("parsed/" + f, 'r').read())
        for item in fstream:
            for ref in item["references"]:
                if ref in search_papers:
                    new_papers.append(item["doi"])
                    break
open(filename+ "2.json", "wb").write(json.dumps(new_papers).encode("utf-8"))