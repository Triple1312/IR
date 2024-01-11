import gzip
import json
import os

DOCUMENTS_LOCATION = "crossref"


paplist = []
first_file_name = ""
counter = 0
for f in os.listdir(DOCUMENTS_LOCATION):
    if counter == 0:
        first_file_name = f
    papers = json.loads(gzip.open(DOCUMENTS_LOCATION + "/" + f, 'r').read())["items"]
    paplist += papers
    if counter == 100:
        open("merged/" + first_file_name + "to" + f + "merged.json.gz", "wb").write(gzip.compress(json.dumps({"items": paplist}).encode("utf-8")))
        print(
            "Merged " + str(counter) + " files into " + "merged/" + first_file_name + "to" + f + "merged.json.gz")
        paplist = []
        counter = 0
    counter += 1
