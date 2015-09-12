'''PingPHP grammar file
'''
from .nodes import *
from .lexer import *
import logging

'''
grammar:

    Root :
         | Body

    Body : Line
         | Body Line

    Line : CodeBlock
         | Statement
         | Embeded
         | JustStrStatement

    Embeded : DOCCOMMENT
            | NATIVEPHP TERMINATOR
            | EMPTYLINE
            | INLINECOMMENT

    Statement : StatementWithoutTerminator Terminator

    StatementWithoutTerminator : Expression
                               | Namespace
                               | UseNamespace
                               | GlobalDec
                               | ConstDefWithoutTerminator
                               | StaticVarDef
                               | Declare


    StaticVarDef : STATIC INDENTIFIER InitModifier

    JustStrStatement: STATEMENT ArgList Terminator

    CodeBlock : If
              | Switch
              | For
              | While
              | DoWhile
              | Try
              | FuncDef
              | Class
              | Interface
              | Trait

    Expression : Value
               | Assign
               | Operation
               | Call
               | Lambda
               | AnonymousClass
               | ParentExp
               | AccessObj
               | Yield

    Block : INDENT Body OUTDENT


Value and Assign:
    InitModifier :
                 | AssignRightSide

    AssignRightSide : ASSIGN Expression

    Value : Varible
          | Literal

    Literal : SimpleLiteral
            | ArrayLiteral

    SimpleLiteral : NUMBER
                  | STRING

    ArrayLiteral : LBRACKET ArrayLiteralContentList RBRACKET

    ArrayLiteralContentList : ArrayLiteralContent
                            | ArrayLiteralContentList COMMA ArrayLiteralContent

    ArrayLiteralContent : Expression
                        | Expression COLON Expression

    Varible : NsContentName
            | NsContentName SCOPEOP INDENTIFIER
            | NsContentName SCOPEOP CLASS

    Assign : Expression AssignRightSide


Param and Arg
    ArgList :
            | Arg
            | ArgList COMMA Arg

    Arg : Expression ThreeDotModifier

    ParamList :
              | Param
              | ParamList COMMA Param

    Param : RefModifier INDENTIFIER ThreeDotModifier TypeModifier InitModifier

    TypeModifier : 
                 | COLON NsContentName

Call
    Call : Callable ArgList RPARENT

    Callable : NsContentName LPARENT
             | NsContentName SCOPEOP INDENTIFIER LPARENT
             | Expression LPARENT
             | Expression DOT INDENTIFIER LPARENT
             | Expression 
             | STATIC SCOPEOP INDENTIFIER LPARENT

Lambda
    Lambda : LAMBDA ParamList UseModifier COLON Terminator Block
    UseModifier : 
                | USE ParamList

Terminator
    Terminator : INLINECOMMENT
               | TERMINATOR

Namespace
    Namespace : NAMESPACE NsContentName

    UseNamespace : USE NsContentNameAsIdList

    DefOrConstModifier :
                       : DEF
                       | CONST

    NsContentName : INDENTIFIER
                  | NAMESPACEBEFORESLASH
                  | BACKSLASH INDENTIFIER
                  | NsContentName BACKSLASH INDENTIFIER

    NsContentNameList : NsContentName
                      | NsContentNameList COMMA NsContentName

    NsContentNameAsId : DefOrConstModifier NsContentName
                      | DefOrConstModifier NsContentName AS INDENTIFIER

    NsContentNameAsIdList : NsContentNameAsId
                          | NsContentNameAsIdList COMMA NsContentNameAsId
If
    If : IfBlock
       | IfBlock ELSE Block

    IfBlock : IF Expression COLON Terminator Block
            | IfBlock ELIF Expression COLON Terminator Block

Switch
    Switch : SWITCH Expression COLON Terminator SwitchContent

    SwitchContent : INDENT InSwitchDefList OUTDENT

    InSwitchDefList : InSwitchDef
                    | InSwitchDefList InSwitchDef

    InSwitchDef : Case
                | Embeded

    Case : CASE ArgList COLON Terminator Block
         | DEFAULT COLON Terminator Block

For
    For : FOR RefModifier INDENTIFIER IN Expression COLON Terminator Block
    For : FOR RefModifier INDENTIFIER COMMA RefModifier INDENTIFIER IN Expression COLON Terminator Block
 

While
    While : WHILE Expression COLON Terminator Block

DoWhile
    DoWhile : DO COLON Terminator Block WHILE Expression Terminator

    Declare : DECLARE LPARENT INDENTIFIER ASSIGN Expression RPARENT

Try
    Try : TRY COLON Terminator Block Catch
        | TRY COLON Terminator Block Catch FINALLY COLON Terminator Block

Catch : 
          | Catch CATCH LPARENT Varible COLON NsContentName RPARENT COLON Terminator Block

Class and Interface
    Class : AbstractModifier FinalModifier CLASS INDENTIFIER ExtendsModifier ImplementsModifier COLON Terminator ClassContent

    Trait : TRAIT INDENTIFIER COLON Terminator ClassContent

    FinalModifier : 
                  | FINAL

    AbstractModifier : 
                     | ABSTRACT

    ClassContent : INDENT InClassDefList OUTDENT

    InClassDefList : InClassDef
                   | InClassDefList InClassDef

    InClassDef : Embeded
               | JustStrStatement
               | DataMemberDef
               | ConstDef
               | MemberFuncDef
               | ABSTRACT MemberFuncDec
               | UseTrait

    UseTrait : UseNamespace Terminator
             | UseNamespace COLON Terminator UseTraitContent

    UseTraitContent : INDENT InUseTraitDefList OUTDENT

    InUseTraitDefList : InUseTraitDef
                      | InUseTraitDefList InUseTraitDef

    InUseTraitDef : Varible INSTEADOF NsContentName Terminator
                  | Varible AS AccessModifier NsContentName Terminator
                  | Varible AS AccessModifier Terminator

    Interface : INTERFACE INDENTIFIER ExtendsModifier COLON Terminator InterfaceContent

    InterfaceContent : INDENT InterfaceDefList OUTDENT

    InterfaceDefList : InterfaceDef
                     | InterfaceDefList InterfaceDef

    InterfaceDef : Embeded
                 | JustStrStatement
                 | ConstDef
                 | MemberFuncDec

    ExtendsModifier :
                    | EXTENDS NsContentNameList

    ImplementsModifier :
                       | IMPLEMENTS NsContentNameList

    AccessModifier :
                   | PUBLIC
                   | PRIVATE
                   | PROTECTED

    StaticModifier :
                   | STATIC

    RefModifier :
                | ANDOP

    MemberFuncDecWithoutTerminator : FinalModifier AccessModifier StaticModifier RefModifier INDENTIFIER LPARENT ParamList RPARENT

    MemberFuncDec : MemberFuncDecWithoutTerminator ReturnTypeModifierForDec Terminator

    ReturnTypeModifierForDec : 
                             | COLON NsContentName

    MemberFuncDef : MemberFuncDecWithoutTerminator COLON ReturnTypeModifier Terminator Block

    DataMemberDef : FinalModifier AccessModifier StaticModifier RefModifier INDENTIFIER InitModifier Terminator

FuncDef

    ReturnTypeModifier : 
                       | NsContentName

    FuncDef : DEF RefModifier INDENTIFIER LPARENT ParamList RPARENT COLON ReturnTypeModifier Terminator Block

    ConstDef : ConstDefWithoutTerminator Terminator

    ConstDefWithoutTerminator : CONST INDENTIFIER AssignRightSide

    Yield : YIELD
          | YIELD Expression
          | YIELD Expression COMMA Expression

    GlobalDec : GLOBAL GlobalVaribleList

    GlobalVaribleList : INDENTIFIER
                      | GlobalVaribleList COMMA INDENTIFIER

Operation
    Operation : UMath
              | BMath
              | NewOrClone
              | Compare
              | Cast
              | InDecrement
              | UBit
              | BBit
              | ULogic
              | BLogic
              | InstanceOf
              | Ternary
              | At
              | Ref
              | StrCat

    StrCat : Expression STRCAT Expression

    BMath : Expression MATH1 Expression
          | Expression MATH2 Expression

    UMath : MATH2 Expression %prec UMATH

    NewOrClone : NEW NsContentName LPARENT ArgList RPARENT
               | NEW Varible
               | CLONE Varible
               | NEW STRING
               | CLONE STRING
               | NEW STATIC LPARENT ArgList RPARENT

    Compare : Expression COMPARE Expression

    Cast : CAST Expression

    InDecrement : INDECREMENT Expression
                | Expression INDECREMENT

    UBit : BITNOT Expression

    BBit : Expression SHIFT Expression
         | Expression ANDOP Expression
         | Expression BITOR Expression
         | Expression BITXOR Expression

    InstanceOf : Expression INSTANCEOF NsContentName

    ULogic : NOT Expression
    BLogic : Expression AND Expression
           | Expression OR Expression

    Ternary : Expression IF Expression ELSE Expression

    At : AT Expression

    Ref : ANDOP Expression %prec REFOP

'''

