grammar LLang;

programm
    : (variableDeclarationStatement | functionDeclaration)*
    ;

functionDeclaration
    : FUN functionSignature functionBody
    ;

functionSignature
    : Identifier '(' functionParameterList? ')'
    ;

functionBody
    : block
    ;

functionParameterList
    : (functionParameter ',')* functionParameter
    ;

functionParameter
    : Identifier;

variableDeclarationStatement
    : variableDeclaration ';'
    ;

variableDeclaration
    : type Identifier ('=' variableInitializer)?
    ;

variableInitializer
    : expression
    | arrayInitializer
    ;

arrayInitializer
    : '[' variableInitializerList? ']'
    ;

variableInitializerList
    : variableInitializer (',' variableInitializer)*
    ;

type
    : primitiveType
    | arrayType
    ;

primitiveType
    : BOOL
    | INT
    | STR
    ;

arrayType
    : primitiveType dims
    ;

dims
    : ('[' ']')+
    ;


block
    : '{' statement* '}'
    ;

statement
    : block
    | assignmentStatement
    | ifStatement
    | functionInvocationStatement
    | forStatement
    ;

forStatement
    : FOR '(' forInit? ';' expression? ';' forUpdate? ')' block
    ;

forInit
    : assignment
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
    : Identifier '(' functionParameterList? ')'
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
    | Identifier
    | '(' expression ')'
    ;

assignmentStatement
    : assignment ';'
    ;

assignment
	:	leftHandSide assignmentOperator expression
	;

leftHandSide
	:	expressionName
//	|	arrayAccess
	;

expressionName
    : Identifier
    ;

literal
    : IntegerLiteral
    | StringLiteral
    | BooleanLiteral
    ;

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
VOID : 'Bool';

CLASS : 'class';
DOUBLE : 'double';
ELSE : 'else';
FOR : 'for';
IF : 'if';
ELIF : 'elif';
NEW : 'new';
RETURN : 'return';
THIS : 'this';
WHILE : 'while';
FUN : 'fun';

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
