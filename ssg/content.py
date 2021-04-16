import re

from yaml import load, FullLoader

from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = __regex.split(string, 2)
        load(fm, Loader = FullLoader)
        return cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data = {'content': content}

    @property
    def body():
        return self.data['content']

    @property
    def type():
        return self.data['type'] if self.data['type'] is not None else return None

    @type.setter
    def type(self, value):
        self.data['type'] = value

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        return self.data.__iter__()

    def __len__(self):
        return self.data.__len__()

    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if not key == 'content':
                data[key] = value
        return str(data)
