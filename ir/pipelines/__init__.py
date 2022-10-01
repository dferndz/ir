from .Pipeline import *
from .WordModules import *


import nltk

try:
    nltk.data.find("corpus/stopwords")
except LookupError:
    nltk.download("stopwords")
