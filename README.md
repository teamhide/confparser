# Python Config Parser Library
[![license]](/LICENSE)
[![pypi]](https://pypi.org/project/confparser/)
[![pyversions]](http://pypi.python.org/pypi/confparser)
![badge](https://action-badges.now.sh/teamhide/confparser)

confparser is a pure yml parser for python

## Installation

```python
pip3 install confparser
```

## Usage

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
print(config.debug)  
# True

print(config.server.dev.debug)  
# True

print(config.server.dev.port)  
# 8000

print(config.server.prod.debug)  
# False

print(config.server.prod.port)  
# 80
```