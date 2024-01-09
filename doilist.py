import gzip
import json
import os
from typing import List

PARSED_DIRECTORY = 'parsed'


def getDoiList():
    doilist: List[str] = []
    for f in os.listdir(PARSED_DIRECTORY):
        if f.endswith(".json.gz"):
            print(f)
            fstream: List = json.loads(gzip.open(PARSED_DIRECTORY + "/" + f, 'r').read())
            for item in fstream:
                doilist.append(item['doi'].lower())
    return doilist


def doiListToFile():
    doilist = getDoiList()
    jf = json.dumps(doilist)
    open("doilist.json", "wb").write(jf.encode("utf-8"))


if __name__ == '__main__':
    doiListToFile()
