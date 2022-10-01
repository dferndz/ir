from .Document import *
from .FileDocument import *
from .HTMLDocument import *
from .Collection import *
from .TextDocument import *


import nltk

try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")
