grammar Project;

// compile all the code
code : (block | line)* EOF ;

// blocks of code
block 
    : ifElseBlock
    | whileLoop
    | forLoop
    | functionDef
    ;

// each line of code
line : statement? EOL ;

// all the parse rules that need to be followed
// be careful, currently equation can go straight to atom and overshadow stuff
// with the addition of declare make sure to keep equation at the bottom
statement 
    : assign
    | functionCall
    | functionReturn
    | logicExpr
    | equation
    ;

/***
** FUNCTION STUFF
***/
functionDef :
    DEF functionID ( '(' paramID (',' paramID)* '):' | '():' ) EOL
        functionCode
  ;

// can repeat code until a return
functionCode
    : (indent (block | line))+
    ;

// most likely need to add this to some larger type, maybe equation since that has most things rn
functionCall
  : functionID ('(' paramVal (',' paramVal)* ')' | '()')
  ;

functionReturn
    : RETURN returnVal
    ;


returnVal
    : VAR
    | ATOM
    | logicExpr
    | equation 
    ;

RETURN : 'return' ;

functionID : VAR ;

paramID : VAR ;
paramVal 
    : VAR
    | ATOM
    | equation 
    ;

DEF : 'def' ;

/***
** LOOP STUFF
***/
// while loop
whileLoop
    : ((WHILE logicExpr (':')) EOL
    | (WHILE ('(') logicExpr ('):')) EOL)
        whileCode
    ;

whileCode
    : (indent (block | line))+
    ;
    
WHILE: 'while';

// for loop
forLoop
    : (FOR id IN RANGE ('(') range ('):')) EOL
        forCode
    ;
    
forCode
    : (indent (block | line))+
    ;

range
    :  rangeVal (',' rangeVal (',' rangeVal)?)?
    ;

rangeVal
    : VAR
    | ATOM 
    | equation
    ;

FOR: 'for';
IN: 'in';
RANGE: 'range';

/***
** LOGICAL STUFF
***/
// if/else statment
ifElseBlock :
    ifStatement
    (indent* elifStatement)*
    (indent* elseStatement)?
    ;


ifStatement
    : ((IF logicExpr (':')) EOL 
    | (IF ('(') logicExpr ('):')) EOL )
        ifElseCode
    ;

elifStatement
    : ((ELIF logicExpr (':')) EOL 
    | (ELIF ('(') logicExpr ('):')) EOL )
        ifElseCode
    ;

elseStatement
    : ELSE (':') EOL
        ifElseCode
    ;

ifElseCode
    : (indent (block | line))+
    ;
    
IF: 'if' ;
ELIF: 'elif' ;
ELSE: 'else' ;

// logical Expression
logicExpr 
    : '('? (NOT)? (logicVal (logicOp logicVal)*) ')'? (logicConj '('? logicExpr ')'?)*
    ;

logicVal
    : VAR
    | ATOM 
    | equation
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

/***
** ASSIGN STUFF
***/
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
    | logicExpr
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

/***
** ARITHMETIC STUFF
***/
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


/***
** GENERAL HOUSE KEEPING STUFF
***/
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
indent : TAB+ ;

TAB : [\t];

WS : [ ]+ -> skip ;

COMMENTS : '#' (NUM | [A-Za-z,.<>/?'";:!@#$%^&*()\-_] | WS | TAB)* -> skip ;

// TODO
// genericVal
//     : VAR
//     | ATOM
//     | functionCall
//     | equation 
//     ;