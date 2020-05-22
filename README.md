# Python Config Parser Library
[![license]](/LICENSE)
[![pypi]](https://pypi.org/project/confparser/)
[![pyversions]](http://pypi.python.org/pypi/confparser)
![badge](https://action-badges.now.sh/teamhide/confparser)

confparser is a config parser by yml file or dictionary.

In confparser, you can easily access to value through dot notation.

Like, `conf.debug`, `conf.server.dev.debug`.

## Installation

```python
pip3 install confparser
```

## Usage

### Config by .yml file

Create yml file

```yaml
debug: True
server:
  dev:
    debug: True
    port: 8000
  prod:
    debug: False
    port: 80
```

Import confparser and insert your yml file.
```python
from confparser import ConfParser


config = ConfParser(path='./config.yml').to_obj()

print(config)
# {'debug': True, 'server': {'dev': {'debug': True, 'port': 8000}, 'prod': {'debug': False, 'port': 80}}}

print(config.debug)  
# True

print(config.server)
# {'dev': {'debug': True, 'port': 8000}, 'prod': {'debug': False, 'port': 80}}

print(config.server.dev)
# {'debug': True, 'port': 8000}

print(config.server.dev.debug)  
# True

print(config.server.dev.port)  
# 8000

print(config.server.prod.debug)  
# False

print(config.server.prod.port)  
# 80
```

### Config by dictionary

Import confparser and insert your dictionary.
```python
from confparser import ConfParser

conf_dict = {
    'debug': True,
    'server': {
        'dev': {
            'debug': True,
            'port': 8000,
        },
        'prod': {
            'debug': False,
            'port': 80,
        },
    }
}
config = ConfParser(conf_dict=conf_dict).to_obj()

print(config)
# {'debug': True, 'server': {'dev': {'debug': True, 'port': 8000}, 'prod': {'debug': False, 'port': 80}}}

print(config.debug)  
# True

print(config.server)
# {'dev': {'debug': True, 'port': 8000}, 'prod': {'debug': False, 'port': 80}}

print(config.server.dev)
# {'debug': True, 'port': 8000}

print(config.server.dev.debug)  
# True

print(config.server.dev.port)  
# 8000

print(config.server.prod.debug)  
# False

print(config.server.prod.port)  
# 80
```

## Note

`path` and `conf_dict` cannot be used at once.

## Dependencies

To use parsing yml file, `pyyaml` is needed.

But it will be install automatically with confparser so you don't have to install manually.


[license]: https://img.shields.io/badge/License-MIT-yellow.svg
[pypi]: https://img.shields.io/pypi/v/confparser
[pyversions]: https://img.shields.io/pypi/pyversions/confparser