start = 'Root'

precedence = [
    ('nonassoc', 'CLONE', 'NEW'),
    ('left', 'LBRACKET'),
    ('right', 'EXPONENT'),
    ('right', 'INDECREMENT', 'BITNOT', 'CAST', 'AT'),
    ('nonassoc', 'INSTANCEOF'),
    ('right', 'NOT'),
    ('right', 'UMATH'),
    ('left', 'MATH1'),
    ('left', 'MATH2', 'STRCAT'),
    ('left', 'SHIFT'),
    ('nonassoc', 'COMPARE'),
    ('left', 'ANDOP'),
    ('left', 'REFOP'),
    ('left', 'BITXOR'),
    ('left', 'BITOR'),
    ('left', 'AND'),
    ('left', 'OR'),
    ('left', 'IF', 'ELSE'),
    ('right', 'ASSIGN'),
    ('left', 'COMMA')
]

precedence.reverse()


def p_Root(p):
    '''
    Root :
         | Body
    '''
    if len(p) < 2:
        p[0] = Root(None)
    else:
        p[0] = Root(p[1])


def p_Body(p):
    '''
    Body : Line
         | Body Line
    '''
    if not isinstance(p[1], Body):
        p[0] = Body(None, p[1])
    else:
        p[0] = Body(p[1], p[2])


