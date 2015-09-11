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
            
class StatementWithoutTerminator(BaseNode):
    pass

class StaticVarDef(BaseNode):
    def __init__(self, id_, init):
        super(StaticVarDef, self).__init__(id_)
        self.init = init
    def gen(self):
        append('static $')
        super(StaticVarDef, self).gen()
        self.init.gen()


class JustStrStatement(WithTerminatorNode):
    def __init__(self, val, args, terminator):
        super(JustStrStatement, self).__init__(val, terminator)
        self.args = args
    def gen(self):
        if not self.val=='pass':
            super(JustStrStatement, self).gen()
            if self.args.val:
                append(' ')
            self.args.gen()
            append('; ')
            self.terminator.gen()
        else:
            popStrToLastNewLine()
         


class CodeBlock(BaseNode):
    pass


class Expression(BaseNode):
    pass

class ParentExp(BaseNode):
    def gen(self):
        append('(')
        super(ParentExp, self).gen()
        append(')')

class AccessObj(BaseNode):
    def __init__(self, exp1, id_, exp2):
        super(AccessObj, self).__init__(exp1)
        self.id_ = id_
        self.exp2 = exp2
    def gen(self):
        super(AccessObj, self).gen()
        if self.id_:
            append(['->', self.id_])
        else:
            append('[')
            self.exp2 and self.exp2.gen()
            append(']')


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

    def gen(self, noDollar = False):
        if self.nsContentName:
            if isinstance(self.nsContentName, basestring):
                append(self.nsContentName)
            else:
                self.nsContentName.gen()
            append('::')
        if isinstance(self.val, NsContentName):
            self.val.list_ and self.val.list_.gen()
            self.val = self.val.val
        if self.val == '_':
            return
        if not (self.val.isupper() or self.val == 'class'):
            noDollar or append('$')
        super(Varible, self).gen()


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
        append('(')
        self.args.gen()
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
                append([': ', '\n'])
            popStr()
            self.terminator.gen()
            append('\n')
            self.block.gen()
            indent()
            append([indentSpaces(), 'break; ', '\n'])
            outdent()
        else:
            append('default: ')
            self.terminator.gen()
            append('\n')
            self.block.gen()
        popStr()





class For(WithTerminatorNode):
    def __init__(self, exp1, exp2, exp3, terminator, block):
        super(For, self).__init__(exp3, terminator)
        self.exp1 = exp1
        self.exp2 = exp2
        self.block = block

    def gen(self):
        append('foreach (')
        super(For, self).gen()
        append(' as ')
        self.exp1.gen()
        if self.exp2:
            append(' => ')
            self.exp2.gen()
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

class Declare(BaseNode):
    def __init__(self, id_, exp):
        super(Declare, self).__init__(id_)
        self.exp = exp
    def gen(self):
        append('declare(')
        super(Declare, self).gen()
        append(' = ')
        self.exp.gen()
        append(')')

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
    def __init__(self,abstract, final, id_, extends, implements, terminator, content):
        self.abstract = abstract
        self.final = final
        super(Class, self).__init__(id_, terminator)
        self.extends = extends
        self.implements = implements
        self.content = content

    def gen(self):
        self.abstract.gen()
        self.final.gen()
        append('class ')
        super(Class, self).gen()
        self.extends.gen()
        self.implements.gen()
        append(' { ')
        self.terminator.gen()
        append('\n')
        self.content.gen()
        append([indentSpaces(), '}'])

class Trait(WithTerminatorNode):
    def __init__(self, id_, terminator, content):
        super(Trait, self).__init__(id_, terminator)
        self.content = content
    def gen(self):
        append('trait ')
        super(Trait, self).gen()
        append(' { ')
        self.terminator.gen()
        append('\n')
        self.content.gen()
        append([indentSpaces(), '}'])


class JustStrModifier(BaseNode):
    def gen(self):
        super(JustStrModifier, self).gen()
        self.val and append(' ')

class AbstractModifier(JustStrModifier):
    pass

class FinalModifier(JustStrModifier):
    pass

class ClassContent(Block):
    pass


class InClassDefList(Body):
    pass


class InClassDef(BaseNode):
    def __init__(self, abstract, val):
        self.abstract = abstract
        super(InClassDef, self).__init__(val)
    
    def gen(self):
        append(indentSpaces())
        self.abstract and append([self.abstract, ' '])
        super(InClassDef, self).gen()
        append('\n')

class UseTrait(WithTerminatorNode):
    def __init__(self, use, terminator, content):
        super(UseTrait, self).__init__(use, terminator)
        self.content = content
    def gen(self):
        super(UseTrait, self).gen()
        if self.content:
            append(' { ')
            self.terminator.gen()
            append('\n')
            self.content.gen()
            append([indentSpaces(), '}'])
        else:
            append('; ')
            self.terminator.gen()

class UseTraitContent(Block):
    pass

class InUseTraitDefList(Body):
    pass

class InUseTraitDef(BaseNode):
    def __init__(self, var, type_, access, ns, terminator):
        super(InUseTraitDef, self).__init__(var)
        self.type_ = type_
        self.access = access
        self.ns = ns
        self.terminator = terminator
    def gen(self):
        append(indentSpaces())
        self.val.gen(True)
        append([' ', self.type_, ' '])
        if self.access:
            self.access.gen()
        if self.ns:
            self.ns.gen()
        else:
            popStr()
        append('; ')
        self.terminator.gen()
        append('\n')



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



class AccessModifier(JustStrModifier):
    def gen(self, defaultPublic = False):
        if defaultPublic and self.val == None:
            self.val = 'public'
        super(AccessModifier, self).gen()



class StaticModifier(JustStrModifier):
    pass

class RefModifier(BaseNode):
    pass
    

class MemberFuncDecWithoutTerminator(BaseNode):
    def __init__(self, final, access, static, ref, id_, paramList):
        super(MemberFuncDecWithoutTerminator, self).__init__(id_)
        self.final = final
        self.access = access
        self.static = static
        self.ref = ref
        self.paramList = paramList

    def gen(self):
        self.final.gen()
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
    def __init__(self, access, static, ref, id_, init, terminator):
        super(DataMemberDef, self).__init__(id_, terminator)
        self.access = access
        self.static = static
        self.init = init
        self.ref = ref

    def gen(self):
        self.access.gen(True)
        self.static.gen()
        self.ref.gen()
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


class Yield(BaseNode):
    def __init__(self, exp1, exp2):
        super(Yield, self).__init__(exp1)
        self.exp2 = exp2
    def gen(self):
        append('yield')
        self.val and append(' ')
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
        #append('$')
        super(CommaList, self).gen()

class Operation(BaseNode):
    pass

class StrCat(BinaryOperationNode):
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

class BBit(BinaryOperationNode):
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
