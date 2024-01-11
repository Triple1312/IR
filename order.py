import json
import operator


def orderPublisherCount():
    publishers = json.loads(open("publishers.json", "rb").read())
    eek = dict(sorted(publishers.items(), key=operator.itemgetter(1), reverse=True))
    open("publishers_ordered.json", "wb").write(json.dumps(eek).encode("utf-8"))


if __name__ == '__main__':
    orderPublisherCount()