def p_Line(p):
    '''
    Line : CodeBlock
         | Statement
         | Embeded
         | JustStrStatement
    '''
    p[0] = Line(p[1])


def p_Embeded(p):
    '''
    Embeded : DOCCOMMENT
            | NATIVEPHP TERMINATOR
            | EMPTYLINE
            | INLINECOMMENT

    '''
    p[0] = Embeded(p[1])


def p_Statement(p):
    '''
    Statement : StatementWithoutTerminator Terminator
    '''
    if len(p) < 3:
        term = Terminator('')
    else:
        term = p[2]
    p[0] = Statement(p[1], term)


def p_StatementWithoutTerminator(p):
    '''
    StatementWithoutTerminator : Expression
                               | Namespace
                               | UseNamespace
                               | GlobalDec
                               | ConstDefWithoutTerminator
                               | StaticVarDef
                               | Declare
    '''
    p[0] = StatementWithoutTerminator(p[1])


def p_StaticVarDef(p):
    '''
    StaticVarDef : STATIC INDENTIFIER InitModifier
    '''
    p[0] = StaticVarDef(p[2], p[3])


def p_JustStrStatement(p):
    '''
    JustStrStatement : STATEMENT ArgList Terminator
    '''
    p[0] = JustStrStatement(p[1], p[2], p[3])


def p_CodeBlock(p):
    '''
    CodeBlock : If
              | Switch
              | For
              | While
              | DoWhile
              | Try
              | FuncDef
              | Class
              | Interface
              | Trait
    '''
    p[0] = CodeBlock(p[1])


def p_Expression(p):
    '''
    Expression : Value
               | Assign
               | Operation
               | Call
               | Lambda
               | AnonymousClass
               | AccessObj
               | ParentExp
               | Yield
    '''
    p[0] = Expression(p[1])

def p_ParentExp(p):
    '''
    ParentExp : LPARENT Expression RPARENT
    '''
    p[0] = ParentExp(p[2])

def p_AccessObj(p):
    '''
    AccessObj : Expression DOT INDENTIFIER
              | Expression LBRACKET Expression RBRACKET
              | Expression LBRACKET RBRACKET
    '''
    if len(p) <= 4:
        if p[2] == '.':
            p[0] = AccessObj(p[1], p[3], None)
        else:
            p[0] = AccessObj(p[1], None, None)
    else:
        p[0] = AccessObj(p[1], None, p[3])


def p_Block(p):
    '''
    Block : INDENT Body OUTDENT
    '''
    p[0] = Block(p[2])


def p_InitModifier(p):
    '''
    InitModifier :
                 | AssignRightSide
    '''
    if len(p) < 2:
        p[0] = InitModifier(None)
    else:
        p[0] = InitModifier(p[1])


def p_AssignRightSide(p):
    '''
    AssignRightSide : ASSIGN Expression
    '''
    p[0] = AssignRightSide(p[1], p[2])


def p_Value(p):
    '''
    Value : Varible
          | Literal
    '''
    p[0] = Value(p[1])


