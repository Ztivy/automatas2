grammar Expr;
//el gramar indica como se llama el archivo
root : expr EOF;

//expr : expr MAS expr | NUM;

expr : EOF;

//en EOF estan las reglas sintacticas

IF :'if';
ID : [A-Za-z];
MAYOR_QUE : '>';
NUM : [0-9]+;
MAS : '+';
WS : [ \t\r\n]+->skip;