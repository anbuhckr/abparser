#! /usr/bin/env python3

import sys
from abparser import AbParser

if __name__ == '__main__':
    abp = AbParser(sys.argv[1])
    print('start matching')
    abp.match(sys.argv[2])
