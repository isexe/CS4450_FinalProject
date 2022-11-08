grammar Project;

hi 
    : 'hello' ID
    ;

ID
    : [A-Za-z]+
    ;

WS 
    : [ \t\r\n]+ -> skip 
    ;