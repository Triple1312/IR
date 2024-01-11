import os
import json
import gzip

file = "doilist_ turing.json"
doi_list: [str] = json.loads(open(file, "r").read())
extended_doi_list: [str] = []

for f in os.listdir("parsed_3"):
    o = json.loads(gzip.open("parsed_3/" + f, 'r').read())
    print(f)
    for item in o:
        if "doi" in item:
            if item["doi"] in doi_list:
                extended_doi_list += item["references"]

open("doilist_turing_extended.json", "wb").write(json.dumps(extended_doi_list).encode("utf-8"))