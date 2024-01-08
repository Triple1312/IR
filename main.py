# This is a sample Python script.
import gzip
import os

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import parse
import json
import paper


DOCUMENTS_LOCATION = "crossref"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    f = open("doilist.json", "r")
    jf = json.loads(f.read())
    print("idk")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
