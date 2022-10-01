from .Module import Module
from .EmptyModule import EmptyModule


class Pipeline:
    def __init__(self, *args: [Module]):
        self.modules = list(args)

    def __call__(self, x):
        temp = x
        for m in self.modules:
            temp = m(temp)
        return temp

    def add(self, m):
        self.modules.append(m)

    @staticmethod
    def empty_pipeline():
        return Pipeline(EmptyModule())
