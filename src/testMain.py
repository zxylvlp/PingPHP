from .helper import *
from .grammar import *
from .lexer import PingLexer
from .ply import yacc

if __name__ == '__main__':
    pLexer = PingLexer(read('./test/References/whatdo.ping'))
    parser = yacc.yacc(debug=1, write_tables=0)
    res = parser.parse(lexer=pLexer,debug=True)
    str_res = res.gen()
    # write('test.php',str_res)

    print(res.gen())
