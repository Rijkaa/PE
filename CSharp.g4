grammar CSharp;

// Lexer rules
WS : [ \t\r\n]+ -> skip;
COMMENT : '//' ~[\r\n]* -> skip;
MULTILINE_COMMENT : '/*' .*? '*/' -> skip;

// Keywords
CLASS : 'class';
PUBLIC : 'public';
PRIVATE : 'private';
STATIC : 'static';
VOID : 'void';
INT : 'int';
DOUBLE : 'double';
STRING : 'string';
BOOL : 'bool';
IF : 'if';
ELSE : 'else';
FOR : 'for';
WHILE : 'while';

// Identifiers
ID : [a-zA-Z_] [a-zA-Z_0-9]*;

// Literals
INT_LITERAL : [0-9]+;
DOUBLE_LITERAL : [0-9]+ '.' [0-9]+;
STRING_LITERAL : '"' (~["\r\n] | '\\"' | '\\n' | '\\r' | '\\t' | '\\b' | '\\f' | '\\u')* '"';
BOOL_LITERAL : 'true' | 'false';

// Operators
PLUS : '+';
MINUS : '-';
MULTIPLY : '*';
DIVIDE : '/';
MODULO : '%';
ASSIGN : '=';
EQUALS : '==';
NOT_EQUALS : '!=';
GREATER_THAN : '>';
LESS_THAN : '<';
GREATER_THAN_OR_EQUAL : '>=';
LESS_THAN_OR_EQUAL : '<=';
AND : '&&';
OR : '||';
NOT : '!';

// Punctuation
LPAREN : '(';
RPAREN : ')';
LBRACE : '{';
RBRACE : '}';
SEMICOLON : ';';
COMMA : ',';
DOT : '.';
QUESTION_MARK : '?';
COLON : ':';

// Parser rules
start : methodDeclarations? EOF;
compilation_unit : using_directive* namespace_declaration*;

using_directive : 'using' namespace_name SEMICOLON;

namespace_declaration : 'namespace' namespace_name LBRACE type_declaration* RBRACE;

namespace_name : ID (DOT ID)*;

type_declaration : class_declaration;

class_declaration : CLASS ID LBRACE class_member* RBRACE;

class_member : method_declaration | field_declaration;

method_declaration : method_modifier* method_return_type ID LPAREN formal_parameter_list? RPAREN method_body;

method_modifier : PUBLIC | PRIVATE | STATIC;

method_return_type : VOID | type;

formal_parameter_list : formal_parameter (COMMA formal_parameter)*;

formal_parameter : type ID;

method_body : LBRACE statement* RBRACE;

field_declaration : type ID SEMICOLON;

type : INT | DOUBLE | STRING | BOOL | ID;

statement : block | if_statement | iteration_statement | expression_statement | return_statement;

block : LBRACE statement* RBRACE;

if_statement : IF LPAREN expression RPAREN statement (ELSE statement)?;

iteration_statement : while_statement | for_statement;

while_statement : WHILE LPAREN expression RPAREN statement;

for_statement : FOR LPAREN for_initializer? SEMICOLON expression? SEMICOLON for_iterator? RPAREN statement;

for_initializer : local_variable_declaration | expression_statement;

for_iterator : expression;

local_variable_declaration : type ID (ASSIGN expression)?;

expression_statement : expression SEMICOLON;

return_statement : 'return' expression? SEMICOLON;

expression : assignment_expression;

assignment_expression : conditional_expression (ASSIGN assignment_expression)?;

conditional_expression : logical_or_expression (QUESTION_MARK expression COLON conditional_expression)?;

logical_or_expression : logical_and_expression (OR logical_and_expression)*;

logical_and_expression : equality_expression (AND equality_expression)*;

equality_expression : relational_expression ((EQUALS | NOT_EQUALS) relational_expression)*;

relational_expression : additive_expression ((GREATER_THAN | LESS_THAN | GREATER_THAN_OR_EQUAL | LESS_THAN_OR_EQUAL) additive_expression)*;

additive_expression : multiplicative_expression ((PLUS | MINUS) multiplicative_expression)*;

multiplicative_expression : unary_expression ((MULTIPLY | DIVIDE | MODULO) unary_expression)*;

unary_expression : primary_expression | (PLUS | MINUS | NOT) unary_expression;

primary_expression : literal | ID | LPAREN expression RPAREN;

literal : INT_LITERAL | DOUBLE_LITERAL | STRING_LITERAL | BOOL_LITERAL;

// Helper rules
namespace_name_list : namespace_name (COMMA namespace_name)*;