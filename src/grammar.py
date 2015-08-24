'''PingPHP grammar file
'''
from ply import yacc
from lexer import tokens
from nodes import *
'''
grammar:
	
	Root : 
	     | Body

	Body : Line
	     | Body Line

	Line : CodeBlock
	     | Statement
	     | Embeded

	Embeded : DOCCOMMENT
		| NATIVEPHP
		| EMPTYLINE
		| INLINECOMMENT

	Statement : StatementWithoutTerminator Terminator

	StatementWithoutTerminator : Expression
		  		   | STATEMENT
				   | Return
				   | Namespace
				   | UseNamespace
				   | GlobalDec
				   | ConstDefWithoutTerminator

	JustStrStatementWithTerminator : STATEMENT Terminator

	CodeBlock : If
		  | For
		  | FuncDef
		  | Class
		  | Interface

	Expression : Value
		   | Assign 
		   | Operation
		   | Call

	Block : INDENT Body OUTDENT

	
Value and Assign:
	InitModifier : 
		     | AssignRightSide

	AssignRightSide : ASSIGN Expression

	Value : Assignable
	      | Literal
	
	Literal : SimpleLiteral
		| ArrayLiteral

	SimpleLiteral : NUMBER
		      | STRING

	ArrayLiteral : LBRACKET ArrayLiteralContentList RBRACKET

	ArrayLiteralContentList : ArrayLiteralContent
				| ArrayLiteralContentList COMMA ArrayLiteralContent
	ArrayLiteralContent : Expression
			    | SimpleLiteral COLON Expression

	Varible : NsContentName
		| NsContentName SCOPEOP INDENTIFIER

	Assignable : Varible
		   | Assignable LBRACKET Expression RBRACKET
		   | Assignable DOT INDENTIFIER

	Assign : Assignable AssignRightSide


Param and Arg	
	ArgList : 
		| Arg
		| ArgList COMMA Arg

	Arg : Expression

	ParamList : 
		  | Param
		  | ParamList COMMA Param

	Param : INDENTIFIER InitModifier

Call
	Call : Callable ArgList RPARENT

	Callable : NsContentName LPARENT 
		 | Expression LPARENT 
	
Terminator
	Terminator : INLINECOMMENT
		   | TERMINATOR

Namespace
	Namespace : NAMESPACE NsContentName 
	UseNamespace : USE NsContentNameAsIdList 

	NsContentName : INDENTIFIER
		      | BACKSLASH INDENTIFIER
		      | NsContentName BACKSLASH INDENTIFIER

	NsContentNameList : NsContentName
			  | NsContentNameList COMMA NsContentName

	NsContentNameAsId : NsContentName
			  | NsContentName AS INDENTIFIER
	NsContentNameAsIdList : NsContentNameAsId
			      | NsContentNameAsIdList COMMA NsContentNameAsId
If
	If : IfBlock
	   | IfBlock ELSE Block

	IfBlock : IF Expression COLON Terminator Block
	        | IfBlock ELIF Expression COLON Terminator Block

For
	For : FOR INDENTIFIER IN Expression COLON Terminator Block

Class and Interface
	Class : CLASS INDENTIFIER ExtendsModifier ImplementsModifier COLON Terminator ClassContent
	
	ClassContent : INDENT InClassDefList OUTDENT
	
	InClassDefList : InClassDef
		       | InClassDefList InClassDef

	InClassDef : Embeded
		   | JustStrStatementWithTerminator
		   | DataMemberDef
		   | ConstDef
		   | MemberFuncDef

	Interface : INTERFACE INDENTIFIER ExtendsModifier COLON Terminator InterfaceContent
	
	InterfaceContent : INDENT InterfaceDefList OUTDENT

	InterfaceDefList : InterfaceDef
			 | InterfaceDefList InterfaceDef
	
	InterfaceDef : Embeded
		     | JustStrStatementWithTerminator
		     | ConstDef
		     | MemberFuncDec

	ExtendsModifier : 
			| EXTENDS NsContentName

	ImplementsModifier : 
			   | IMPLEMENTS NsContentNameList 

	AccessModifier : 
		       | PUBLIC
		       | PRIVATE
		       | PROTECTED

	StaticModifier : 
		       | STATIC

	MemberFuncDecWithoutTerminator: AccessModifier StaticModifier INDENTIFIER LPARENT ParamList RPARENT

	MemberFuncDec : MemberFuncDecWithoutTerminator Terminator

	MemberFuncDef : MemberFuncDecWithoutTerminator COLON Terminator Block


	DataMemberDef : AccessModifier StaticModifier INDENTIFIER InitModifier Terminator

FuncDef
	FuncDef : DEF INDENTIFIER LPARENT ParamList RPARENT COLON Terminator Block

	ConstDef : ConstDefWithoutTerminator Terminator

	ConstDefWithoutTerminator : CONST INDENTIFIER AssignRightSide

	Return : RETURN Expression 
	       | RETURN 

	GlobalDec : GLOBAL GlobalVaribleList

	GlobalVaribleList : INDENTIFIER
			  | GlobalVaribleList COMMA INDENTIFIER

Operation
	Operation : Math
		  | New
		  | Compare

	Math : Expression PLUS Expression
	New : NEW NsContentName LPARENT ArgList RPARENT
	    | NEW Varible
	Compare : Expression EQ Expression


'''
start = 'Root'

