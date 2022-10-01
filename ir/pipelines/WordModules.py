from .Module import Module
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk import download


class Stemmer(Module):
    stemmer = PorterStemmer()

    def forward(self, w):
        return self.stemmer.stem(w)


class ToLower(Module):
    def forward(self, x):
        return str(x).lower()


class StopWordRemover(Module):
    def __init__(self):
        try:
            self.stops = set(stopwords.words("english"))
        except LookupError:
            download("stopwords")
            self.stops = set(stopwords.words("english"))

    def forward(self, x):
        return x if x not in self.stops else None
