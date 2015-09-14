# encoding: utf-8
'''
PingPHP lexer
'''

from ply import lex

reserved = set([
    # namespace
    'namespace', 'use', 'as', 'insteadof',
    # class and interface
    'class', 'extends', 'implements',
    'public', 'private', 'protected',
    'static', 'abstract', 'final',
    'interface', 'trait',

    # ctrl flow
    'if', 'elif', 'else',
    'for', 'in',
    'switch', 'case', 'default',
    'while', 'do',
    'declare',

    # function
    'def',

    # op
    'new', 'clone',
    'instanceof',

    'not', 'or', 'and',

    'const', 'global',

    'try', 'catch', 'finally',

    'yield',

    'lambda'

])

strStatment = set(['pass', 'break', 'continue', 'echo', 'print', 'require', 'require_once',
                   'include', 'include_once', 'return', 'throw'])

reservedMap = {
    'not': '!',
    'and': '&&',
    'or': '||'
}

commentAndNative = [
    'DOCCOMMENT',
    'INLINECOMMENT',
    'NATIVEPHP',
    'EMPTYLINE'
]

braces = [
    'LPARENT',
    'RPARENT',
    'LBRACKET',
    'RBRACKET'
]

bit = [
    'SHIFT',
    'ANDOP',
    'BITNOT',
    'BITOR',
    'BITXOR'
]

math = [
    'EXPONENT',
    'MATH1',
    'MATH2',
    'INDECREMENT',
]

slash = [
    'SLASH',
    'FOLDLINE'
]

numAndStr = [
    'STRING',
    'NUMBER'
]

inOutdent = [
    'INDENT',
    'OUTDENT'
]

tokens = [
             'ASSIGN',
             'COMPARE',
             'CAST',
             'AT',
             'STRCAT',
             'SCOPEOP',
             'INDENTIFIER',
             'COMMA',
             'THREEDOT',
             'DOT',
             'COLON',
             'SPACE',
             'TAB',
             'NEWLINE',
             'TERMINATOR',
             'STATEMENT',
             'NAMESPACEBEFORESLASH',
             'EXEC'

         ] + list(
    map(lambda x: x.upper(), reserved)) + commentAndNative + braces + bit + math + slash + numAndStr + inOutdent


def lineNoInc(t):
    t.lexer.lineno += t.value.count('\n')


def t_DOCCOMMENT(t):
    r'((\'\'\'((?!\'\'\')[\s\S])*\'\'\')|(\'{6,8})|("""((?!""")[\s\S])*""")|("{6,8}))[ \t]*\n'
    lineNoInc(t)
    pos = t.value.rfind('"""')
    if pos == -1:
        pos = t.value.rfind('\'\'\'')
    t.value = '/**' + t.value[3:pos] + '**/'
    return t


def t_NATIVEPHP(t):
    r'<\?php((?!<\?php)[\s\S])*\?>[ \t]*(?=\n)'
    lineNoInc(t)
    t.value = t.value[6:].lstrip()
    pos2 = t.value.rfind('?>')
    t.value = t.value[0:pos2].rstrip()
    # print t.value
    return t


def t_INLINECOMMENT(t):
    r'\#[^\n]*\n'
    lineNoInc(t)
    t.value = '//' + t.value[1:-1]
    return t


def t_STRING(t):
    r'b?((\'(([^\'])|((?<=\\)(?<!\\\\)\'))*\')|("(([^"\n])|((?<=\\)(?<!\\\\)"))*"))'
    lineNoInc(t)
    return t


def t_EXEC(t):
    r'`(((?<!\\)`)|([^`]))*`'
    return t


def t_ASSIGN(t):
    r'(((\+|-|\*|/|%|&|\||^|(<<<)|(<<)|(>>))\s*)?=)(?![=])'
    if t.value[0:3] == '<<<':
        t.value = '.='
    return t


def t_STRCAT(t):
    r'<<<'
    t.value = '.'
    return t


def t_SHIFT(t):
    r'(<<)|(>>)'
    return t


def t_COMPARE(t):
    r'([=!]=[=]?)|(<>)|(>=?)|(<=?)'
    return t


def t_FOLDLINE(t):
    r'\\[ ]*\n'
    lineNoInc(t)


def t_NEWLINE(t):
    r'\n'
    lineNoInc(t)
    return t


