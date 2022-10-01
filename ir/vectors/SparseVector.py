from collections import Counter
import numpy as np


class SparseVector:
    def __init__(self, data):
        if isinstance(data, dict):
            self.data = data.copy()
        else:
            self.data = self._data_from_iterable(data)

    @staticmethod
    def _data_from_iterable(data):
        return dict({i: item for i, item in enumerate(data) if item is not None})

    @staticmethod
    def counter(data):
        return SparseVector(dict(Counter(data)))

    def _operation_vector(self, v, func):
        res = SparseVector(self.data)
        for k, v in v.items():
            res[k] = func(res[k], v)
        return res

    def _operation_unary(self, c, func):
        res = SparseVector(self.data)
        for k in res:
            res[k] = func(res[k], c)
        return res

    def add(self, v):
        return self._operation_vector(v, lambda a, b: a + b)

    def __add__(self, other):
        return self.add(other)

    def subtract(self, v):
        return self._operation_vector(v, lambda a, b: a - b)

    def __sub__(self, other):
        return self.subtract(other)

    def top_idx(self, n=1, reverse=True):
        return sorted(self.data.keys(), key=lambda k: self[k], reverse=reverse)[:n]

    def multiply(self, c):
        return self._operation_unary(c, lambda a, b: a * b)

    def __mul__(self, other):
        return self.multiply(other)

    def __str__(self):
        return f"SparseVector({self.data})"

    def __repr__(self):
        return str(self)

    def __getitem__(self, item):
        if isinstance(item, list) or isinstance(item, set):
            return [self.data[k] for k in item]
        return self.data[item]

    def __setitem__(self, key, value):
        if isinstance(key, list) and isinstance(value, list):
            for k, v in zip(key, value):
                self.data[k] = v
        else:
            self.data[key] = value

    def __len__(self):
        return len(self.data)

    def items(self):
        return self.data.items()

    def __iter__(self):
        return iter(self.data)

    def vec_len(self):
        return np.sqrt(np.sum([np.power(v, 2) for _, v in self.items()]))
