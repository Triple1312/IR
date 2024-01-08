import gzip
import json
import os

import numpy as np


PARSED_DIRECTORY = 'parsed'
MATRIX_DIRECTORY = 'matrix'


def openDoiList():
    file = open('doilist.json', 'r').read()
    return json.loads(file)


def makeIndexUpdateMatrix():
    doilist = openDoiList()
    indexmatrix = []
    file_done_count = 0


def makematrix():
    doilist = openDoiList()
    matrix = np.zeros((len(doilist), len(doilist)))
    file_done_count = 0
    for f in os.listdir(PARSED_DIRECTORY):
        file_done_count += 1
        papers = json.loads(gzip.open(PARSED_DIRECTORY + "/" + f, 'r').read())
        for pap in papers:
            i = doilist.index(pap['doi'])
            for ref in pap['references']:
                j = doilist.index(ref)
                matrix[j][i] = 1
        if file_done_count % 10 == 0:
            open(MATRIX_DIRECTORY + "/" + str(file_done_count) + "matrix.json.gz", "wb").write(gzip.compress(json.dumps(matrix.tolist()).encode("utf-8")))
            print("Done with " + str(file_done_count) + " files and written matrix to " + str(file_done_count) + "matrix.json")
    return matrix


def getparsedfiles():
    return [f for f in os.listdir(PARSED_DIRECTORY) if f.endswith(".json.gz")]



if __name__ == '__main__':
    matrix = makematrix()
