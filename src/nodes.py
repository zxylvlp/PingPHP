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
    # printObj(outputString)
    res = ''.join(outputString)
    initOutput()
    return res


def initOutput():
    global outputString, indentLevel
    indentLevel = 0
    outputString = ['<?php', '\n']


def popStr():
    global outputString
    outputString.pop()

def popStrToLastNewLine():
    while lastStr() != '\n':
        popStr()
    popStr()

def lastStr():
    global outputString
    return outputString[-1]


def indentSpaces():
    global indentLevel
    return ''.join(['    ' for i in xrange(0, indentLevel)])

def notFunction(name):
    notFunctions = ['echo', 'require', 'require_once', 'include', 'include_once']
    if name in notFunctions:
        return True
    return False

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

class UnaryOperationNode(BaseNode):
    def __init__(self, op, exp):
        super(UnaryOperationNode, self).__init__(op)
        self.exp = exp

    def gen(self):
        super(UnaryOperationNode, self).gen()
        self.exp.gen()

class UnaryOperationWithSpaceNode(UnaryOperationNode):
    def gen(self):
        super(UnaryOperationWithSpaceNode, self).gen()
        append(' ')
        self.exp.gen()

class BinaryOperationNode(BaseNode):
    def __init__(self, exp1, op, exp2):
        super(BinaryOperationNode, self).__init__(op)
        self.exp1 = exp1
        self.exp2 = exp2

    def gen(self):
        self.exp1.gen()
        append([' ', self.val, ' '])
        self.exp2.gen()


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
        if self.body != None:
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

        if not self.val.val=='':
            append('; ')
            self.terminator.gen()
        else:
            popStrToLastNewLine()
            
class LambdaAssignStatement(BaseNode):
    def __init__(self, val, lambda_):
        super(LambdaAssignStatement, self).__init__(val)
        self.lambda_ = lambda_
    def gen(self):
        super(LambdaAssignStatement, self).gen()
        append(' = ')
        self.lambda_.gen()

class StatementWithoutTerminator(BaseNode):
    pass


class JustStrStatementWithTerminator(WithTerminatorNode):
    def gen(self):
        if not self.val=='':
            append('; ')
            self.terminator.gen()
        else:
            popStrToLastNewLine()
         


class CodeBlock(BaseNode):
    pass


class Expression(BaseNode):
    def gen(self):
        if isinstance(self.val, Expression):
            append('(')
            super(Expression, self).gen()
            append(')')
        else:
            super(Expression, self).gen()


class Block(BaseNode):
    def gen(self):
        indent()
        super(Block, self).gen()
        outdent()


class InitModifier(BaseNode):
    pass


class AssignRightSide(BaseNode):
    def __init__(self, assign, exp):
        super(AssignRightSide, self).__init__(assign)
        self.exp = exp
    
    def gen(self):
        append(' ')
        super(AssignRightSide, self).gen()
        append(' ')
        self.exp.gen()


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
        if self.list_ != None:
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
        if self.key != None:
            self.key.gen()
            append(' => ')
        super(ArrayLiteralContent, self).gen()


class Varible(BaseNode):
    def __init__(self, nsContentName, val):
        self.nsContentName = nsContentName
        super(Varible, self).__init__(val)

    def gen(self):
        if self.nsContentName:
            if isinstance(self.nsContentName, basestring):
                append(self.nsContentName)
            else:
                self.nsContentName.gen()
            append('::')
        if isinstance(self.val, NsContentName):
            self.val.list_ and self.val.list_.gen()
            self.val = self.val.val
        if not (self.val.isupper() or self.val == 'class'):
            append('$')
        super(Varible, self).gen()


class Assignable(BaseNode):
    def __init__(self, val, exp, id_):
        super(Assignable, self).__init__(val)
        self.exp = exp
        self.id_ = id_

    def gen(self):
        super(Assignable, self).gen()
        if self.exp != None and self.id_ == None:
            append('[')
            self.exp.gen()
            append(']')
        elif self.exp == None and self.id_ != None:
            append(['->', self.id_])