def p_Literal(p):
    '''
    Literal : SimpleLiteral
            | ArrayLiteral
    '''
    p[0] = Literal(p[1])


def p_SimpleLiteral(p):
    '''
    SimpleLiteral : NUMBER
                  | STRING
                  | EXEC
    '''
    p[0] = SimpleLiteral(p[1])


def p_ArrayLiteral(p):
    '''
    ArrayLiteral : LBRACKET ArrayLiteralContentList RBRACKET
    '''
    p[0] = ArrayLiteral(p[2])


def p_ArrayLiteralContentList(p):
    '''
    ArrayLiteralContentList : ArrayLiteralContent
                            | ArrayLiteralContentList COMMA ArrayLiteralContent
    '''
    if len(p) < 3:
        p[0] = ArrayLiteralContentList(None, p[1])
    else:
        p[0] = ArrayLiteralContentList(p[1], p[3])


def p_ArrayLiteralContent(p):
    '''
    ArrayLiteralContent : Expression
    ArrayLiteralContent : Expression COLON Expression
    '''
    if len(p) < 3:
        p[0] = ArrayLiteralContent(None, p[1])
    else:
        p[0] = ArrayLiteralContent(p[1], p[3])


def p_Varible(p):
    '''
    Varible : NsContentName
            | NsContentName SCOPEOP INDENTIFIER
            | NsContentName SCOPEOP CLASS
            | STATIC SCOPEOP INDENTIFIER
    '''
    if len(p) < 3:
        p[0] = Varible(None, p[1])
    else:
        p[0] = Varible(p[1], p[3])


def p_Assign(p):
    '''
    Assign : Expression AssignRightSide
    '''
    p[0] = Assign(p[1], p[2])


def p_ArgList(p):
    '''
    ArgList :
            | Arg
            | ArgList COMMA Arg
    '''
    if len(p) == 1:
        p[0] = ArgList(None, None)
    elif len(p) == 2:
        p[0] = ArgList(None, p[1])
    else:
        p[0] = ArgList(p[1], p[3])


def p_Arg(p):
    '''
    Arg : Expression ThreeDotModifier
    '''
    if len(p) <= 2:
        p[0] = Arg(p[1], None)
    else:
        p[0] = Arg(p[1], p[2])


def p_ParamList(p):
    '''
    ParamList :
              | Param
              | ParamList COMMA Param
    '''
    if len(p) == 1:
        p[0] = ParamList(None, None)
    elif len(p) == 2:
        p[0] = ParamList(None, p[1])
    else:
        p[0] = ParamList(p[1], p[3])

def p_ThreeDotModifier(p):
    '''
    ThreeDotModifier :
                     | THREEDOT
    '''
    if len(p) <= 1:
        p[0] = ThreeDotModifier(None)
    else:
        p[0] = ThreeDotModifier(p[1])


def p_Param(p):
    '''
    Param : RefModifier INDENTIFIER ThreeDotModifier TypeModifier InitModifier
    '''
    p[0] = Param(p[1], p[2], p[3], p[4], p[5])

def p_TypeModifier(p):
    '''
    TypeModifier : 
                 | COLON NsContentName
    '''
    if len(p) <= 1:
        p[0] = TypeModifier(None)
    else:
        p[0] = TypeModifier(p[2])


def p_Call(p):
    '''
    Call : Callable ArgList RPARENT
    '''
    p[0] = Call(p[1], p[2])


def p_Callable(p):
    '''
    Callable : NsContentName LPARENT
             | NsContentName SCOPEOP INDENTIFIER LPARENT
             | Expression LPARENT
             | STATIC SCOPEOP INDENTIFIER LPARENT
    '''
    if len(p) <= 3:
        p[0] = Callable(p[1], None)
    else:
        p[0] = Callable(p[1], p[3])

def p_Lambda(p):
    '''
    Lambda : LAMBDA LPARENT ParamList RPARENT UseModifier COLON Terminator Block
    '''
    p[0] = Lambda(p[3], p[5], p[7], p[8])

def p_UseModifier(p):
    '''
    UseModifier : 
                | USE LPARENT ParamList RPARENT
    '''
    if len(p) <= 1:
        p[0] = UseModifier(None)
    else:
        p[0] = UseModifier(p[3])


def p_Terminator(p):
    '''
    Terminator : INLINECOMMENT
               | TERMINATOR
    '''
    p[0] = Terminator(p[1])


def p_Namespace(p):
    '''
    Namespace : NAMESPACE NsContentName
    '''
    p[0] = Namespace(p[2])


