grammar LLang;

// Should contain only one justBlock. It is start point of whole programe.
programme
    : (variableDeclarationStatement | functionDeclaration | recordDeclaration | justBlock)*
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
    : '{' statement* '}'
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
    : exprType identifier ('=' expression)?
    ;

recordInitializer
    : 'new' identifier '(' recordFieldInitializerList? ')'
    ;

recordFieldInitializerList
    : (recordFieldInitializer ',')* recordFieldInitializer
    ;

recordFieldInitializer
    : identifier '=' expression
    ;

cortegeInitializer
    : '[' expressionList? ']'
    ;

expressionList
    : expression (',' expression)*
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
    : '[' cortegeTypeNonEmptyList ']'
    ;

cortegeTypeUnit
    : primitiveType
    | cortegeType
    ;

cortegeTypeNonEmptyList
    : cortegeTypeUnit (',' cortegeTypeUnit)*
    ;

// Shouldn't have own scope!
block
    : '{' statement* '}'
    ;

// Has its own scope unlike block
justBlock
    : block
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
    | breakStatement
    | continueStatement
    | returnStatement
    ;

breakStatement
    : breaks ';'
    ;

breaks
    : 'break'
    ;

continueStatement
    : continues ';'
    ;

continues
    : 'continue'
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
    : FOR '(' forInit ';' forCondition ';' forUpdate ')' block
    ;

forInit
    : assignment
    | variableDeclaration
    ;

forCondition
    : expression
    ;

forUpdate
    : assignment
    | functionInvocation
    ;

ifStatement
    : IF '(' expression ')' justBlock elifBlock* elseBlock?
    ;

elifBlock
    : ELIF '(' expression ')' justBlock
    ;

elseBlock
    : ELSE justBlock
    ;

writelnStatement
    : writelnCall ';'
    ;

writelnCall
    : WRITELN '(' argumentList ')'
    ;

readlnStatement
    : readIntCall ';'
    | readStrCall ';'
    | readBoolCall ';'
    ;

readIntCall
    : 'readInt' '(' leftHandSide ')'
    ;

readStrCall
    : 'readStr' '(' leftHandSide ')'
    ;

readBoolCall
    : 'readBool' '(' leftHandSide ')'
    ;

functionInvocationStatement
    : functionInvocation ';'
    ;

functionInvocation
    : identifier '(' argumentList ')'
    ;

argumentList
    : (expression (',' expression)*)?
    ;

expression
    : '(' expression ')'
    | unaryOperator expression
    | <assoc=left> expression mulDivModOperator expression
    | <assoc=left> expression addSubOperator expression
    | <assoc=left> expression compareOperator expression
    | <assoc=left> expression equalOrNotOperator expression
    | <assoc=left> expression boolOperator expression
    | functionInvocation
    | literal
    | cortegeInitializer
    | recordInitializer
    | leftHandSide
    ;

assignmentStatement
    : assignment ';'
    ;

assignment
	:	leftHandSide assignmentOperator expression
	;

leftHandSide
	: identifier
	| recordFieldAccess
	| cortegeAccess
	;

cortegeAccess
    : cortegeAccess '[' intLiteral ']'
    | identifier '[' intLiteral ']'
    ;

recordFieldAccess
    : identifier
    | recordFieldAccess '.' (identifier | cortegeAccess)
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
