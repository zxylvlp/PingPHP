from helper import *
from grammar import *
from lexer import PingLexer
from ply import yacc

if __name__ == '__main__':
	pLexer = PingLexer(read('./test/asdf.ping'))	
	parser = yacc.yacc()
	res = parser.parse(lexer=pLexer)
	str_res = res.gen()
	write('test.php',str_res)

	print res.gen()
