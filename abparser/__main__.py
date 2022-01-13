#! /usr/bin/env python3

import sys
from abparser import AbParser

if __name__ == '__main__':
    abp = AbParser(sys.argv[1])
    if abp.match(sys.argv[2]):
        print(f"{sys.argv[2]} is blocked!!!")
    else:
        print(f"{sys.argv[2]} is clear!!!")

