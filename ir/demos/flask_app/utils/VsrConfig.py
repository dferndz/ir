from ir.vsr import InvertedIndex
from ir.documents import Collection
from ir.pipelines import Pipeline


def get_inverted_index(app) -> InvertedIndex:
    return app.config['inverted_index']


def get_collection(app) -> Collection:
    return app.config['collection']


def get_pipeline(app) -> Pipeline:
    return app.config['pipeline']
