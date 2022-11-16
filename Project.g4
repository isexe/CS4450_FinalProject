grammar Project;

// information on how to reserve words that variables can't use was found at resource #5
RESERVED_WORD 
    : 'class' | 'public' | 'static' | 'extends' | 'void' | 'boolean' 
    | 'if' | 'else' | 'while' | 'return' | 'null' | 'true' | 'false' | 'this' 
    | 'new' | 'String' | 'str' | 'int' | 'float' | 'complex'| 'list' | 'tuple' | 'range'
    | 'dict' | 'set' | 'frozenset' | 'bool' | 'bytes' | 'bytearray' | 'memoryview' | 'nonetype';

// compile all the code
code : line* EOF ;

// each line of code
line : statement EOL ;

// all the parse rules that need to be followed
// be careful, currently equation can go straight to atom and overshadow stuff
// with the addition of declare make sure to keep equation at the bottom
statement 
    : declare
    | assign
    | equation
    ;

// parser rule for declaring a variable
declare : VAR;

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
    | CHAR
    | BOOL
    | NONE
    ;

// TODO currently this breaks the addition and subtraction if there isn't a space
// rule for signed decimal numbers
// requires num before . so need to add option for no num but forced decimal
// now 0.0, 0., and .0 are all valid
NUM : DECIMAL ;

// real numbers
// works with 0.0 .0 and 0.
DECIMAL 
    : DIGIT+ ('.' DIGIT*)?
    | (DIGIT* '.')? DIGIT+
    ;

// 1 digit numbers
DIGIT : [0-9] ;

// TODO need to include much more than this
CHAR : QUOTES ([A-Za-z] | [0-9] | WS | TAB | EOL)+ QUOTES;

QUOTES : '"' | '\'';

// Bool
BOOL : 'True' | 'False' ;

// None
NONE : 'None' ;

// follow python naming conventions
VAR : [A-Za-z_][0-9A-Za-z_]* ;

EOL : [\n\r]+ ;

// not impemented yet but tabs are used for scope not WS
TAB : [\t] -> skip;

WS : [ ]+ -> skip ;