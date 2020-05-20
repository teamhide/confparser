from collections import defaultdict

from yaml import load, FullLoader


class DotDict(defaultdict):
    def __init__(self, *args, **kwargs):
        if args or kwargs:
            dict.__init__(self, *args, **kwargs)

    def __getattr__(self, key):
        value = self.__getitem__(key)

        if isinstance(value, dict) and not isinstance(value, DotDict):
            value = DotDict(value)

        return value

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    def __delattr__(self, key):
        return self.__delitem__(key)


class ConfParserException(Exception):
    pass


class ConfParser:
    def __init__(self, path=None):
        self.config = None

        if path:
            self.load(path=path)

    def load(self, path: str) -> None:
        try:
            with open(path, 'r') as f:
                self.config = load(stream=f, Loader=FullLoader)
        except IOError:
            raise ConfParserException

    def to_obj(self) -> 'DotDict':
        return DotDict(config=self.config).config
