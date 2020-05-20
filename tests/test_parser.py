import pytest

from confparser import ConfParser
from confparser.parser import ConfParserException, DotDict


def test_parser_with_do_not_exist_path():
    with pytest.raises(ConfParserException):
        ConfParser(path='unknown')


def test_parser_with_none_path_and_none_conf_dict():
    with pytest.raises(ConfParserException):
        ConfParser()


def test_parser_with_path_and_conf_dict():
    with pytest.raises(ConfParserException):
        ConfParser(path='./config.yml', conf_dict={'debug': True})


def test_parser_with_conf_dict():
    config = ConfParser(
        conf_dict={
            'debug': True,
            'server': {
                'dev': {
                    'debug': True,
                    'port': 8000,
                },
                'prod': {
                    'debug': False,
                    'port': 80,
                }
            }
        },
    ).to_obj()
    assert isinstance(config, DotDict)
    assert config.debug is True
    assert isinstance(config.server, DotDict)
    assert isinstance(config.server.dev, DotDict)
    assert isinstance(config.server.prod, DotDict)
    assert config.server.dev.debug is True
    assert config.server.dev.port == 8000
    assert config.server.prod.debug is False
    assert config.server.prod.port == 80


def test_parser_with_path():
    config = ConfParser(path='./config.yml').to_obj()

    assert isinstance(config, DotDict)
    assert config.debug is True
    assert isinstance(config.server, DotDict)
    assert isinstance(config.server.dev, DotDict)
    assert isinstance(config.server.prod, DotDict)
    assert config.server.dev.debug is True
    assert config.server.dev.port == 8000
    assert config.server.prod.debug is False
    assert config.server.prod.port == 80