precedence = (  
    ('left','PLUS'),  
    ('nonassoc','EQ'),  
    )  

def p_Root(p):
	'''
	Root : 
	     | Body
	'''
	if len(p)<2:
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
	'''
	p[0] = Line(p[1])

def p_Embeded(p):
	'''
	Embeded : DOCCOMMENT 
		| NATIVEPHP
		| EMPTYLINE
		| INLINECOMMENT

	'''
	p[0] = Embeded(p[1])

def p_Statement(p):
	'''
	Statement : StatementWithoutTerminator Terminator
	'''
	p[0] = Statement(p[1], p[2])

def p_StatementWithoutTerminator(p):
	'''
	StatementWithoutTerminator : Expression
		  		   | STATEMENT
				   | Return
				   | Namespace
				   | UseNamespace
				   | GlobalDec
				   | ConstDefWithoutTerminator
	'''
	p[0] = StatementWithoutTerminator(p[1])

def p_JustStrStatementWithTerminator(p):
	'''
	JustStrStatementWithTerminator : STATEMENT Terminator
	'''
	if p[1] == 'PASS':
		p[1] = ''
	p[0] = JustStrStatementWithTerminator(p[1],p[2])

def p_CodeBlock(p):
	'''
	CodeBlock : If
		  | For
		  | FuncDef
		  | Class
		  | Interface
	'''
	p[0] = CodeBlock(p[1])

def p_Expression(p):
	'''
	Expression : Value
		   | Assign 
		   | Operation
		   | Call
	'''
	p[0] = Expression(p[1])

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
	if len(p)<2:
		p[0] = InitModifier(None)
	else:
		p[0] = InitModifier(p[1])

def p_AssignRightSide(p):
	'''
	AssignRightSide : ASSIGN Expression
	'''
	p[0] = AssignRightSide(p[2])

def p_Value(p):
	'''
	Value : Assignable
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
	if len(p)<3:
		p[0] = ArrayLiteralContentList(None, p[1])
	else:
		p[0] = ArrayLiteralContentList(p[1], p[3])

def p_ArrayLiteralContent(p):
	'''
	ArrayLiteralContent : Expression
	ArrayLiteralContent : SimpleLiteral COLON Expression
	'''
	if len(p)<3:
		p[0] = ArrayLiteralContent(None, p[1])
	else:
		p[0] = ArrayLiteralContent(p[1], p[3])

def p_Varible(p):
	'''
	Varible : NsContentName 
		| NsContentName SCOPEOP INDENTIFIER
	'''
	if len(p)<3:
		p[0] = Varible(None, p[1])
	else:
		p[0] = Varible(p[1],p[3])

