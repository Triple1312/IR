import gzip
import json
import os
import threading

import numpy as np

from adj import makeIndexUpdateMatrix, AdjacencyMatrixElement

PARSED_DIRECTORY = 'parsed'
MATRIX_DIRECTORY = 'matrix'



def openDoiList():
    file = open('doilist.json', 'r').read()
    print("Opened doilist.json")
    return json.loads(file)

def makeIndexUpdateMatrixMul(start):
    doilist = openDoiList()
    indexmatrix: [AdjacencyMatrixElement] = []
    file_done_count = 0
    files = os.listdir(PARSED_DIRECTORY)
    for i in range(start, start + 5):
        file = files[i]
        file_done_count += 1
        papers = json.loads(gzip.open(PARSED_DIRECTORY + "/" + file, 'r').read())
        for pap in papers:
            element = AdjacencyMatrixElement(pap['referenced_by_count'])
            # todo if order is different from doilist, gives wrong result
            for ref in pap['references']:
                try:
                    j = doilist.index(ref.lower())
                    element.referenceindeces.append(j)
                except ValueError:
                    print("Reference " + ref + " not found in doilist for file " + file)
                    pass
            indexmatrix.append(element)
        if file_done_count % 5 == 0:
            matr = [p.__dict__ for p in indexmatrix]
            open(MATRIX_DIRECTORY + "/" + str(file_done_count) + "indexmatrix.json", "wb").write(json.dumps(matr).encode("utf-8"))
            print("Done with " + str(start) + " to " + str(start + file_done_count) + " files and written matrix to " + str(file_done_count) + "indexmatrix.json")
            return indexmatrix
        print("Done with " + file)
    return indexmatrix

if __name__ == '__main__':
    start = 0
    th1 = threading.Thread(target=makeIndexUpdateMatrixMul, args=(start,))
    th2 = threading.Thread(target=makeIndexUpdateMatrixMul, args=(start + 5,))
    th3 = threading.Thread(target=makeIndexUpdateMatrixMul, args=(start + 10,))
    th4 = threading.Thread(target=makeIndexUpdateMatrixMul, args=(start + 15,))
    th5 = threading.Thread(target=makeIndexUpdateMatrixMul, args=(start + 20,))

    th1.start()
    th2.start()
    th3.start()
    th4.start()
    th5.start()

    th1.join()
    th2.join()
    th3.join()
    th4.join()
    th5.join()

    print("all threads are done")