def p_UseNamespace(p):
    '''
    UseNamespace : USE NsContentNameAsIdList

    '''
    p[0] = UseNamespace(p[2])

def p_DefOrConstModifier(p):
    '''
    DefOrConstModifier :
                       | DEF
                       | CONST
    '''
    if len(p) <= 1:
        p[0] = DefOrConstModifier(None)
    else:
        p[0] = DefOrConstModifier(p[1])


def p_NsContentName(p):
    '''
    NsContentName : INDENTIFIER
                  | NAMESPACEBEFORESLASH
                  | SLASH INDENTIFIER
                  | NsContentName SLASH INDENTIFIER
    '''
    if len(p) == 2:
        p[0] = NsContentName(None, p[1])
    elif len(p) == 3:
        p[0] = NsContentName(None, p[1] + p[2])
    else:
        p[0] = NsContentName(p[1], p[2] + p[3])


def p_NsContentNameList(p):
    '''
    NsContentNameList : NsContentName
                      | NsContentNameList COMMA NsContentName
    '''
    if len(p) == 2:
        p[0] = NsContentNameList(None, p[1])
    else:
        p[0] = NsContentNameList(p[1], p[3])


def p_NsContentNameAsId(p):
    '''
    NsContentNameAsId : DefOrConstModifier NsContentName
                      | DefOrConstModifier NsContentName AS INDENTIFIER
    '''
    if len(p) <= 3:
        p[0] = NsContentNameAsId(p[1], p[2], None)
    else:
        p[0] = NsContentNameAsId(p[1], p[2], p[4])


def p_NsContentNameAsIdList(p):
    '''
    NsContentNameAsIdList : NsContentNameAsId
                          | NsContentNameAsIdList COMMA NsContentNameAsId
    '''
    if len(p) == 2:
        p[0] = NsContentNameAsIdList(None, p[1])
    else:
        p[0] = NsContentNameAsIdList(p[1], p[3])


def p_If(p):
    '''
    If : IfBlock
       | IfBlock ELSE COLON Terminator Block
    '''
    if len(p) == 2:
        p[0] = If(p[1], None, None)
    else:
        p[0] = If(p[1], p[5], p[4])


def p_IfBlock(p):
    '''
    IfBlock : IF Expression COLON Terminator Block
            | IfBlock ELIF Expression COLON Terminator Block
    '''
    if isinstance(p[1], basestring):
        p[0] = IfBlock(None, p[2], p[4], p[5])
    else:
        p[0] = IfBlock(p[1], p[3], p[5], p[6])


def p_Switch(p):
    '''
    Switch : SWITCH Expression COLON Terminator SwitchContent
    '''
    p[0] = Switch(p[2], p[4], p[5])


def p_SwitchContent(p):
    '''
    SwitchContent : INDENT InSwitchDefList OUTDENT
    '''
    p[0] = SwitchContent(p[2])


def p_InSwitchDefList(p):
    '''
    InSwitchDefList : InSwitchDef
                    | InSwitchDefList InSwitchDef
   '''
    if len(p) <= 2:
        p[0] = InSwitchDefList(None, p[1])
    else:
        p[0] = InSwitchDefList(p[1], p[2])

def p_InSwitchDef(p):
    '''
    InSwitchDef : Case
                | Embeded
    '''
    p[0] = InSwitchDef(p[1])

def p_Case(p):
    '''
    Case : CASE ArgList COLON Terminator Block
         | DEFAULT COLON Terminator Block
    '''
    if p[1] == 'case':
        p[0] = Case(p[1], p[2], p[4], p[5])
    else:
        p[0] = Case(p[1], None, p[3], p[4])


def p_For(p):
    '''
    For : FOR Expression IN Expression COLON Terminator Block
    For : FOR Expression COMMA Expression IN Expression COLON Terminator Block
    '''
    if len(p) <= 8:
        p[0] = For(p[2], None, p[4], p[6], p[7])
    else:
        p[0] = For(p[2], p[4], p[6], p[8], p[9])

def p_While(p):
    '''
    While : WHILE Expression COLON Terminator Block
    '''
    p[0] = While(p[2], p[4], p[5])


def p_DoWhile(p):
    '''
    DoWhile : DO COLON Terminator Block CommentOrEmptyLineList WHILE Expression Terminator
    '''
    p[0] = DoWhile(p[3], p[4], p[5], p[7], p[8])

