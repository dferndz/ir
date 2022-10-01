import os
from ir.documents import FileDocument
from ir.pipelines import Pipeline


class Collection:
    def __init__(self, dir_path, wrapper_class=FileDocument, pipeline=Pipeline.empty_pipeline()):
        self.file_names = [os.path.join(dir_path, file_name) for file_name in os.listdir(dir_path)]
        self.pipeline = pipeline
        self.wrapper_class = wrapper_class
        self.dir_path = dir_path

    def __len__(self):
        return len(self.file_names)

    def files(self):
        for file_name in self.file_names:
            yield self.wrapper_class(open(file_name), self.pipeline)

    def __iter__(self):
        return self.files()
