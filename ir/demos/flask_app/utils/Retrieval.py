from .VsrConfig import get_inverted_index, get_collection, get_pipeline
from ir.documents import TextDocument
import os


def get_retrievals(app, query):
    inverted_index = get_inverted_index(app)
    pipeline = get_pipeline(app)
    query_doc = TextDocument(query, pipeline=pipeline)
    return inverted_index.retrieve(query_doc)


def get_file_contents(path):
    f = open(path)
    content = ""

    for line in f:
        content += line

    return content


def render_retrieval(app, file_name):
    collection = get_collection(app)
    path = os.path.join(collection.dir_path, file_name)
    return get_file_contents(path)
