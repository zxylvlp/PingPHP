''' AST BaseNode Abstract Class
'''
from helper import *

'''utils functions'''
indentLevel = 0
outputString = []

def indent():
	global indentLevel
	indentLevel += 1

def outdent():
	global indentLevel
	indentLevel -= 1

def append(val):
	global outputString
	if isinstance(val, list):
		outputString.extend(val)	
	else:
		outputString.append(val)

def finishOutput():
	global outputString
	#printObj(outputString)
	res = ''.join(outputString)
	initOutput()
	return res

def initOutput():
	global outputString, indentLevel
	indentLevel = 0
	outputString = ['<?php\n']

def popStr():
	global outputString
	outputString.pop()
		
	
def indentSpaces():
	global indentLevel
	return ''.join(['        ' for i in xrange(0,indentLevel)])

''' Node classes '''
class BaseNode(object):
	def __init__(self, val):
		self.val = val
	def gen(self):
		if self.val:
			from helper import isString
			if isString(self.val):
				append(self.val)
			elif hasattr(self.val, 'gen'):
				self.val.gen()

class WithTerminatorNode(BaseNode):
	def __init__(self, val, terminator):
		super(WithTerminatorNode, self).__init__(val)
		self.terminator = terminator
	
class Root(BaseNode):
	def gen(self):
		initOutput()
		super(Root, self).gen()
		return finishOutput()
			
	
class Body(BaseNode):
	def __init__(self, body, val):
		self.body = body
		super(Body, self).__init__(val)
	def gen(self):
		if self.body!=None:
			self.body.gen()
		super(Body, self).gen()

'''
indent is Line's duty
'''
class Line(BaseNode):
	def gen(self):
		append(indentSpaces())
		super(Line, self).gen()
		append('\n')

class Embeded(BaseNode):
	pass

class Statement(WithTerminatorNode):
	def __init__(self, val, terminator):
		super(Statement, self).__init__(val, terminator)
	def gen(self):
		super(Statement, self).gen()
		append(';')
		self.terminator.gen()
	
class StatementWithoutTerminator(BaseNode):
	pass

class JustStrStatementWithTerminator(WithTerminatorNode):
	pass

class CodeBlock(BaseNode):
	pass

class Expression(BaseNode):
	pass

class Block(BaseNode):
	def gen(self):
		indent()
		super(Block, self).gen()
		outdent()

class InitModifier(BaseNode):
	pass

class AssignRightSide(BaseNode):
	def gen(self):
		append(' = ')
		super(AssignRightSide, self).gen()

class Value(BaseNode):
	pass

class Literal(BaseNode):
	pass

class SimpleLiteral(BaseNode):
	pass

class ArrayLiteral(BaseNode):
	def gen(self):
		append('[')
		super(ArrayLiteral, self).gen()
		append(']')

class CommaList(BaseNode):
	def __init__(self, list_, val):
		super(CommaList, self).__init__(val)
		self.list_ = list_
	def gen(self):
		if self.list_!=None:
			self.list_.gen()
			append(', ')
		super(CommaList, self).gen()

class ArrayLiteralContentList(CommaList):
	pass

class ArrayLiteralContent(BaseNode):
	def __init__(self, key, val):
		self.key = key
		super(ArrayLiteralContent, self).__init__(val)
	def gen(self):
		if self.key!=None:
			self.key.gen()
			append(' => ')
		super(ArrayLiteralContent, self).gen()

class Varible(BaseNode):
	def __init__(self, nsContentName, val):
		self.nsContentName = nsContentName
		super(Varible, self).__init__(val)
	def gen(self):
		if self.nsContentName:
			self.nsContentName.gen()
			append('::')
		if not val.isupper():
			append('$')
		super(Varible, self).gen()

class Assignable(BaseNode):
	def __init__(self, val, exp, id_):
		super(Assignable, self).__init__(val)
		self.exp = exp
		self.id_ = id_
	def gen(self):
		super(Assignable, self).gen()
		if self.exp!=None and self.id_==None:
			append('[')	
			self.exp.gen()
			append(']')
		elif self.exp==None and self.id_!=None:
			append(['.', id_])

