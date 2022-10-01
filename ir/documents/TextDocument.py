from .Document import Document
from ir.pipelines import Pipeline
from nltk.tokenize import word_tokenize


class TextDocument(Document):
    def __init__(self, text: str, pipeline=Pipeline.empty_pipeline()):
        super().__init__(pipeline)
        self.text = text

    def tokens(self):
        for w in word_tokenize(self.text):
            yield w

    def __str__(self):
        return f"TextDocument(text={self.text})"

    def __repr__(self):
        return str(self)
