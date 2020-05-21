import pytest

from confparser import ConfParser
from confparser.parser import ConfParserException, ConfParserDict


def test_parser_with_do_not_exist_path():
    with pytest.raises(ConfParserException):
        ConfParser(path='unknown')


def test_parser_with_none_path_and_none_conf_dict():
    with pytest.raises(ConfParserException):
        ConfParser()


def test_parser_with_path_and_conf_dict():
    with pytest.raises(ConfParserException):
        ConfParser(path='./config.yml', conf_dict={'debug': True})


def test_parser_conf_dict_type_is_not_dict():
    with pytest.raises(ConfParserException):
        ConfParser(conf_dict=1)

    with pytest.raises(ConfParserException):
        ConfParser(conf_dict='test')

    with pytest.raises(ConfParserException):
        ConfParser(conf_dict=())

    with pytest.raises(ConfParserException):
        ConfParser(conf_dict=[])


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
    assert isinstance(config, ConfParserDict)
    assert config == {'debug': True, 'server': {'dev': {'debug': True, 'port': 8000}, 'prod': {'debug': False, 'port': 80}}}
    assert config.debug is True
    assert isinstance(config.server, ConfParserDict)
    assert config.server == {'dev': {'debug': True, 'port': 8000}, 'prod': {'debug': False, 'port': 80}}
    assert isinstance(config.server.dev, ConfParserDict)
    assert config.server.dev == {'debug': True, 'port': 8000}
    assert isinstance(config.server.prod, ConfParserDict)
    assert config.server.prod == {'debug': False, 'port': 80}
    assert config.server.dev.debug is True
    assert config.server.dev.port == 8000
    assert config.server.prod.debug is False
    assert config.server.prod.port == 80


def test_parser_with_path():
    config = ConfParser(path='./config.yml').to_obj()

    assert isinstance(config, ConfParserDict)
    assert config == {'debug': True, 'server': {'dev': {'debug': True, 'port': 8000}, 'prod': {'debug': False, 'port': 80}}}
    assert config.debug is True
    assert isinstance(config.server, ConfParserDict)
    assert config.server == {'dev': {'debug': True, 'port': 8000}, 'prod': {'debug': False, 'port': 80}}
    assert isinstance(config.server.dev, ConfParserDict)
    assert config.server.dev == {'debug': True, 'port': 8000}
    assert isinstance(config.server.prod, ConfParserDict)
    assert config.server.prod == {'debug': False, 'port': 80}
    assert config.server.dev.debug is True
    assert config.server.dev.port == 8000
    assert config.server.prod.debug is False
    assert config.server.prod.port == 80