def p_CommentOrEmptyLineList(p):
    '''
    CommentOrEmptyLineList :
                           | CommentOrEmptyLine
                           | CommentOrEmptyLineList CommentOrEmptyLine 
    '''
    if len(p) <= 1:
        p[0] = CommentOrEmptyLineList(None, None)
    elif len(p) <= 2:
        p[0] = CommentOrEmptyLineList(None, p[1])
    else:
        p[0] = CommentOrEmptyLineList(p[1], p[2])

def p_CommentOrEmptyLine(p):
    '''
    CommentOrEmptyLine : EMPTYLINE
                       | DOCCOMMENT
                       | INLINECOMMENT
    '''
    p[0] = CommentOrEmptyLine(p[1])

def p_Declare(p):
    '''
    Declare : DECLARE LPARENT INDENTIFIER ASSIGN Expression RPARENT
    '''
    p[0] = Declare(p[3], p[5])

def p_Try(p):
    '''
    Try : TRY COLON Terminator Block Catch
        | TRY COLON Terminator Block Catch FINALLY COLON Terminator Block
    '''
    if len(p) <= 6:
        p[0] = Try(p[3], p[4], p[5], None, None)
    else:
        p[0] = Try(p[3], p[4], p[5], p[8], p[9])

def p_Catch(p):
    '''
    Catch : 
          | Catch CATCH LPARENT Varible COLON NsContentName RPARENT COLON Terminator Block
    '''
    if len(p) <= 1:
        p[0] = Catch(None, None, None, None, None)
    else:
        p[0] = Catch(p[1], p[4], p[6], p[9], p[10])


def p_Class(p):
    '''
    Class : AbstractModifier FinalModifier CLASS INDENTIFIER ExtendsModifier ImplementsModifier COLON Terminator ClassContent
    '''
    p[0] = Class(p[1], p[2], p[4], p[5], p[6], p[8], p[9])

def p_AnonymousClass(p):
    '''
    AnonymousClass : NEW CLASS LPARENT ArgList RPARENT ExtendsModifier ImplementsModifier COLON Terminator ClassContent
    '''
    #p[0] = Class(p[1], p[2], p[4], p[5], p[6], p[8], p[9])




def p_Trait(p):
    '''
    Trait : TRAIT INDENTIFIER COLON Terminator ClassContent
    '''
    p[0] = Trait(p[2], p[4], p[5])


def p_FinalModifier(p):
    '''
    FinalModifier : 
                  | FINAL
    '''
    if len(p)<= 1:
        p[0] = FinalModifier(None)
    else:
        p[0] = FinalModifier(p[1])

def p_AbstractModifier(p):
    '''
    AbstractModifier : 
                     | ABSTRACT
    '''
    if len(p)<=1:
        p[0] = AbstractModifier(None)
    else:
        p[0] = AbstractModifier(None)


def p_ClassContent(p):
    '''
    ClassContent : INDENT InClassDefList OUTDENT
    '''
    p[0] = ClassContent(p[2])


def p_InClassDefList(p):
    '''
    InClassDefList : InClassDef
                   | InClassDefList InClassDef
    '''
    if len(p) < 3:
        p[0] = InClassDefList(None, p[1])
    else:
        p[0] = InClassDefList(p[1], p[2])


def p_InClassDef(p):
    '''
    InClassDef : Embeded
               | JustStrStatement
               | DataMemberDef
               | ConstDef
               | MemberFuncDef
               | ABSTRACT MemberFuncDec
               | UseTrait
    '''
    if len(p) <= 2:
        p[0] = InClassDef(None, p[1])
    else:
        p[0] = InClassDef(p[1], p[2])

def p_UseTrait(p):
    '''
    UseTrait : UseNamespace Terminator
             | UseNamespace COLON Terminator UseTraitContent
    '''
    if len(p) <= 3:
        p[0] = UseTrait(p[1], p[2], None)
    else:
        p[0] = UseTrait(p[1], p[3], p[4])

def p_UseTraitContent(p):
    '''
    UseTraitContent : INDENT InUseTraitDefList OUTDENT
    '''
    p[0] = UseTraitContent(p[2])

def p_InUseTraitDefList(p):
    '''
    InUseTraitDefList : InUseTraitDef
                      | InUseTraitDefList InUseTraitDef
    '''
    if len(p) <= 2:
        p[0] = InUseTraitDefList(None, p[1])
    else:
        p[0] = InUseTraitDefList(p[1], p[2])

