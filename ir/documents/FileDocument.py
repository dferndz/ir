from .Document import Document
from ir.pipelines import Pipeline
from nltk.tokenize import word_tokenize
import os


class FileDocument(Document):
    def __init__(self, file, pipeline=Pipeline.empty_pipeline()):
        super().__init__(pipeline)
        self.file = file
        self.file_name = os.path.basename(file.name)

    def tokens(self):
        for line in self.file:
            for w in word_tokenize(line):
                yield w

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"HTMLDocument(file_name='{self.file_name}')"
