grammar LLang;

programme
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
    : exprType
    | voidType
    ;

functionBody
    : '{' statement* returnStatement? '}'
    ;

functionParameterList
    : (functionParameter COMMA)* functionParameter
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
    : (recordFieldInitializer COMMA)* recordFieldInitializer
    ;

recordFieldInitializer
    : identifier '=' expression
    ;

cortegeInitializer
    : '[' variableInitializerNonEmptyList? ']'
    ;

variableInitializerNonEmptyList
    : variableInitializer (COMMA variableInitializer)*
    ;

passStatement
    : PASS ';'
    ;

exprType
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
voidType : NONE;

cortegeType
    : '[' typeNonEmptyList ']'
    ;

typeNonEmptyList
    : exprType (COMMA exprType)*
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
    | whileStatement
    | passStatement
    | readlnStatement
    | writelnStatement
    ;

returnStatement
    : RETURN expression? ';'
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
    : IF '(' expression ')' block (ELIF '(' expression ')' block)* (ELSE block)?
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
    : READLN '(' leftHandSide (COMMA leftHandSide)* ')'
    ;

functionInvocationStatement
    : functionInvocation ';'
    ;

functionInvocation
    : identifier '(' argumentList? ')'
    ;

argumentList
    : expression (COMMA expression)*
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

// keywords

// Types
BOOL : 'Bool';
INT : 'Int';
STR : 'Str';
NONE : 'None';

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
