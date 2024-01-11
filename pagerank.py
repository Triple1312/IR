


class PaperScore:
    def __init__(self, doi, title, score, references):
        self.doi: str = doi
        self.title: str = title
        self.score: int = score
        self.references = references

papers = []

paperscores = [PaperScore] = []

new_scores = []


for pap in papers:
    paperscores.append(PaperScore(pap["doi"], pap["title"], pap["referenced_by_count"], pap["references"]))

for it in range(0, 5):
    for paper in paperscores:
        new_scores.append(copy.deepcopy(paper))
    for paper in paperscores:
        for ref in paper.references:
            for paper2 in paperscores:
                if paper2.doi == ref:
                    paper2.score += paper.score
    paperscores = new_scores
    new_scores = []
