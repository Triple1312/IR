import gzip
import json
import os
import threading
from multiprocessing import Pool

import numpy as np


PARSED_DIRECTORY = 'parsed'
MATRIX_DIRECTORY = 'matrix'

class AdjacencyMatrixElement:
    def __init__(self, defaultscore: int = 0):
        self.score: int = defaultscore
        self.referenceindeces: [int] = []

def openDoiList():
    file = open('doilist.json', 'r').read()
    print("Opened doilist.json")
    return json.loads(file)

def matrixListThread(personal_list: [AdjacencyMatrixElement], startindex: int, endindex: int, doilist: [str], parsedfiles: json):
    for i in range(startindex, endindex):
        pap = parsedfiles[i]
        element = AdjacencyMatrixElement(pap['referenced_by_count'])
        for ref in pap['references']:
            try:
                j = doilist.index(ref.lower())
                element.referenceindeces.append(j)
            except ValueError:
                print("Reference " + ref + " not found in doilist")
                pass
        personal_list.append(element)
    return personal_list


def makeIndexUpdateMatrixThreaded():
    doilist = openDoiList()
    indexmatrix: [AdjacencyMatrixElement] = []
    file_done_count = 0
    for file in os.listdir(PARSED_DIRECTORY):
        file_done_count += 1
        papers = json.loads(gzip.open(PARSED_DIRECTORY + "/" + file, 'r').read())
        pl1: [AdjacencyMatrixElement] = []
        th1 = threading.Thread(target=matrixListThread, args=(pl1, 0, len(papers)//10, doilist, papers))
        pl2: [AdjacencyMatrixElement] = []
        th2 = threading.Thread(target=matrixListThread, args=(pl2, len(papers)//10, 2 * len(papers)//10, doilist, papers))
        pl3: [AdjacencyMatrixElement] = []
        th3 = threading.Thread(target=matrixListThread, args=(pl3, 2*len(papers)//10, 3*len(papers)//10, doilist, papers))
        pl4: [AdjacencyMatrixElement] = []
        th4 = threading.Thread(target=matrixListThread, args=(pl4, 3*len(papers)//10, 4*len(papers)//10, doilist, papers))
        pl5: [AdjacencyMatrixElement] = []
        th5 = threading.Thread(target=matrixListThread, args=(pl5, 4*len(papers)//10, 5*len(papers)//10, doilist, papers))
        pl6: [AdjacencyMatrixElement] = []
        th6 = threading.Thread(target=matrixListThread, args=(pl6, 5*len(papers)//10, 6*len(papers)//10, doilist, papers))
        pl7: [AdjacencyMatrixElement] = []
        th7 = threading.Thread(target=matrixListThread, args=(pl7, 6*len(papers)//10, 7*len(papers)//10, doilist, papers))
        pl8: [AdjacencyMatrixElement] = []
        th8 = threading.Thread(target=matrixListThread, args=(pl8, 7*len(papers)//10, 8*len(papers)//10, doilist, papers))
        pl9: [AdjacencyMatrixElement] = []
        th9 = threading.Thread(target=matrixListThread, args=(pl9, 8*len(papers)//10, 9*len(papers)//10, doilist, papers))
        pl10: [AdjacencyMatrixElement] = []
        th10 = threading.Thread(target=matrixListThread, args=(pl10, 9*len(papers)//10, len(papers), doilist, papers))
        th1.start()
        th2.start()
        th3.start()
        th4.start()
        th5.start()
        th6.start()
        th7.start()
        th8.start()
        th9.start()
        th10.start()
        print("all threads started")
        th1.join()
        th2.join()
        th3.join()
        th4.join()
        th5.join()
        th6.join()
        th7.join()
        th8.join()
        th9.join()
        th10.join()
        print("all threads are done")
        indexmatrix.extend(pl1)
        indexmatrix.extend(pl2)
        indexmatrix.extend(pl3)
        indexmatrix.extend(pl4)
        indexmatrix.extend(pl5)
        indexmatrix.extend(pl6)
        indexmatrix.extend(pl7)
        indexmatrix.extend(pl8)
        indexmatrix.extend(pl9)
        indexmatrix.extend(pl10)
        if file_done_count % 5 == 0:
            matr = [p.__dict__ for p in indexmatrix]
            open(MATRIX_DIRECTORY + "/" + str(file_done_count) + "indexmatrix.json", "wb").write(json.dumps(matr).encode("utf-8"))
            print("Done with " + str(file_done_count) + " files and written matrix to " + str(file_done_count) + "indexmatrix.json")
        print("Done with " + file)
    return indexmatrix


def makeIndexUpdateMatrixPooled():
    doilist = openDoiList()
    indexmatrix: [AdjacencyMatrixElement] = []
    file_done_count = 0
    for file in os.listdir(PARSED_DIRECTORY):
        file_done_count += 1
        papers = json.loads(gzip.open(PARSED_DIRECTORY + "/" + file, 'r').read())
        p = Pool(10)
        pl = p.map(matrixListThread, [([], 0, len(papers)//10, doilist, papers),
                                        ([], len(papers)//10, 2 * len(papers)//10, doilist, papers),
                                        ([], 2*len(papers)//10, 3*len(papers)//10, doilist, papers),
                                        ([], 3*len(papers)//10, 4*len(papers)//10, doilist, papers),
                                        ([], 4*len(papers)//10, 5*len(papers)//10, doilist, papers),
                                        ([], 5*len(papers)//10, 6*len(papers)//10, doilist, papers),
                                        ([], 6*len(papers)//10, 7*len(papers)//10, doilist, papers),
                                        ([], 7*len(papers)//10, 8*len(papers)//10, doilist, papers),
                                        ([], 8*len(papers)//10, 9*len(papers)//10, doilist, papers),
                                        ([], 9*len(papers)//10, len(papers), doilist, papers)])
        pl.start()
        pl.join()
        print("all threads are done")
        indexmatrix.extend(pl[0])
        indexmatrix.extend(pl[1])
        indexmatrix.extend(pl[2])
        indexmatrix.extend(pl[3])
        indexmatrix.extend(pl[4])
        indexmatrix.extend(pl[5])
        indexmatrix.extend(pl[6])
        indexmatrix.extend(pl[7])
        indexmatrix.extend(pl[8])
        indexmatrix.extend(pl[9])
        if file_done_count % 5 == 0:
            matr = [p.__dict__ for p in indexmatrix]
            open(MATRIX_DIRECTORY + "/" + str(file_done_count) + "indexmatrix.json", "wb").write(json.dumps(matr).encode("utf-8"))
            print("Done with " + str(file_done_count) + " files and written matrix to " + str(file_done_count) + "indexmatrix.json")
        print("Done with " + file)
    return indexmatrix

def makeIndexUpdateMatrix():
    doilist = openDoiList()
    indexmatrix: [AdjacencyMatrixElement] = []
    file_done_count = 0
    for file in os.listdir(PARSED_DIRECTORY):
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
                    print("Reference " + ref + " not found in doilist")
                    pass
            indexmatrix.append(element)
        if file_done_count % 5 == 0:
            matr = [p.__dict__ for p in indexmatrix]
            open(MATRIX_DIRECTORY + "/" + str(file_done_count) + "indexmatrix.json", "wb").write(json.dumps(matr).encode("utf-8"))
            print("Done with " + str(file_done_count) + " files and written matrix to " + str(file_done_count) + "indexmatrix.json")
        print("Done with " + file)
    return indexmatrix

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
        if file_done_count % 5 == 0:
            open(MATRIX_DIRECTORY + "/" + str(file_done_count) + "matrix.json.gz", "wb").write(gzip.compress(json.dumps(matrix.tolist()).encode("utf-8")))
            print("Done with " + str(file_done_count) + " files and written matrix to " + str(file_done_count) + "matrix.json")
    return matrix


def getparsedfiles():
    return [f for f in os.listdir(PARSED_DIRECTORY) if f.endswith(".json.gz")]



if __name__ == '__main__':
    matrix = makeIndexUpdateMatrix()