def p_Assignable(p):
	'''
	Assignable : Varible
		   | Assignable LBRACKET Expression RBRACKET
		   | Assignable DOT INDENTIFIER
	'''
	if len(p)==2:
		p[0] = Assignable(p[1], None, None)
	elif len(p)==5:
		p[0] = Assignable(p[1], p[3], None)
	else:
		p[0] = Assignable(p[1], None, p[3])

def p_Assign(p):
	'''
	Assign : Assignable AssignRightSide
	'''
	p[0] = Assign(p[1], p[2])

def p_ArgList(p):
	'''
	ArgList : 
		| Arg
		| ArgList COMMA Arg
	'''
	if len(p)==1:
		p[0] = ArgList(None, None)
	elif len(p)==2:
		p[0] = ArgList(None, p[1])
	else:
		p[0] = ArgList(p[1], p[2])
		
def p_Arg(p):
	'''
	Arg : Expression
	'''
	p[0] = Arg(p[1])

def p_ParamList(p):
	'''
	ParamList : 
		  | Param
		  | ParamList COMMA Param
	'''
	if len(p)==1:
		p[0] = ParamList(None, None)
	elif len(p)==2:
		p[0] = ParamList(None, p[1])
	else:
		p[0] = ParamList(p[1], p[3])

def p_Param(p):
	'''
	Param : INDENTIFIER InitModifier
	'''
	p[0] = Param(p[1], p[2])

def p_Call(p):
	'''
	Call : Callable ArgList RPARENT
	'''
	p[0] = Call(p[1], p[3])

def p_Callable(p):
	'''
	Callable : NsContentName LPARENT 
		 | Expression LPARENT 
	'''
	if len(p)==2:
		p[0] = Callable(p[1])
	else:
		p[0] = Callable(p[1])
	

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

def p_NsContentName(p):
	'''
	NsContentName : INDENTIFIER
		      | BACKSLASH INDENTIFIER
		      | NsContentName BACKSLASH INDENTIFIER
	'''
	if len(p)==2:
		p[0] = NsContentName(None, p[1])
	elif len(p)==3:
		p[0] = NsContentName(None, p[1] + p[2])
	else:
		p[0] = NsContentName(p[1], p[1] + p[2])


def p_NsContentNameList(p):
	'''
	NsContentNameList : NsContentName
			  | NsContentNameList COMMA NsContentName
	'''
	if len(p)==2:
		p[0] = NsContentNameList(None, p[1])
	else:
		p[0] = NsContentNameList(p[1], p[3])

		
def p_NsContentNameAsId(p):
	'''
	NsContentNameAsId : NsContentName
			  | NsContentName AS INDENTIFIER
	'''
	if len(p)==2:
		p[0] = NsContentNameAsId(p[1])
	else:
		p[0] = NsContentNameAsId(p[1], p[3])


def p_NsContentNameAsIdList(p):
	'''
	NsContentNameAsIdList : NsContentNameAsId
			      | NsContentNameAsIdList COMMA NsContentNameAsId
	'''
	if len(p)==2:
		p[0] = NsContentNameAsIdList(None, p[1])
	else:
		p[0] = NsCOntentNameAsIdList(p[1], p[3])

def p_If(p):
	'''
	If : IfBlock
	   | IfBlock ELSE COLON Terminator Block
	'''
	if len(p)==2:
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

def p_For(p):
	'''
	For : FOR INDENTIFIER IN Expression COLON Terminator Block
	For : FOR INDENTIFIER COMMA INDENTIFIER IN Expression COLON Terminator Block
	'''
	if p[3] == 'IN':
		p[0] = For(p[2], None, p[4], p[6], p[7])
	else:
		p[0] = For(p[2], p[4], p[6], p[8], p[9])
	

def p_Class(p):
	'''
	Class : CLASS INDENTIFIER ExtendsModifier ImplementsModifier COLON Terminator ClassContent
	'''
	p[0] = Class(p[2], p[3], p[4], p[6], p[7])

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
	if len(p)<3:
		p[0] = InClassDefList(None, p[1])
	else:
		p[0] = InClassDefList(p[1], p[2])

