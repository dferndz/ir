from ir.documents import Collection, HTMLDocument, FileDocument, TextDocument
from ir.pipelines import Pipeline, Stemmer, StopWordRemover, ToLower
from ir.vsr import InvertedIndex
from argparse import ArgumentParser


class Demo:
    def __init__(self, parser):
        self.prepare_parser(parser)
        args = parser.parse_args()
        self.args = args
        self.doc_class = HTMLDocument if args.html else FileDocument

        self.pipeline = Pipeline(ToLower())
        if args.stem:
            self.pipeline.add(Stemmer())
        self.pipeline.add(StopWordRemover())
        self.inverted_index = InvertedIndex(self.pipeline)

        self.collection = Collection(args.docsdir, wrapper_class=self.doc_class, pipeline=self.pipeline)

        self.index_collection()
        self.start()

    def index_collection(self):
        print(f"Indexing {len(self.collection)} files.")
        self.inverted_index.index_collection(self.collection)
        print(f"Indexed {len(self.collection)} files with {len(self.inverted_index.token_indexer)} unique terms")

    def start(self):
        raise NotImplementedError("Implement start() in derived classes!")

    def prepare_parser(self, parser):
        pass

    @classmethod
    def run(cls):
        parser = ArgumentParser()
        parser.add_argument('--docsdir', required=True, help="The file containing corpora")
        parser.add_argument('--stem', default=False, required=False, action='store_true', help="Use porter stemmer")
        parser.add_argument('--html', required=False, default=False, action='store_true', help="Parse html")

        cls(parser)
