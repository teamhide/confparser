from collections import defaultdict

from yaml import load, Loader


class ConfParserDict(defaultdict):
    def __init__(self, *args, **kwargs):
        if args or kwargs:
            dict.__init__(self, *args, **kwargs)

    def __getattr__(self, key):
        value = self.__getitem__(key)

        if isinstance(value, dict) and not isinstance(value, ConfParserDict):
            value = ConfParserDict(value)

        return value

    def __setattr__(self, key, value):
        return self.__setitem__(key, value)

    def __delattr__(self, key):
        return self.__delitem__(key)


class ConfParserException(Exception):
    def __init__(self, msg: str):
        super().__init__(msg)


class ConfParser:
    def __init__(self, path: str = None, conf_dict: dict = None):
        self.config = None

        if not path and not conf_dict:
            raise ConfParserException(
                msg='Either path or conf_dict must be present',
            )
        elif path and conf_dict:
            raise ConfParserException(
                msg='path and conf_dict cannot coexist',
            )

        if path:
            self.load_from_path(path=path)
        elif conf_dict:
            if not isinstance(conf_dict, dict):
                raise ConfParserException(msg='type of conf_dict must be dict')

            self.config = conf_dict

    def load_from_path(self, path: str) -> None:
        try:
            with open(path, 'r') as f:
                self.config = load(stream=f, Loader=Loader)
        except IOError:
            raise ConfParserException(msg='Read file error')

    def to_obj(self) -> ConfParserDict:
        return ConfParserDict(config=self.config).config