class Assign(BaseNode):
    def __init__(self, val, rightSide):
        super(Assign, self).__init__(val)
        self.rightSide = rightSide

    def gen(self):
        if isinstance(self.val, ArrayLiteral):
            append('list(')
            self.val.val.gen()
            append(')')
        else:
            super(Assign, self).gen()
        self.rightSide.gen()


class ArgList(CommaList):
    pass


class Arg(BaseNode):
    def __init__(self, exp, threeDot):
        self.threeDot = threeDot
        super(Arg, self).__init__(exp)
    def gen(self):
        self.threeDot and self.threeDot.gen()
        super(Arg, self).gen()


class ParamList(CommaList):
    pass

class ThreeDotModifier(BaseNode):
    pass

class Param(BaseNode):
    def __init__(self, ref, val, threeDot, type_, init):
        self.ref = ref
        super(Param, self).__init__(val)
        self.threeDot = threeDot
        self.type_ = type_
        self.init = init

    def gen(self):
        self.type_.gen()
        self.threeDot.gen()
        self.ref.gen()
        append('$')
        super(Param, self).gen()
        self.init.gen()

class TypeModifier(BaseNode):
    def gen(self):
        super(TypeModifier, self).gen()
        self.val and append(' ')

class Call(BaseNode):
    def __init__(self, val, args):
        super(Call, self).__init__(val)
        self.args = args

    def gen(self):
        super(Call, self).gen()
        last = lastStr()
        isNotFunction = notFunction(last)
        if isNotFunction:
            append(' ')
        else:
            append('(')
        self.args.gen()
        if not isNotFunction:
            append(')')


class Callable(BaseNode):
    def __init__(self, val, id_):
        super(Callable, self).__init__(val)
        self.id_ = id_
    def gen(self):
        super(Callable, self).gen()
        if self.id_:
            append('::')
            append(self.id_)


class Lambda(WithTerminatorNode):
    def __init__(self, paramList, use, terminator, block):
        super(Lambda, self).__init__(paramList, terminator)
        self.use = use
        self.block = block
    def gen(self):
        append('function (')
        super(Lambda, self).gen()
        append(') ')
        self.use.gen()
        append('{ ')
        self.terminator.gen()
        append('\n')
        self.block.gen()
        append([indentSpaces(), '}'])

class UseModifier(BaseNode):
    def __init__(self, paramList):
        super(UseModifier, self).__init__(paramList)
    def gen(self):
        if not self.val:
            return
        append('use (')
        super(UseModifier, self).gen()
        append(')')


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

class DefOrConstModifier(BaseNode):
    def gen(self):
        if not self.val:
            return
        if self.val == 'def':
            self.val = 'function'
        super(DefOrConstModifier, self).gen()
        append(' ')


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
    def __init__(self, defOrConst, val, id_):
        self.defOrConst = defOrConst
        super(NsContentNameAsId, self).__init__(val)
        self.id_ = id_

    def gen(self):
        self.defOrConst.gen()
        super(NsContentNameAsId, self).gen()
        self.id_ and append([' as ', self.id_])


class NsContentNameAsIdList(CommaList):
    pass


class If(WithTerminatorNode):
    def __init__(self, val, elseBlock, terminator):
        super(If, self).__init__(val, terminator)
        self.elseBlock = elseBlock

    def gen(self):
        super(If, self).gen()
        if self.elseBlock:
            append(' else { ')
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
            append(' else if (')
        else:
            append('if (')
        super(IfBlock, self).gen()
        append(') { ')
        self.terminator.gen()
        append('\n')
        self.block.gen()
        append([indentSpaces(), '}'])

class Switch(WithTerminatorNode):
    def __init__(self, exp, terminator, content):
        super(Switch, self).__init__(exp, terminator)
        self.content = content
    def gen(self):
        append('switch (')
        super(Switch, self).gen()
        append(') { ')
        self.terminator.gen()
        append('\n')
        self.content.gen()
        append([indentSpaces(), '}'])

class SwitchContent(Block):
    pass


class InSwitchDefList(Body):
    pass


class InSwitchDef(Line):
    pass


class ValueList(BaseNode):
    def __init__(self, list_, value):
        super(ValueList, self).__init__(value)
        self.list_ = list_

