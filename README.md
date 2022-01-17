# abparser

[![GitHub issues](https://img.shields.io/github/issues/anbuhckr/abparser)](https://github.com/anbuhckr/abparser/issues)
[![GitHub forks](https://img.shields.io/github/forks/anbuhckr/abparser)](https://github.com/anbuhckr/abparser/network)
[![GitHub stars](https://img.shields.io/github/stars/anbuhckr/abparser)](https://github.com/anbuhckr/abparser/stargazers)
[![GitHub license](https://img.shields.io/github/license/anbuhckr/abparser)](./LICENSE)
![PyPI - Python Version](https://img.shields.io/badge/python-3.6%20%7C%203.7%20%7C%203.8%20%7C%203.9-blue)

Python Adblock Plus Parser

## Table of Contents

* [Installation](#installation)
* [CLI](#CLI)
* [Getting Started](#getting-started)


## Installation

To install bincli, simply:

```
$ python3 -m pip install -U git+https://github.com/anbuhckr/abparser.git
```

or from source:

```
$ python3 setup.py install
```

## CLI

Usage:

```
# dowload file from https://easylist.to/easylist/easylist.txt
$ python3 -m abparser easylist.txt https://ads.google.com
```

## Getting Started

``` python
#! /usr/bin/env python3

from abparser import AbParser

# dowload file from https://easylist.to/easylist/easylist.txt
rules = AbParser('easylist.txt')
url = "https://ads.google.com"
if rules.match(url):
    print(f"{url} is blocked!!!")
else:
    print(f"{url} is clear!!!")
```