class Assign(BaseNode):
	def __init__(self, val, rightSide):
		super(Assign, self).__init__(val)
		self.rightSide = rightSide
	def gen(self):
		super(Assign, self).gen()
		self.rightSide.gen()

class ArgList(CommaList):
	pass

class Arg(BaseNode):
	pass

class ParamList(CommaList):
	pass

class Param(BaseNode):
	def __init__(self, val, init):
		super(Param, self).__init__(val)
		self.init = init
	def gen(self):
		append('$')
		super(Param, self).gen()
		self.init.gen()

class Call(BaseNode):
	def __init__(self, val, args):
		super(Call,self).__init__(val)
		self.args = args
	def gen(self):
		super(Call, self).gen()
		append('(')
		self.args.gen()
		append(')')

class Callable(BaseNode):
	pass

class Terminator(BaseNode):
	pass

class Namespace(BaseNode):
	def gen(self):
		append('namespace ')
		super(Namespace, self).gen()

class UseNamespace(BaseNode):
	def gen(self):
		append('use ')
		super(UseNamespace, self).gen()

class NsContentName(BaseNode):
	def __init__(self, list_, val):
		super(NsContentName, self).__init__(val)
		self.list_ = list_
	def gen(self):
		self.list_ and self.list_.gen()
		super(NsContentName, self).gen()

class NsContentNameList(CommaList):
	pass

class NsContentNameAsId(BaseNode):
	def __init__(self, val, id_):
		super(NsContentNameAsId, self).__init__(val)
		self.id_ = id_
	def gen(self):
		super(NsContentNameAsId, self).gen()
		append(['as ', self.id_])

class NsContentNameAsIdList(CommaList):
	pass

class If(WithTerminatorNode):
	def __init__(self, val, elseBlock, terminator):
		super(If, self).__init__(val, terminator)
		self.elseBlock = elseBlock
	def gen(self):
		super(If, self).gen()
		if elseBlock:
			append(' else {')
			self.terminator.gen()
			append('\n')
			self.elseBlock.gen()
			append([indentSpaces(), '}'])

class IfBlock(WithTerminatorNode):
	def __init__(self, list_, exp, terminator, block):
		super(IfBlock, self).__init__(exp, terminator)
		self.list_ = list_
		self.block = block
	def gen(self):
		if self.list_ != None:
			self.list_.gen()
			append([indentSpaces(), ' else if ('])
		else:
			append('if (')
		super(IfBlock, self).gen()
		append(') {')
		self.terminator.gen()
		append('\n')
		self.block.gen()
		append([indentSpaces(), '}'])

class For(WithTerminatorNode):
	def __init__(self, id1, id2, exp, terminator, block):
		super(For, self).__init__(exp, terminator)
		self.id1 = id1
		self.id2 = id2
		self.block = block
	def gen(self):
		append('foreach (')
		super(For, self).gen()
		append(' as ')
		append(['$', id1])
		self.id2 and append([' => $', id2])
		append(') {')
		self.terminator.gen()
		append('\n')
		self.block.gen()
		append([indentSpaces(), '}'])

class Class(WithTerminatorNode):
	def __init__(self, id_, extends, implements, terminator, content):
		super(Class, self).__init__(id_, terminator)
		self.extends = extends
		self.implements = implements
		self.content = content
	def gen(self):
		append(['class ', self.val])
		self.extends.gen()
		self.implements.gen()
		append(' {')
		self.terminator.gen()
		append('\n')
		self.content.gen()
		append([indentSpaces(), '}'])

class ClassContent(Block):
	pass

class InClassDefList(Body):
	pass

class InClassDef(Line):
	pass

class Interface(WithTerminatorNode):
	def __init__(self, id_, extends, terminator, content):
		super(Interface, self).__init__(id_, terminator)
		self.extends = extends
		self.terminator = terminator
		self.content = content
	def gen(self):
		append(['interface ', self.val])
		self.extends.gen()
		append(' {')
		self.terminator.gen()
		append('\n')
		self.content.gen()
		append([indentSpaces(), '}'])

class InterfaceContent(Block):
	pass

class InterfaceDefList(Body):
	pass

class InterfaceDef(Line):
	pass