def t_NUMBER(t):
    r'(([0-9]+|(([0-9]*\.[0-9]+)|([0-9]+\.[0-9]*)))[eE][+-]?[0-9]+)|(([0-9]*\.[0-9]+)|([0-9]+\.[0-9]*))|([1-9][0-9]*)|(0b[01]+)|(0[0-7]+)|(0[xX][0-9a-fA-F]+)|(true)|(false)|(null)|0'
    return t


def t_NAMESPACEBEFORESLASH(t):
    r'namespace(?=[ \t]*\\[ \t]*[_a-zA-Z0-9])'
    return t


# handle id and reversed
def t_INDENTIFIER(t):
    r'(\$?[_a-zA-Z][_a-zA-Z0-9]*)|(__[A-Z_]+__)'
    if t.value in reserved:
        t.type = t.value.upper()
        if t.value in reservedMap:
            t.value = reservedMap[t.value]
    elif t.value in strStatment:
        t.type = 'STATEMENT'
    return t


t_ANDOP = r'&'
t_BITNOT = r'~'
t_BITOR = r'\|'
t_BITXOR = r'\^'

t_EXPONENT = r'\*\*     '
t_MATH1 = r'\*|/|%'
t_MATH2 = r'\+|-'
t_INDECREMENT = r'(\+\+)|(--)'

t_CAST = r'\([ \t]*((int)|(float)|(double)|(string)|(array)|(object)|(binary)|(bool)|(unset))[ \t]*\)'
t_AT = r'@'
t_SCOPEOP = r'::'
t_SPACE = r'[ ]'
t_TAB = r'\t'

t_LPARENT = r'\('
t_RPARENT = r'\)'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_THREEDOT = r'\.\.\.'
t_DOT = r'\.'
t_SLASH = r'\\'
t_COLON = r':'


def t_error(t):
    from .helper import errorMsg
    errorMsg('Lexical', t)


def tokenList(lexer):
    return [t for t in lexer]


def makeLexToken(type, value, lineno, lexpos):
    tok = lex.LexToken()
    tok.type = type
    tok.value = value
    tok.lineno = lineno
    tok.lexpos = lexpos
    return tok


def changeTokenList(tokList):
    dummy = makeLexToken('NEWLINE', '\n', 0, 0)
    tokList.insert(0, dummy)

    dummy = makeLexToken('EOF', '', tokList[-1].lineno + 1, tokList[-1].lexpos + 1)
    tokList.append(dummy)

    preSpace = 0
    countStart = False
    spaceStack = [0]
    contentCache = []

    resultTokList = []
    for tok in tokList:
        if countStart == False and (tok.type in ('NEWLINE', 'INLINECOMMENT')):
            preSpace = 0
            countStart = True
            if tok.type == 'NEWLINE':
                tok = makeLexToken('TERMINATOR', '', tok.lineno, tok.lexpos)
            resultTokList.append(tok)
            continue
        if countStart:
            if tok.type == 'SPACE':
                preSpace += 1
            elif tok.type == 'TAB':
                preSpace += 4
            elif tok.type in ['NEWLINE', 'INLINECOMMENT', 'DOCCOMMENT']:
                preSpace = 0
                if tok.type == 'NEWLINE':
                    tok = makeLexToken('EMPTYLINE', '', tok.lineno, tok.lexpos)
                contentCache.append(tok)
            else:
                countStart = False

                if spaceStack[-1] < preSpace:
                    spaceStack.append(preSpace)
                    indent = makeLexToken('INDENT', '', tok.lineno, tok.lexpos)
                    resultTokList.append(indent)
                    # print 'INDENT'
                else:
                    while spaceStack[-1] > preSpace:
                        spaceStack.pop()
                        indent = makeLexToken('OUTDENT', '', tok.lineno, tok.lexpos)
                        resultTokList.append(indent)
                        # print 'OUTDENT'

                resultTokList.extend(contentCache)
                resultTokList.append(tok)
                contentCache = []
        else:
            if tok.type != 'SPACE' and tok.type != 'TAB':
                resultTokList.append(tok)

    return resultTokList[1:-1]


class PingLexer(object):
    def __init__(self, inputStr):
        lexer = lex.lex()
        lexer.input(inputStr)
        self.tokList = tokenList(lexer)
        self.tokList = changeTokenList(self.tokList)
        self.nowIndex = 0

    def token(self):
        if self.nowIndex < len(self.tokList):
            result = self.tokList[self.nowIndex]
            self.nowIndex += 1
            return result

    def __iter__(self):
        return self

    def next(self):
        t = self.token()
        if t is None:
            raise StopIteration
        return t

    __next__ = next
