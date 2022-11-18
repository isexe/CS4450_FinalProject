grammar Project;

// information on how to reserve words that variables can't use was found at resource #5
// as you need to use these remove them from list and insert them in the section you used them
// i.e. if section now has lexer rule for IF and ELSE
RESERVED_WORD 
    : 'class' | 'public' | 'static' | 'extends' | 'void' | 'boolean' 
    | 'while' | 'return' | 'null' | 'this' 
    | 'new' | 'String' | 'str' | 'int' | 'float' | 'complex'| 'list' | 'tuple' | 'range'
    | 'dict' | 'set' | 'frozenset' | 'bool' | 'bytes' | 'bytearray' | 'memoryview' | 'nonetype';

// compile all the code
code : (block | line)* EOF ;

// blocks of code
block : ifElseBlock;

// each line of code
line : statement EOL ;

// all the parse rules that need to be followed
// be careful, currently equation can go straight to atom and overshadow stuff
// with the addition of declare make sure to keep equation at the bottom
statement 
    : assign
    | logicExpr
    | equation
    ;

/* 
TODO need to allow for nested blocks
to do this will need to figure out how to track indents
*/

ifElseBlock :
    ifStatement
    (elifStatement)*
    (elseStatement)?
    ;

ifStatement
    : (IF ('(') logicExpr ('):')) EOL 
        (TAB line)+
    ;

elifStatement
    : (ELIF ('(') logicExpr ('):')) EOL 
        (TAB line)+
    ;

elseStatement
    : ELSE (':') EOL
        (TAB line)+
    ;

IF: 'if' ;
ELIF: 'elif' ;
ELSE: 'else' ;

logicExpr 
    : logicVal (logicOp logicVal)? (logicConj logicExpr)?
    ;

logicVal
    : (NOT)? VAR
    | (NOT)? ATOM 
    | (NOT)? equation
    ;

logicOp
    : '=='
    | '!='
    | '>='
    | '>'
    | '<='
    | '<'
    ;

logicConj
    : AND
    | OR
    ;

AND : 'and' ;
OR : 'or' ;
NOT : 'not' ;

// parser rule for assignment
// information on assignemnt operators found at resource #4
assign
    : left=id operator=EQU right=assign_val
    | left=id operator=PLU_EQU right=assign_val
    | left=id operator=MIN_EQU right=assign_val
    | left=id operator=MULT_EQU right=assign_val
    | left=id operator=DIV_EQU right=assign_val
    ;

assign_val
    : VAR
    | ATOM
    | equation
    ;

// parser rule
id : VAR ;

// lexer rules used in the assign parse rule
// all the different assignment operators
EQU : '=' ;
PLU_EQU : '+=' ;
MIN_EQU : '-=' ;
MULT_EQU : '*=' ;
DIV_EQU : '/=' ;

//*** NOTES
// Arithmetic rule
// grows one way rather than both to fix ambiguity
// changed lexer rules to parse rules
// broke apart into seperate rules for neatness and more control
// Depth First Search so important at bottom


// parser rule for arithmetic
equation : eqFourthOrder ;

// follow order of operations in ascending order
eqFourthOrder : eqThirdOrder ((add | sub) eqThirdOrder)* ;

eqThirdOrder : eqSecondOrder ((mult | div | mod) eqSecondOrder)* ;

eqSecondOrder : eqFirstOrder ((expon | sqrt) eqFirstOrder)* ;

// moved negative sign here by suggestion in reference #6
eqFirstOrder
    : sign=('+' | '-')? ('(' para=eqFourthOrder ')' | terminal=eqVal)
    ;

eqVal
    : ATOM
    | VAR
    ;

// parser rules used in the equation parse rule
// all the different math operators
// were lexer rules but changed in hopes it would fix the positive sign issue
// 1 +1 is read as two equations 1 and +1 rather than 1+1
expon : '**' ;
sqrt : '//' ;
mult : '*' ;
div : '/' ;
mod : '%' ;
add : '+' ;
sub : '-' ;

// rule for defining datatypes
ATOM
    : NUM
    | STRING
    | BOOL
    | NONE
    ;


// real numbers
// works with 0.0 .0 and 0.
NUM 
    : DIGIT+ ('.' DIGIT*)?
    | (DIGIT* '.')? DIGIT+
    ;

// 1 digit numbers
fragment DIGIT : [0-9] ;

// Bool
BOOL : 'True' | 'False' ;

// None
NONE : 'None' ;



// TODO need to include much more than this
STRING : QUOTES (CHAR | DIGIT | WS | TAB | EOL)+ QUOTES;

fragment QUOTES : '"' | '\'';

fragment CHAR : [A-Za-z] ;

// follow python naming conventions
VAR : [A-Za-z_][0-9A-Za-z_]* ;

EOL : [\n\r]+ ;

// not impemented yet but tabs are used for scope not WS
TAB : [\t];

WS : [ ]+ -> skip ;