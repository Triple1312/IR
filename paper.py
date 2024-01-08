
DOI = str

class Paper:
    def __init__(self, doi: DOI, title: str, referenced_by_count: int, references: [DOI]):
        self.doi: DOI = doi
        self.title: str = title
        self.referenced_by_count: int = referenced_by_count
        self.references: [DOI] = references
