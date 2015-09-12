import re
from .helper import *


# dev helper
def findAllUpper():
    str_ = read('grammar.py')
    p = re.compile(r'[ \n\t]')
    printObj(list(set(filter(lambda x: x.isupper(), p.split(str_)))))


if __name__ == '__main__':
    findAllUpper()
