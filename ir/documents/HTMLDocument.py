from .FileDocument import FileDocument
from ir.parsers import SimpleHTMLParser
from nltk.tokenize import word_tokenize
from ir.pipelines import Pipeline


class HTMLDocument(FileDocument):
    def __init__(self, file, pipeline=Pipeline.empty_pipeline()):
        super().__init__(file, pipeline)

    def tokens(self):
        data = ""
        for line in self.file:
            data += line

        for w in word_tokenize(SimpleHTMLParser.parse_html(data)):
            yield w
