grammar Project;

// Might want to break apart grammer into others for organization
// follows OOP concepts
// import OtherGrammer;

// parser rule for arithmetic
// reads left to right, top to bottom, so ordering needs to follow PEMDAS (maybe)
// TODO fix bug with addition and subtraction not working when no space is present

assign
    : left=id operator=EQU right=expression
    | left=id operator=PLU_EQU right=expression
    | left=id operator=MIN_EQU right=expression
    | left=id operator=MULT_equ right=expression
    | left=id operator=DIV_EQU right=expression
    ;

id 
    : terminal=VAR
    ;

expression
    : '(' expr=expression ')'
    | left=expression operator=EXPON right=expression
    | left=expression operator=(MULT | DIV | MOD) right=expression
    | left=expression operator=(ADD | SUB) right=expression
    | terminal=ATOM
    | terminal=VAR
    ;

// rules used in the expression parse rule
// all the different math operators
EXPON : '**' ;
MULT : '*' ;
DIV : '/' ;
MOD : '%' ;
ADD : '+' ;
SUB : '-' ;

// rules used in the assign parse rule
// all the different assignment operators
EQU : '=' ;
PLU_EQU : '+=' ;
MIN_EQU : '-=' ;
MULT_equ : '*=' ;
DIV_EQU : '/=' ;

// rule for defining datatypes
ATOM
    : NUM
    | CHAR
    ;

//TODO currently this breaks the addition and subtraction if there isn't a space
// rule for signed decimal numbers
NUM : ('+' | '-')? [0-9]+ ('.' [0-9]*)? ;

// TODO need to include much more than this
CHAR : ([A-Za-z] | [0-9])+;

// follow python naming conventions
VAR : [A-Za-z_][0-9A-Za-z_]* ;

WS : [ \t\r\n]+ -> skip ;