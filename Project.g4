grammar Project;


// compile all the code
code : lines* EOF ;

// each line of code
lines : statement EOL ;

// all the parse rules that need to be followed
statement 
    : equation
    | assign
    ;

//parser rule for assignment
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


// Arithmetic rule
// grows one way rather than both to fix ambiguity
// changed lexer rules to parse rules
// broke apart into seperate rules for neatness and more control
// Depth First Search so important at bottom
// parser rule for arithmetic
equation : sum ;

// redundant but more readable in here and py code
sum : factor ((add | sub) factor)* ;

factor : val ((mult | div | mod) val)* ;

val
    : '(' sum ')'
    | ATOM
    | VAR
    ;

// parser rules used in the equation parse rule
// all the different math operators
// believe parser rules have higher precedence than lexer rules
// hopefully this fixes issues with positive values
mult : '*' ;
div : '/' ;
mod : '%' ;
add : '+' ;
sub : '-' ;

//! DEPRECIATED
//BAD ambigous and left/right recursion
// expression
//    : '(' expr=expression ')'
//    | left=expression operator=EXPON right=expression
//    | left=expression operator=(MULT | DIV | MOD) right=expression
//    | left=expression operator=(ADD | SUB) right=expression
//    | terminal=(ATOM | VAR)
//    ;

// EXPON : '**' ;
// MULT : '*' ;
// DIV : '/' ;
// MOD : '%' ;
// ADD : '+' ;
// SUB : '-' ;

// rule for defining datatypes
ATOM
    : NUM
    | CHAR
    ;

// TODO currently this breaks the addition and subtraction if there isn't a space
// rule for signed decimal numbers
// requires num before . so need to add option for no num but forced decimal
// now 0.0, 0., and .0 are all valid
NUM : ('+' | '-')? DECIMAL ;

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

// follow python naming conventions
VAR : [A-Za-z_][0-9A-Za-z_]* ;

EOL : [\n\r]+ ;

// not impemented yet but tabs are used for scope not WS
TAB : [\t] -> skip;

WS : [ ]+ -> skip ;