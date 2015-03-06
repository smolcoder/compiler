grammar LLang;

programm
    : (variableDeclarationStatement | functionDeclaration | recordDeclaration)*
    ;

recordDeclaration
    : RECORD identifier recordBody
    ;

recordBody
    : '{' variableDeclarationStatement* '}'
    ;

functionDeclaration
    : FUN functionSignature functionBody
    ;

functionSignature
    : identifier '(' functionParameterList? ')' ':' functionReturnType
    ;

functionReturnType
    : type
    | voidType
    ;

functionBody
    : '{' statement* returnStatement? '}'
    ;

functionParameterList
    : (functionParameter ',')* functionParameter
    ;

functionParameter
    : identifier ':' type;

variableDeclarationStatement
    : variableDeclaration ';'
    ;

variableDeclaration
    : type Identifier ('=' variableInitializer)?
    ;

variableInitializer
    : expression
    | cortegeInitializer
    ;

recordInitializer
    : identifier '(' recordFieldInitializerList? ')'
    ;

recordFieldInitializerList
    : (recordFieldInitializer ',')* recordFieldInitializer
    ;

recordFieldInitializer
    : identifier '=' expression
    ;

cortegeInitializer
    : '[' variableInitializerNonEmptyList? ']'
    ;

variableInitializerNonEmptyList
    : variableInitializer (',' variableInitializer)*
    ;

passStatement
    : PASS ';'
    ;

type
    : primitiveType
    | cortegeType
    | recordType
    ;

primitiveType
    : intType
    | strType
    | boolType
    ;

recordType
    : Identifier
    ;

intType : INT;
strType : STR;
boolType : BOOL;
voidType : VOID;

cortegeType
    : '[' typeNonEmptyList ']'
    ;

typeNonEmptyList
    : type (',' type)*
    ;

block
    : '{' statement* '}'
    ;

statement
    : block
    | variableDeclarationStatement
    | assignmentStatement
    | ifStatement
    | functionInvocationStatement
    | forStatement
    | passStatement
    ;

returnStatement
    : RETURN expression? ';'
    ;

forStatement
    : FOR '(' forInit? ';' expression? ';' forUpdate? ')' block
    ;

forInit
    : assignment
    | variableDeclaration
    ;

forUpdate
    : assignment
    | functionInvocation
    ;

ifStatement
    : IF '(' expression ')' (ELIF block)* (ELSE block)?
    ;

functionInvocationStatement
    : functionInvocation ';'
    ;

functionInvocation
    : identifier '(' argumentList? ')'
    ;

argumentList
    : expression (',' expression)*
    ;

expression
    : assignment
    | '-' expression
    | '!' expression
    | expression ('*' | '/' | '%') expression
    | expression ('-' | '+') expression
    | expression ('>' | '>=' | '<=' | '<') expression
    | expression ('==' | '!=') expression
    | expression '&&' expression
    | expression '||' expression
    | functionInvocation
    | literal
    | identifier
    | cortegeInitializer
    | cortegeAccess
    | recordFieldAccess
    | '(' expression ')'
    ;

assignmentStatement
    : assignment ';'
    ;

assignment
	:	leftHandSide assignmentOperator expression
	;

leftHandSide
	: expressionName
	| cortegeAccess
	| recordFieldAccess
	;

cortegeAccess
    : identifier '[' expression ']'
    ;

recordFieldAccess
    : identifier '.' leftHandSide
    ;

expressionName
    : identifier
    ;

literal
    : intLiteral
    | strLiteral
    | boolLiteral
    ;

intLiteral : IntegerLiteral;
strLiteral : StringLiteral;
boolLiteral : BooleanLiteral;

assignmentOperator
	:	'='
	|	'*='
	|	'/='
	|	'%='
	|	'+='
	|	'-='
	;

// keywords

// Types
BOOL : 'Bool';
INT : 'Int';
STR : 'Str';
VOID : 'Void';

RECORD : 'record';
ELSE : 'else';
FOR : 'for';
IF : 'if';
ELIF : 'elif';
RETURN : 'return';
FUN : 'fun';
PASS : 'pass';

LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
LBRACK : '[';
RBRACK : ']';
SEMI : ';';
COMMA : ',';
DOT : '.';

ASSIGN : '=';
GT : '>';
LT : '<';
BANG : '!';
COLON : ':';
EQUAL : '==';
LE : '<=';
GE : '>=';
NOTEQUAL : '!=';
AND : '&&';
OR : '||';
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
MOD : '%';

ADD_ASSIGN : '+=';
SUB_ASSIGN : '-=';
MUL_ASSIGN : '*=';
DIV_ASSIGN : '/=';
AND_ASSIGN : '&=';
MOD_ASSIGN : '%=';


// identifiers

identifier : Identifier;

Identifier
    : [a-zA-Z_] [a-zA-Z0-9_]*
    ;

BooleanLiteral
    : 'true'
    | 'false'
    ;

StringLiteral
	:	'"' ~["\\]* '"'
	;

IntegerLiteral
    : '0'
   	| [1-9] [0-9]*
   	;

WS  :  [ \t\r\n\u000C]+ -> skip
    ;

COMMENT
    :   '/*' .*? '*/' -> skip
    ;

LINE_COMMENT
    :   '//' ~[\r\n]* -> skip
    ;
