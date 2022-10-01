class ObjectIndexer:
    def __init__(self):
        self.objects_to_idx = dict()
        self.idx_to_object = dict()

    def __len__(self):
        return len(self.objects_to_idx)

    def __iter__(self):
        return iter(self.idx_to_object)

    def add_object(self, obj):
        if obj in self.objects_to_idx:
            return self.objects_to_idx[obj]

        next_idx = len(self)
        self.objects_to_idx[obj] = next_idx
        self.idx_to_object[next_idx] = obj
        return next_idx

    def add_objects(self, objs):
        return [self.add_object(obj) for obj in objs]

    def get_object(self, idx):
        return self.idx_to_object[idx] if idx in self.idx_to_object else None

    def get_objects(self, idxs):
        return [self.get_object(idx) for idx in idxs if idx in self.idx_to_object]

    def indexes_of(self, objs):
        return [self.index_of(obj) for obj in objs if obj in self.objects_to_idx]

    def index_of(self, obj):
        return self.objects_to_idx[obj] if obj in self.objects_to_idx else -1
