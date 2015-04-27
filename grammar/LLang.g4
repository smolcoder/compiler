grammar LLang;

programme
    : (variableDeclarationStatement | functionDeclaration | recordDeclaration | justBlock)*
    ;

justBlock
    : block
    ;

recordDeclaration
    : RECORD recordId recordBody
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
    : exprType
    | voidType
    ;

functionBody
    : '{' statement* returnStatement? '}'
    ;

functionParameterList
    : (functionParameter ',')* functionParameter
    ;

functionParameter
    : identifier ':' exprType;

variableDeclarationStatement
    : variableDeclaration ';'
    ;

variableDeclaration
    : exprType identifier ('=' variableInitializer)?
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

exprType
    : primitiveType
    | cortegeType
    | recordId
    ;

primitiveType
    : intType
    | strType
    | boolType
    ;

recordId
    : Identifier
    ;

intType : INT;
strType : STR;
boolType : BOOL;
voidType : NONE;

cortegeType
    : '[' typeNonEmptyList ']'
    ;

typeNonEmptyList
    : exprType (',' exprType)*
    ;

block
    : '{' statement* '}'
    ;

statement
    : justBlock
    | variableDeclarationStatement
    | assignmentStatement
    | ifStatement
    | functionInvocationStatement
    | forStatement
    | whileStatement
    | passStatement
    | readlnStatement
    | writelnStatement
    ;

returnStatement
    : returnExpr ';'
    ;

returnExpr
    : RETURN expression?
    ;

whileStatement
    : WHILE '(' expression ')' block
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
    : IF '(' expression ')' justBlock (ELIF '(' expression ')' justBlock)* (ELSE justBlock)?
    ;

writelnStatement
    : writelnCall ';'
    ;

writelnCall
    : WRITELN '(' argumentList ')'
    ;

readlnStatement
    : readlnCall ';'
    ;

readlnCall
    : READLN '(' leftHandSide (',' leftHandSide)* ')'
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
    | unaryOperator expression
    | expression mulDivModOperator expression
    | expression addSubOperator expression
    | expression compareOperator expression
    | expression equalOrNotOperator expression
    | expression boolOperator expression
    | functionInvocation
    | literal
    | cortegeInitializer
    | recordInitializer
    | identifier
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
	: identifier
	| cortegeAccess
	| recordFieldAccess
	;

cortegeAccess
    : identifier '[' expression ']'
    ;

recordFieldAccess
    : identifier '.' leftHandSide
    ;

literal
    : intLiteral
    | strLiteral
    | boolLiteral
    ;

intLiteral : IntegerLiteral;
strLiteral : StringLiteral;
boolLiteral : BooleanLiteral;

unaryOperator
    : '-'
    | '!'
    ;

mulDivModOperator
    : '*'
    | '/'
    | '%'
    ;

addSubOperator
    : '+'
    | '-'
    ;

compareOperator
    : '>'
    | '>='
    | '<'
    | '<='
    ;

equalOrNotOperator
    : '=='
    | '!='
    ;

boolOperator
    : '&&'
    | '||'
    ;

assignmentOperator
	:	'='
	|	'*='
	|	'/='
	|	'%='
	|	'+='
	|	'-='
	;

// Types
BOOL : 'Bool';
INT : 'Int';
STR : 'Str';
NONE : 'None';

// keywords
RECORD : 'record';
WRITELN : 'writeln';
READLN : 'readln';
ELSE : 'else';
FOR : 'for';
WHILE : 'while';
IF : 'if';
ELIF : 'elif';
RETURN : 'return';
FUN : 'fun';
PASS : 'pass';

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
