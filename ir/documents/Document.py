from ir.vectors import SparseVector
from ir.indexers import ObjectIndexer
from ir.pipelines import Pipeline


class Document:
    def __init__(self, pipeline=Pipeline.empty_pipeline()):
        self.pipeline = pipeline
        self.doc_vector = None

    def vector(self, *args, **kwargs):
        if self.doc_vector is None:
            self.doc_vector = self.get_vector(*args, **kwargs)
        return self.doc_vector

    def get_vector(self, indexer: ObjectIndexer = None, add_to_indexer=False):
        clean_tokens = self.process_tokens(self.tokens())

        if indexer is None:
            return SparseVector.counter(clean_tokens)
        else:
            return SparseVector.counter(
                indexer.add_objects(clean_tokens)
                if add_to_indexer
                else indexer.indexes_of(clean_tokens)
            )

    def set_vector(self, vector):
        self.doc_vector = vector

    def tokens(self):
        raise NotImplementedError("Implement tokens() in derived classes!")

    def process_tokens(self, tokens):
        for token in tokens:
            yield self.pipeline(token)