def p_InUseTraitDef(p):
    '''
    InUseTraitDef : Varible INSTEADOF NsContentName Terminator
                  | Varible AS AccessModifier Terminator
                  | Varible AS AccessModifier NsContentName Terminator
    '''
    if p[2] == 'insteadof':
        p[0] = InUseTraitDef(p[1], p[2], None, p[3], p[4])
    elif len(p) <= 5:
        p[0] = InUseTraitDef(p[1], p[2], p[3], None, p[4])
    else:
        p[0] = InUseTraitDef(p[1], p[2], p[3], p[4], p[5])


def p_Interface(p):
    '''
    Interface : INTERFACE INDENTIFIER ExtendsModifier COLON Terminator InterfaceContent
    '''
    p[0] = Interface(p[2], p[3], p[5], p[6])


def p_InterfaceContent(p):
    '''
    InterfaceContent : INDENT InterfaceDefList OUTDENT
    '''
    p[0] = InterfaceContent(p[2])


def p_InterfaceDefList(p):
    '''
    InterfaceDefList : InterfaceDef
                     | InterfaceDefList InterfaceDef
    '''
    if len(p) < 3:
        p[0] = InterfaceDefList(None, p[1])
    else:
        p[0] = InterfaceDefList(p[1], p[2])


def p_InterfaceDef(p):
    '''
    InterfaceDef : Embeded
                 | JustStrStatement
                 | ConstDef
                 | MemberFuncDec
    '''
    p[0] = InterfaceDef(p[1])


def p_ExtendsModifier(p):
    '''
    ExtendsModifier :
                    | EXTENDS NsContentNameList
    '''
    if len(p) > 1:
        p[0] = ExtendsModifier(p[2])
    else:
        p[0] = ExtendsModifier(None)


def p_ImplementsModifier(p):
    '''
    ImplementsModifier :
                       | IMPLEMENTS NsContentNameList
    '''
    if len(p) > 1:
        p[0] = ImplementsModifier(p[2])
    else:
        p[0] = ImplementsModifier(None)


def p_AccessModifier(p):
    '''
    AccessModifier :
                   | PUBLIC
                   | PRIVATE
                   | PROTECTED
    '''
    if len(p) > 1:
        p[0] = AccessModifier(p[1])
    else:
        p[0] = AccessModifier(None)


def p_StaticModifier(p):
    '''
    StaticModifier :
                   | STATIC
    '''
    if len(p) > 1:
        p[0] = StaticModifier(p[1])
    else:
        p[0] = StaticModifier(None)

def p_RefModifier(p):
    '''
    RefModifier : 
                | ANDOP
    '''
    if len(p)<2:
        p[0] = RefModifier(None)
    else:
        p[0] = RefModifier(p[1])



def p_MemberFuncDecWithoutTerminator(p):
    '''
    MemberFuncDecWithoutTerminator : FinalModifier AccessModifier StaticModifier RefModifier INDENTIFIER LPARENT ParamList RPARENT
    '''
    p[0] = MemberFuncDecWithoutTerminator(p[1], p[2], p[3], p[4], p[5], p[7])


def p_MemberFuncDec(p):
    '''
    MemberFuncDec : MemberFuncDecWithoutTerminator ReturnTypeModifierForDec Terminator
    '''
    p[0] = MemberFuncDec(p[1], p[2], p[3])

def p_ReturnTypeModifierForDec(p):
    '''
    ReturnTypeModifierForDec : 
                             | COLON NsContentName
    '''
    if len(p) <= 1:
        p[0] = ReturnTypeModifierForDec(None)
    else:
        p[0] = ReturnTypeModifierForDec(p[2])


def p_MemberFuncDef(p):
    '''
    MemberFuncDef : MemberFuncDecWithoutTerminator COLON ReturnTypeModifier Terminator Block
    '''
    p[0] = MemberFuncDef(p[1], p[3], p[4], p[5])


def p_DataMemberDef(p):
    '''
    DataMemberDef : FinalModifier AccessModifier StaticModifier RefModifier INDENTIFIER InitModifier Terminator
    '''
    if p[1].val != None:
        raise SyntaxError 
    p[0] = DataMemberDef(p[2], p[3], p[4], p[5], p[6], p[7])

def p_ReturnTypeModifier(p):
    '''
    ReturnTypeModifier : 
                       | NsContentName
    '''
    if len(p) <= 1:
        p[0] = ReturnTypeModifier(None)
    else:
        p[0] = ReturnTypeModifier(p[1])

def p_FuncDef(p):
    '''
    FuncDef : DEF RefModifier INDENTIFIER LPARENT ParamList RPARENT COLON ReturnTypeModifier Terminator Block
    '''
    p[0] = FuncDef(p[2], p[3], p[5], p[8], p[9], p[10])


