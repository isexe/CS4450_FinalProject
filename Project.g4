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

assign
    : id eq equation         #assignment
    | id eq_add equation     #addition_assignment
    | id eq_sub equation     #subtraction_assignment
    | id eq_mult equation    #multiplication_assignment
    | id eq_div equation     #division_assignment
    ;

id : VAR ;

// rules used in the assign parse rule
// all the different assignment operators
eq : '=' ;
eq_add : '+=' ;
eq_sub : '-=' ;
eq_mult : '*=' ;
eq_div : '/=' ;

// Arithmetic rule
// grows one way to fix ambiguity rather than both to fix
// changed lexer rules to parse rules
// broke apart into seperate rules for neatness and more control
// Depth First Search so important at bottom
// parser rule for arithmetic
equation : factor ((add | sub) factor)* ;

factor : exponent ((mult | div | mod) exponent)* ;

exponent : ATOM (expon ATOM)* ;

val
    : '(' equation ')'
    | VAR
    | ATOM;

// parser rules used in the equation parse rule
// all the different math operators
// believe parser rules have higher precedence than lexer rules
// hopefully this fixes issues with positive values
expon : '**' ;
mult : '*' ;
div : '/' ;
mod : '%' ;
add : '+' ;
sub : '-' ;

//! DEPRECIATED
//BAD ambigous and left/right repeating
expression
   : '(' expr=expression ')'
   | left=expression operator=EXPON right=expression
   | left=expression operator=(MULT | DIV | MOD) right=expression
   | left=expression operator=(ADD | SUB) right=expression
   | terminal=(ATOM | VAR)
   ;

EXPON : '**' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
ADD : '+' ;
SUB : '-' ;

// rule for defining datatypes
ATOM
    : NUM
    | CHAR
    ;

// TODO currently this breaks the addition and subtraction if there isn't a space
// rule for signed decimal numbers
// requires num before . so need to add option for no num but forced decimal
// now 0.0, 0., and .0 are all valid
NUM 
    : ('+' | '-')? DECIMAL;

// real numbers
DECIMAL 
    : DIGIT+ ('.' DIGIT*)?
    | (DIGIT* '.')? DIGIT+;

// 1 digit numbers
DIGIT : [0-9];

// TODO need to include much more than this
CHAR : QUOTES ([A-Za-z] | [0-9])+ QUOTES;

QUOTES : '"' | '\'';

// follow python naming conventions
VAR : [A-Za-z_][0-9A-Za-z_]* ;

EOL : [\n\r]+ ;

// skip for now but tabs are important for scope later on
TAB : [\t] -> skip;

WS : [ ]+ -> skip ;