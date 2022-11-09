grammar Project;

// Might want to break apart grammer into others for organization
// follows OOP concepts
// import OtherGrammer;

// need to represent math expression beyond just 1 + 1
// i.e. (1 + 2) * 3
// TODO change NUM to all datatypes i.e. 'a' + 'b' should be 'ab'
expression  // reads left to right, top to bottom, so ordering needs to follow PEMDAS
    : '(' expression ')'
    | left=expression operator=('*' | '/' | '%') right=expression
    | left=expression operator=('+' | '-') right=expression
    | terminal=ATOM
    ;

ATOM
    : NUM
    ;
    
NUM : [0-9]+ ('.' [0-9]*)? ;


// Focus on one at a time
/* 
// TODO change value = NUM to all datatypes
// TODO need to add other assignment operators
assignment
    : name=VAR operator='=' value=NUM
    ;

// generic number format must allow for digits 0-9 as well as decimal points
// TODO implement signed num

// Variable naming conventions
// Must start with letter or _
// can continue with letters, numbers, or _
VAR 
    : [A-Za-z_][0-9A-Za-z_]*
    ;
*/

WS : [ \t\r\n]+ -> skip ;