class Case(WithTerminatorNode):
    def __init__(self, case, valueList, terminator, block):
        super(Case, self).__init__(case, terminator)
        self.valueList = valueList
        self.block = block
    def gen(self):
        if self.val == 'case':
            valueList = []
            while(self.valueList):
                valueList.append(self.valueList.val)
                self.valueList = self.valueList.list_
            valueList.reverse()
            popStr()
            for value in valueList:
                append([indentSpaces(), 'case '])
                value.gen()
                append([' : ', '\n'])
            popStr()
            self.terminator.gen()
            append('\n')
            self.block.gen()
            indent()
            append([indentSpaces(), 'break; ', '\n'])
            outdent()
        else:
            append('default : ')
            self.terminator.gen()
            append('\n')
            self.block.gen()
        popStr()





class For(WithTerminatorNode):
    def __init__(self, id1Ref, id1, id2Ref, id2, exp, terminator, block):
        super(For, self).__init__(exp, terminator)
        self.id1Ref = id1Ref
        self.id1 = id1
        self.id2Ref = id2Ref
        self.id2 = id2
        self.block = block

    def gen(self):
        append('foreach (')
        super(For, self).gen()
        append(' as ')
        self.id1Ref.gen()
        append(['$', self.id1])
        if self.id2:
            append(' => ')
            self.id2Ref.gen()
            append(['$', self.id2])
        append(') { ')
        self.terminator.gen()
        append('\n')
        self.block.gen()
        append([indentSpaces(), '}'])

class While(WithTerminatorNode):
    def __init__(self, exp, terminator, block):
        super(While, self).__init__(exp, terminator)
        self.block = block
    def gen(self):
        append('while (')
        super(While, self).gen()
        append(') { ')
        self.terminator.gen()
        append('\n')
        self.block.gen()
        append([indentSpaces(), '}'])

class DoWhile(WithTerminatorNode):
    def __init__(self, term1, block, cmtOrEptList, exp, term2):
        super(DoWhile, self).__init__(exp, term1)
        self.block = block
        self.term2 = term2
        self.cmtOrEptList = cmtOrEptList
    def gen(self):
        append('do { ')
        self.terminator.gen()
        append('\n')
        self.block.gen()
        indent()
        self.cmtOrEptList.gen()
        outdent()
        append([indentSpaces(), '} while('])
        super(DoWhile, self).gen()
        append('); ')
        self.term2.gen()

class CommentOrEmptyLineList(Body):
    pass

class CommentOrEmptyLine(Line):
    pass

class Try(WithTerminatorNode):
    def __init__(self, tryTerm, tryBlock, catch, finTerm, finBlock):
        super(Try, self).__init__(tryBlock, tryTerm)
        self.catch = catch
        self.finTerm = finTerm
        self.finBlock = finBlock
    def gen(self):
        append('try { ')
        self.terminator.gen()
        append('\n')
        super(Try, self).gen()
        append([indentSpaces(), '} '])
        self.catch.gen()
        if self.finTerm:
            append('finally { ')
            self.finTerm.gen()
            append('\n')
            self.finBlock.gen()
            append([indentSpaces(), '}'])

class Catch(WithTerminatorNode):
    def __init__(self, catch, var, className, terminator, block):
        super(Catch, self).__init__(var, terminator)
        self.catch = catch
        self.className = className
        self.block = block
    def gen(self):
        if self.catch:
            self.catch.gen()
            append('catch (')
            self.className.gen()
            append(' ')
            super(Catch, self).gen()
            append(') { ')
            self.terminator.gen()
            append('\n')
            self.block.gen()
            append([indentSpaces(), '} '])






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
        append(' { ')
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
        append(' { ')
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

class RefModifier(BaseNode):
    pass
    

class MemberFuncDecWithoutTerminator(BaseNode):
    def __init__(self, access, static, ref, id_, paramList):
        super(MemberFuncDecWithoutTerminator, self).__init__(id_)
        self.access = access
        self.static = static
        self.ref = ref
        self.paramList = paramList

    def gen(self):
        self.access.gen()
        self.static.gen()
        self.ref.gen()
        append('function ')
        super(MemberFuncDecWithoutTerminator, self).gen()
        append('(')
        self.paramList.gen()
        append(')')

