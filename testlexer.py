#!/usr/bin/env python

import sys
from pingphp.helper import read
from pingphp.lexer import PingLexer

filename = './test/test/'

if len(sys.argv)>1:
    filename += sys.argv[1]
else:
    print('Please input filename!')
    exit(1)

lexer = PingLexer(read(filename))

for item in lexer:
    print(item)
