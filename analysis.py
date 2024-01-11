import gzip
import json
import os
DOCUMENTS_LOCATION = "crossref"

def analyse():
    publishers: [dict] = {}
    published: [int] = [0, 0, 0, 0, 0] # o: <1980, 1980-1990, 1990-2000, 2000-2010, 2010-2020
    refernced_count: [int] = [0, 0, 0, 0, 0, 0, 0, 0] # 0: < 3, 3-5, 5-10, 10-20, 20-50, 50-100, 100-200, 200+

    for f in os.listdir(DOCUMENTS_LOCATION):
        print(f)
        papers = json.loads(gzip.open(DOCUMENTS_LOCATION + "/" + f, 'r').read())["items"]
        for pap in papers:
            if pap["is-referenced-by-count"] < 3:
                continue
            try:
                publisher = pap["publisher"]
                if publisher in publishers:
                    publishers[publisher] += 1
                else:
                    publishers[publisher] = 1
            except (KeyError, TypeError):
                pass
            try:
                publishedd: int = pap["published-print"]["date-parts"][0][0]
                if publishedd < 1980:
                    published[0] += 1
                elif publishedd < 1990:
                    published[1] += 1
                elif publishedd < 2000:
                    published[2] += 1
                elif publishedd < 2010:
                    published[3] += 1
                else:
                    published[4] += 1
            except (KeyError, TypeError):
                pass
            try:
                referenced_by_count = pap["is-referenced-by-count"]
                if referenced_by_count < 3:
                    refernced_count[0] += 1
                elif referenced_by_count < 5:
                    refernced_count[1] += 1
                elif referenced_by_count < 10:
                    refernced_count[2] += 1
                elif referenced_by_count < 20:
                    refernced_count[3] += 1
                elif referenced_by_count < 50:
                    refernced_count[4] += 1
                elif referenced_by_count < 100:
                    refernced_count[5] += 1
                elif referenced_by_count < 200:
                    refernced_count[6] += 1
                else:
                    refernced_count[7] += 1
            except (KeyError, TypeError):
                pass
    open("publishers.json", "wb").write(json.dumps(publishers).encode("utf-8"))
    open("published.json", "wb").write(json.dumps(
        {"<1980": published[0], "1980-1990": published[1], "1990-2000": published[2], "2000-2010": published[3], "2010-2021": published[4]}
    ).encode("utf-8"))
    open("referenced.json", "wb").write(json.dumps({
        "<3": refernced_count[0], "3-5": refernced_count[1], "5-10": refernced_count[2], "10-20": refernced_count[3],
        "20-50": refernced_count[4], "50-100": refernced_count[5], "100-200": refernced_count[6], "200+": refernced_count[7]
    }).encode("utf-8"))

if __name__ == '__main__':
    analyse()