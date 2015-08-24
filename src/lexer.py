#!/bin/env python
# codeing: utf8

from ply import lex
from helper import *

reserved = set([
	#namespace
	'namespace', 'use', 'as',
	#class and interface
	'class', 'extends', 'implements',
	'public', 'private', 'protected', 
	'static', 'abstract',
	'interface',
	
	#ctrl flow
	'if', 'elif', 'else',
	'for', 'in',
	
	#function
	'def', 'return',
	
	#op
	'new', 'clone',
	
	'const', 'global'
	
])

commentAndNative = [
	'DOCCOMMENT',
	'INLINECOMMENT',
	'NATIVEPHP',
	'EMPTYLINE'
]


braces = [
	'LPARENT',
	'RPARENT',
	'LBRACE',
	'RBRACE',
	'LBRACKET',
	'RBRACKET'
]

tokens = [
#	'COMPAREOP1',
#	'COMPAREOP2',
	'SCOPEOP',
	'ASSIGN',
	'INDENT',
	'OUTDENT',
	'INDENTIFIER',
	'DOT',
	'BACKSLASH',
	'SLASH',
	'COLON',
	'NUMBER',
	'SPACE',
	'NEWLINE',
	'TAB',
	'STRING',
	'PLUS',
	'COMMA',
	'EQ',
	'TERMINATOR',
	'STATEMENT'

] + map(lambda x:x.upper(), reserved) + commentAndNative + braces

def t_DOCCOMMENT(t):
	r'((\'\'\'((?!\'\'\')[\s\S])*\'\'\')|(\'{6,8})|("""((?!""")[\s|s])*""")|("{6,8}))[ \t]*\n'
	pos = t.value.rfind('"""')
	if pos == -1:
		pos = t.value.rfind('\'\'\'')
	t.value = '/**' + t.value[3:pos] + '**/'
	return t

#t_BITOPUN = r'~'
#t_BITOPBIN = r'(&)|(\|)|(\^)|(<<)|(>>)'

#t_COMPAREOP1 = r'(<)|(<=)|(>)|(>=)'
#t_COMPAREOP2 = r'(==)|(!=)|(===)|(!==)|(<>)'
t_EQ = r'=='
t_SCOPEOP = r'::'
t_SPACE = r'[ ]'
t_TAB = r'\t'
t_ASSIGN = r'='
t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_PLUS = r'\+'
t_COMMA = r','
t_DOT = r'\.'
t_BACKSLASH = r'/'
t_SLASH = r'\\'

t_STATEMENT = r'(pass)|(break)|(return)'

def t_INLINECOMMENT(t):
	r'\#[^\#\n]*\n'
	t.value = '//' + t.value[1:-1]
	return t

# handle id and reversed
def t_INDENTIFIER(t):
	r'[_a-zA-z][_a-zA-Z0-9]*'
	if t.value in reserved:
		t.type = t.value.upper()
	return t



def t_NATIVEPHP(t):
	r'<\?php((?!<\\?php)[\s\S])*\?>[ \t]*\n'
	pos = t.value.rfind('?>')
	t.value = t.value[5:pos]
	return t

t_STRING = r'(\'(([^\'])|(\\\'))*\')|("(([^"\n])|(\\"))*")'

t_NUMBER = r'0|([1-9][0-9]*)|(0b[01]+)|(0[0-7]+)|(0[xX][0-9a-fA-F]+)|(true)|(false)|(null)|(([0-9]*\.[0-9]+)|([0-9]+\.[0-9]*))|(([0-9]+|(([0-9]*\.[0-9]+)|([0-9]+\.[0-9]*)))[eE][+-]?[0-9]+)'

t_COLON = r':'


def t_error(t):
	print t

def t_NEWLINE(t):
	r'\n'
	t.lexer.lineno += 1 
	return t


def token_list(lexer):
	return [t for t in lexer]

def make_lexToken(type, value, lineno, lexpos):
	tok = lex.LexToken()#'NEWLINE','\n',0,0)
	tok.type = type
	tok.value = value
	tok.lineno = lineno
        tok.lexpos = lexpos
	return tok

def change_token_list_new(tok_list):

	#from ply import lex 
	dummy = make_lexToken('NEWLINE', '\n', 0, 0)
	tok_list.insert(0, dummy)

	dummy = make_lexToken('EOF', '', tok_list[-1].lineno + 1, tok_list[-1].lexpos + 1)
	tok_list.append(dummy)


	pre_space = 0
	count_start = False
	space_stack = [0]
	content_cache = []

	result_tok_list = []
	for tok in tok_list:
		if count_start==False and (tok.type in ('NEWLINE', 'INLINECOMMENT')):
			pre_space = 0
			count_start = True
			if tok.type == 'NEWLINE':
				tok = make_lexToken('TERMINATOR', '', tok.lineno, tok.lexpos)
			result_tok_list.append(tok)
			continue
		if count_start:
			if tok.type == 'SPACE':
				pre_space += 1
			elif tok.type == 'TAB':
				pre_space += 8
			elif tok.type in ['NEWLINE', 'INLINECOMMENT', 'DOCCOMMENT', 'NATIVEPHP']:
				pre_space = 0
				if tok.type == 'NEWLINE':
					tok= make_lexToken('EMPTYLINE', '', tok.lineno, tok.lexpos)
				content_cache.append(tok)
			else:
				count_start = False
				
				if space_stack[-1] < pre_space:
					space_stack.append(pre_space)
					indent = make_lexToken('INDENT', '', tok.lineno, tok.lexpos)
					result_tok_list.append(indent)
					#print 'INDENT'
				else: 
					while(space_stack[-1] > pre_space):
						space_stack.pop()
						indent = make_lexToken('OUTDENT', '', tok.lineno, tok.lexpos)
						result_tok_list.append(indent)
						#print 'OUTDENT'
				
				result_tok_list.extend(content_cache)
				result_tok_list.append(tok)
				content_cache = []
		else:
			if tok.type != 'SPACE' and tok.type != 'TAB':
				result_tok_list.append(tok)
		

	return result_tok_list[1:-1]


lexer = lex.lex()


class PingLexer(object):
	def __init__(self, inputStr):
		lexer.input(inputStr)
		self.tokList = token_list(lexer)
		self.tokList = change_token_list_new(self.tokList)
		self.nowIndex = 0
	def token(self):
		if self.nowIndex < len(self.tokList):
			result = self.tokList[self.nowIndex]
			self.nowIndex+=1
			return result
	# Iterator interface
	def __iter__(self):
		return self
	def next(self):
		t = self.token()
		if t is None:
			raise StopIteration
		return t
	__next__ = next

		

if __name__ == '__main__':
	lexer.input(read('./test/asdf.ping'))
	tokList = token_list(lexer)
	for item in change_token_list_new(tokList):
		print item