def p_ConstDefWithoutTerminator(p):
    '''
    ConstDefWithoutTerminator : CONST INDENTIFIER AssignRightSide
    '''
    p[0] = ConstDefWithoutTerminator(p[2], p[3])


def p_ConstDef(p):
    '''
    ConstDef : ConstDefWithoutTerminator Terminator
    '''
    p[0] = ConstDef(p[1], p[2])



def p_Yield(p):
    '''
    Yield : YIELD
          | YIELD Expression
          | YIELD Expression COMMA Expression
    '''
    if len(p) == 2:
        p[0] = Yield(None, None)
    elif len(p) == 3:
        p[0] = Yield(p[2], None)
    else:
        p[0] = Yield(p[2], p[4])


def p_GlobalDec(p):
    '''
    GlobalDec : GLOBAL GlobalVaribleList
    '''
    p[0] = GlobalDec(p[2])


def p_GlobalVaribleList(p):
    '''
    GlobalVaribleList : Varible 
                      | GlobalVaribleList COMMA Varible
    '''
    if len(p) > 2:
        p[0] = GlobalVaribleList(p[1], p[3])
    else:
        p[0] = GlobalVaribleList(None, p[1])


def p_Operation(p):
    '''
    Operation : UMath
              | BMath
              | NewOrClone
              | Compare
              | Cast
              | InDecrement
              | UBit
              | BBit
              | ULogic
              | BLogic
              | InstanceOf
              | Ternary
              | At
              | Ref
              | StrCat
    '''
    p[0] = Operation(p[1])

def p_StrCat(p):
    '''
    StrCat : Expression STRCAT Expression
    '''
    p[0] = StrCat(p[1], p[2], p[3])



def p_BMath(p):
    '''
    BMath : Expression MATH1 Expression
          | Expression MATH2 Expression
          | Expression EXPONENT Expression
    '''
    p[0] = BMath(p[1], p[2], p[3])

def p_UMath(p):
    '''
    UMath : MATH2 Expression %prec UMATH
    '''
    p[0] = UMath(p[1], p[2])


def p_Cast(p):
    '''
    Cast : CAST Expression
    '''
    p[0] = Cast(p[1], p[2])


def p_InDecrement(p):
    '''
    InDecrement : INDECREMENT Expression
                | Expression INDECREMENT
    '''
    from .helper import isString
    if isString(p[1]):
        p[0] = InDecrement(p[1], p[2], False)
    else:
        p[0] = InDecrement(p[2], p[1], True)

def p_UBit(p):
    '''
    UBit : BITNOT Expression
    '''
    p[0] =  UBit(p[1], p[2])

def p_BBit(p):
    '''
    BBit : Expression SHIFT Expression
         | Expression ANDOP Expression
         | Expression BITOR Expression
         | Expression BITXOR Expression
    '''
    p[0] = BBit(p[1], p[2], p[3])

def p_InstanceOf(p):
    '''
    InstanceOf : Expression INSTANCEOF NsContentName
    '''
    p[0] = InstanceOf(p[1], p[2], p[3])

def p_ULogic(p):
    '''
    ULogic : NOT Expression
    '''
    p[0] = ULogic(p[1], p[2])

def p_BLogic(p):
    '''
    BLogic : Expression AND Expression
           | Expression OR Expression
    '''
    p[0] = BLogic(p[1], p[2], p[3])

def p_NewOrClone(p):
    '''
    NewOrClone : NEW NsContentName LPARENT ArgList RPARENT
               | NEW STATIC LPARENT ArgList RPARENT
               | NEW Varible
               | CLONE Varible
               | NEW STRING
               | CLONE STRING
    '''
    if len(p) > 3:
        p[0] = NewOrClone(p[1], p[2], p[4], None)
    else:
        p[0] = NewOrClone(p[1], None, None, p[2])


def p_Compare(p):
    '''
    Compare : Expression COMPARE Expression
    '''
    p[0] = Compare(p[1], p[2], p[3])


def p_Ternary(p):
    '''
    Ternary : Expression IF Expression ELSE Expression
    '''
    p[0] = Ternary(p[3], p[1], p[5])


def p_At(p):
    '''
    At : AT Expression
    '''
    p[0] = At(p[1],p[2])

def p_Ref(p):
    '''
    Ref : ANDOP Expression %prec REFOP
    '''
    p[0] = Ref(p[1],p[2])

def p_error(p):
    from .helper import errorMsg
    errorMsg("Grammar", p)
