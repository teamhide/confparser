from yaml import load, Loader


class ConfParserDict(dict):
    def __init__(self, config):
        super().__init__(config)
        if isinstance(config, dict):
            for k, v in config.items():
                if not isinstance(v, dict):
                    self[k] = v
                else:
                    self.__setattr__(k, ConfParserDict(v))

    def __getattr__(self, attr):
        return self.get(attr)

    def __setattr__(self, key, value):
        self.__setitem__(key, value)

    def __setitem__(self, key, value):
        super().__setitem__(key, value)
        self.__dict__.update({key: value})

    def __delattr__(self, item):
        self.__delitem__(item)

    def __delitem__(self, key):
        super().__delitem__(key)
        del self.__dict__[key]


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
        return ConfParserDict(config=self.config)