class ExtendsModifier(BaseNode):
	def gen(self):
		if not self.val:
			return
		append(' extends ')
		super(ExtendsModifier, self).gen()

class ImplementsModifier(BaseNode):
	def gen(self):
		if not self.val:
			return
		append(' implements ')
		super(ImplementsModifier, self).gen()

class JustStrModifier(BaseNode):
	def gen(self):
		super(JustStrModifier, self).gen()
		self.val and append(' ')


class AccessModifier(JustStrModifier):
	pass

class StaticModifier(JustStrModifier):
	pass

class MemberFuncDecWithoutTerminator(BaseNode):
	def __init__(self, access, static, id_, paramList):
		super(MemberFuncDecWithoutTerminator, self).__init__(id_)
		self.access = access
		self.static = static
		self.paramList = paramList
	def gen(self):
		self.access.gen()
		self.static.gen()
		append('function ')
		super(MemberFuncDecWithoutTerminator, self).gen()
		append('(')
		self.paramList.gen()
		append(')')
		
class MemberFuncDec(WithTerminatorNode):
	def gen(self):
		super(MemberFuncDec, self).gen()
		append(';')
		self.terminator.gen()

class MemberFuncDef(WithTerminatorNode):
	def __init__(self, val, terminator, block):
		super(MemberFuncDef, self).__init__(val, terminator)
		self.block = block
	def gen(self):
		super(MemberFuncDef, self).gen()
		append(' {')
		self.terminator.gen()
		append('\n')
		self.block.gen()
		append([indentSpaces(), '}'])

class DataMemberDef(WithTerminatorNode):
	def __init__(self, access, static, id_, init, terminator):
		super(DataMemberDef, self).__init__(id_, terminator)
		self.access = access
		self.static = static
		self.init = init
	def gen(self):
		self.access.gen()
		self.static.gen()
		append('$')
		super(DataMemberDef, self).gen()
		self.init.gen()
		append(';')
		self.terminator.gen()
		
class FuncDef(WithTerminatorNode):
	def __init__(self, id_, paramList, terminator, block):
		super(FuncDef, self).__init__(id_, terminator)
		self.paramList = paramList
		self.block = block
	def gen(self):
		append('function ')
		super(FuncDef, self).gen()
		append('(')
		self.paramList.gen()
		append(') {')
		self.terminator.gen()
		append('\n')
		self.block.gen()
		append([indentSpaces(), '}'])

class ConstDefWithoutTerminator(BaseNode):
	def __init__(self, id_, assignRightSide):
		super(ConstDefWithoutTerminator, self).__init__(id_)
		self.assignRightSide = assignRightSide
	def gen(self):
		append('const ')
		super(ConstDefWithoutTerminator, self).gen()
		self.assignRightSide.gen()
			
class ConstDef(WithTerminatorNode):
	def gen(self):
		super(ConstDef, self).gen()
		append(';')
		self.terminator.gen()

class Return(BaseNode):
	def gen(self):
		append('return')
		self.val and append(' ')
		super(Return, self).gen()

class GlobalDec(BaseNode):
	def gen(self): 
		append('global ')
		super(GlobalDec, self).gen()

class GlobalVaribleList(CommaList):
	pass

class Operation(BaseNode):
	pass

class BinaryOperationNode(BaseNode):
	def __init__(self, exp1, op, exp2):
		super(BinaryOperationNode, self).__init__(op)
		self.exp1 = exp1
		self.exp2 = exp2
	def gen(self):
		self.exp1.gen()
		append([' ', op, ' '])
		self.exp2.gen()



class Math(BinaryOperationNode):
	pass

class New(BaseNode):
	def __init__(self, nsConentName, argList, varible):
		super(New, self).__init__(nsContentName)
		self.argList = argList
		self.varible = varible
	def gen(self):
		if self.argList:
			append('new ')
			super(New, self).gen()
			append('(')
			self.argList.gen()
			append(')')
		else:
			append('new ')
			self.varible.gen()

class Compare(BinaryOperationNode):
	pass

if __name__ == '__main__':
	pass
	#b = BaseNode('str')
	#print b.isinstance(basestring)
	#print Body.indentLevel
	