class MemberFuncDec(WithTerminatorNode):
    def __init__(self, func, returnType, terminator):
        super(MemberFuncDec, self).__init__(func, terminator)
        self.returnType = returnType

    def gen(self):
        super(MemberFuncDec, self).gen()
        self.returnType.gen()
        append('; ')
        self.terminator.gen()

class ReturnTypeModifierForDec(BaseNode):
    def gen(self):
        if not self.val:
            return
        append(': ')
        super(ReturnTypeModifierForDec, self).gen()
        append(' ')

class MemberFuncDef(WithTerminatorNode):
    def __init__(self, val, returnType, terminator, block):
        super(MemberFuncDef, self).__init__(val, terminator)
        self.block = block
        self.returnType = returnType

    def gen(self):
        super(MemberFuncDef, self).gen()
        self.returnType.gen()
        append(' { ')
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
        append('; ')
        self.terminator.gen()

class ReturnTypeModifier(BaseNode):
    def gen(self):
        if self.val:
            append(': ')
            self.val.gen()
            

class FuncDef(WithTerminatorNode):
    def __init__(self, ref, id_, paramList, returnType, terminator, block):
        self.ref = ref
        super(FuncDef, self).__init__(id_, terminator)
        self.paramList = paramList
        self.returnType = returnType
        self.block = block

    def gen(self):
        append('function ')
        self.ref.gen()
        super(FuncDef, self).gen()
        append('(')
        self.paramList.gen()
        append(')')
        self.returnType.gen()
        append(' { ')
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
        append('; ')
        self.terminator.gen()


class Return(BaseNode):
    def gen(self):
        append('return')
        self.val and append(' ')
        super(Return, self).gen()

class Throw(BaseNode):
    def gen(self):
        append('throw ')
        super(Throw, self).gen()

class Yield(BaseNode):
    def __init__(self, exp1, exp2):
        super(Yield, self).__init__(exp1)
        self.exp2 = exp2
    def gen(self):
        append('yield ')
        super(Yield, self).gen()
        if self.exp2:
            append(' => ')
            self.exp2.gen()


class GlobalDec(BaseNode):
    def gen(self):
        append('global ')
        super(GlobalDec, self).gen()


class GlobalVaribleList(CommaList):
    def gen(self):
        if self.list_ != None:
            self.list_.gen()
            append(', ')
        append('$')
        super(CommaList, self).gen()

class Operation(BaseNode):
    pass


class UMath(UnaryOperationNode):
    pass

class BMath(BinaryOperationNode):
    pass

class Cast(UnaryOperationNode):
    pass

class InDecrement(UnaryOperationNode):
    def __init__(self, op, exp, back):
        super(InDecrement, self).__init__(op, exp)
        self.back = back 
    def gen(self):
        if self.back == True:
            self.exp.gen()
            append(self.val)
        else:
            super(InDecrement, self).gen()

class UBit(UnaryOperationNode):
    pass

class BBit(UnaryOperationNode):
    pass

class InstanceOf(BinaryOperationNode):
    pass

class ULogic(UnaryOperationNode):
    pass

class BLogic(BinaryOperationNode):
    pass

class NewOrClone(BaseNode):
    def __init__(self, newOrClone, nsContentName, argList, varible):
        super(NewOrClone, self).__init__(nsContentName)
        self.argList = argList
        self.varible = varible
        self.newOrClone = newOrClone

    def gen(self):
        append(self.newOrClone)
        append(' ')
        if self.argList:
            super(NewOrClone, self).gen()
            append('(')
            self.argList.gen()
            append(')')
        else:
            if isinstance(self.varible, basestring):
                append(self.varible)
            else:
                self.varible.gen()



class Compare(BinaryOperationNode):
    pass

class Ternary(BaseNode):
    def __init__(self, exp1, exp2, exp3):
        super(Ternary, self).__init__(exp1)
        self.exp2 = exp2
        self.exp3 = exp3
    def gen(self):
        super(Ternary, self).gen()
        append(' ? ')
        self.exp2.gen()
        append(' : ')
        self.exp3.gen()

class At(UnaryOperationNode):
    pass

class Ref(UnaryOperationNode):
    pass


if __name__ == '__main__':
    pass
    # b = BaseNode('str')
    # print b.isinstance(basestring)
    # print Body.indentLevel
