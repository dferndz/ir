from ir.documents import Document, Collection
from ir.indexers import ObjectIndexer
from ir.pipelines import Pipeline
from tqdm.auto import tqdm
import numpy as np


class InvertedIndex:
    def __init__(self, pipeline=Pipeline.empty_pipeline()):
        self.token_to_docs = dict()
        self.token_to_idf = dict()
        self.doc_to_length = dict()
        self.token_indexer = ObjectIndexer()
        self.pipeline = pipeline
        self.indexed_docs = set()

    def __len__(self):
        return len(self.indexed_docs)

    def index_collection(self, collection: Collection):
        for doc in tqdm(collection):
            self.index_document(doc)
        self.compute_idf()

    def index_document(self, doc: Document):
        self.indexed_docs.add(doc)
        vector = doc.vector(self.token_indexer, add_to_indexer=True)
        for token_idx, count in vector.items():
            self.index_token(token_idx, count, doc)

    def index_token(self, token_idx, count, doc: Document):
        occurrence = (doc, count)

        if token_idx in self.token_to_docs:
            self.token_to_docs[token_idx].add(occurrence)
        else:
            self.token_to_docs[token_idx] = {occurrence}

    def retrieve(self, query: Document):
        retrievals = dict()
        vector = query.vector(self.token_indexer)
        query_length = 0

        for token_idx, count in vector.items():
            idf = self.token_to_idf[token_idx]
            w = idf * count
            query_length += np.power(w, 2)

            for doc, count_in_doc in self.token_to_docs[token_idx]:
                score = w * idf * count_in_doc
                if doc in retrievals:
                    retrievals[doc] += score
                else:
                    retrievals[doc] = score

        query_length = np.sqrt(query_length)

        for doc in retrievals:
            retrievals[doc] = retrievals[doc] / (query_length * self.doc_to_length[doc])

        return sorted(retrievals.items(), key=lambda x: x[1], reverse=True)

    def compute_idf(self):
        n = len(self)
        for token_idx, occurrences in self.token_to_docs.items():
            idf = np.log2(n / len(occurrences))
            self.token_to_idf[token_idx] = idf

            for occurrence in occurrences:
                doc, count = occurrence
                self.doc_to_length[doc] = (
                    self.doc_to_length[doc] + np.power(idf * count, 2)
                    if doc in self.doc_to_length
                    else np.power(idf * count, 2)
                )

        for doc in self.indexed_docs:
            self.doc_to_length[doc] = np.sqrt(self.doc_to_length[doc])
