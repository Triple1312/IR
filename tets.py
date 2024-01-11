import json


def publishercount():
    eek = json.loads(open("doilist_ turing.json", "rb").read())
    print(len(eek))


publishercount()