def p_InClassDef(p):
	'''
	InClassDef : Embeded
		   | JustStrStatementWithTerminator
		   | DataMemberDef
		   | ConstDef
		   | MemberFuncDef
	'''
	p[0] = InClassDef(p[1])

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
	if len(p)<3:
		p[0] = InterfaceDefList(None, p[1])
	else:
		p[0] = InterfaceDefList(p[1], p[2])

	
def p_InterfaceDef(p):
	'''
	InterfaceDef : Embeded
		     | JustStrStatementWithTerminator
		     | ConstDef
		     | MemberFuncDec
	'''
	p[0] = InterfaceDef(p[1])


def p_ExtendsModifier(p):
	'''
	ExtendsModifier : 
			| EXTENDS NsContentName
	'''
	if len(p)>1:
		p[0] = ExtendsModifier(p[2])
	else:
		p[0] = ExtendsModifier(None)


def p_ImplementsModifier(p):
	'''
	ImplementsModifier : 
			   | IMPLEMENTS NsContentNameList 
	'''
	if len(p)>1:
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
	if len(p)>1:
		p[0] = AccessModifier(p[1])
	else:
		p[0] = AccessModifier('public')

def p_StaticModifier(p):
	'''
	StaticModifier : 
		       | STATIC
	'''
	if len(p)>1:
		p[0] = StaticModifier(p[1])
	else:
		p[0] = StaticModifier(None)

def p_MemberFuncDecWithoutTerminator(p):
	'''
	MemberFuncDecWithoutTerminator : AccessModifier StaticModifier INDENTIFIER LPARENT ParamList RPARENT
	'''
	p[0] = MemberFuncDecWithoutTerminator(p[1],p[2],p[3],p[5])


def p_MemberFuncDec(p):
	'''
	MemberFuncDec : MemberFuncDecWithoutTerminator Terminator
	'''
	p[0] = MemberFuncDec(p[1],p[2])

def p_MemberFuncDef(p):
	'''
	MemberFuncDef : MemberFuncDecWithoutTerminator COLON Terminator Block
	'''
	p[0] = MemberFuncDef(p[1], p[3], p[4])

def p_DataMemberDef(p):
	'''
	DataMemberDef : AccessModifier StaticModifier INDENTIFIER InitModifier Terminator
	'''
	p[0] = DataMemberDef(p[1], p[2], p[3], p[4], p[5])

def p_FuncDef(p):
	'''
	FuncDef : DEF INDENTIFIER LPARENT ParamList RPARENT COLON Terminator Block
	'''
	p[0] = FuncDef(p[2], p[4], p[7], p[8])

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

def p_Return(p):
	'''
	Return : RETURN Expression
	       | RETURN
	'''
	if len(p)>3:
		p[0] - Retrun(p[2])
	else:
		p[0] = Return(None)

def p_GlobalDec(p):
	'''
	GlobalDec : GLOBAL GlobalVaribleList
	'''
	p[0] = GlobalDec(p[2])

def p_GlobalVaribleList(p):
	'''
	GlobalVaribleList : INDENTIFIER
			  | GlobalVaribleList COMMA INDENTIFIER
	'''
	if len(p)>2:
		p[0] = GlobalVaribleList(p[1], p[3])
	else:
		p[0] = GlobalVaribleList(None, p[1])

def p_Operation(p):
	'''
	Operation : Math
		  | New
		  | Compare
	'''
	p[0] = Operation(p[1])

def p_Math(p):
	'''
	Math : Expression PLUS Expression
	'''
	p[0] = Operation(p[1], p[2], p[3])

def p_New(p):
	'''
	New : NEW NsContentName LPARENT ArgList RPARENT
	    | NEW Varible
	'''
	if len(p)>3:
		p[0] = New(p[2], p[4], None)
	else:
		p[0] = New(None, None, p[2])

def p_Compare(p):
	'''
	Compare : Expression EQ Expression
	'''
	p[0] = Compare(p[1], p[2], p[3])


def p_error(p):
	print p


