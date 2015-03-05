grammar LLang;

programm
    : programmStatement*
    ;

programmStatement
    : variableDeclarationStatement
    | functionDeclaration
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

block
    : '{' blockStatements? '}'
    ;

blockStatements
    : blockStatement blockStatement*
    ;

blockStatement
    : variableDeclaration
    | block
    | assignment
    | ifStatement
    | functionInvocation
    | forStatement
    ;

forInit
    : variableDeclaration
    ;

forUpdate
    : assignment
    | functionInvocation
    ;

forStatement
    : FOR '(' forInit? ';' expression? ';' forUpdate? ')' block
    ;

ifStatement
    : IF '(' expression ')' (ELIF block)* (ELSE block)?
    ;

variableDeclarationStatement
    : variableDeclaration ';'
    ;

variableDeclaration
    : Identifier ('=' variableInitializer)?
    ;

variableInitializer
    : expression
    ;

functionInvocation
    : Identifier '(' functionParameterList? ')'
    ;

expression
    : ternaryExpression
    | assignment
    ;

assignment
	:	leftHandSide assignmentOperator ternaryExpression
	;

leftHandSide
	:	expressionName
//	|	arrayAccess
	;

expressionName
    : Identifier
    ;

ternaryExpression
    : orExpression
    | orExpression '?' expression ':' ternaryExpression
    ;

orExpression
    : andExpression
    | orExpression '||' andExpression
    ;

andExpression
    : equalityExpression
    | andExpression '&&' equalityExpression
    ;

equalityExpression
    : relationalExpression
    | equalityExpression '==' relationalExpression
    | equalityExpression '!=' relationalExpression
    ;

relationalExpression
    : additiveExpression
    | relationalExpression '<' additiveExpression
    | relationalExpression '>' additiveExpression
    | relationalExpression '<=' additiveExpression
    | relationalExpression '>=' additiveExpression
    ;

additiveExpression
    : multiplicativeExpression
    | additiveExpression '+' multiplicativeExpression
    | additiveExpression '-' multiplicativeExpression
    ;

multiplicativeExpression
    : unaryExpression
    | multiplicativeExpression '*' unaryExpression
    | multiplicativeExpression '/' unaryExpression
    | multiplicativeExpression '%' unaryExpression
    ;

unaryExpression
	: '+' unaryExpression
	| '-' unaryExpression
	| '!' unaryExpression
	| primary
	| expressionName
	;

primary
    : literal
    | '(' expression ')'
    | functionInvocation
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
BOOLEAN : 'bool';
CLASS : 'class';
DOUBLE : 'double';
ELSE : 'else';
FOR : 'for';
IF : 'if';
ELIF : 'elif';
INT : 'int';
NEW : 'new';
RETURN : 'return';
THIS : 'this';
VOID : 'void';
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
INC : '++';
DEC : '--';
ADD : '+';
SUB : '-';
MUL : '*';
DIV : '/';
MOD : '%';
ARROW : '->';

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
