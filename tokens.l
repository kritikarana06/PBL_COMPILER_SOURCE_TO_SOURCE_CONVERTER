%{
#include <string>
#include "node.h"
#include "parser.hpp"
#define SAVE_TOKEN yylval.string = new std::string(yytext, yyleng)
#define TOKEN(t) (yylval.token = t)
extern "C" int yywrap() { return 1;}
extern int lineNumber;
%}

%%

^"#include ".+                          fprintf(stderr, "include line\n");
[ \t\r]                                 ;

"if"                                    return TOKEN(TIF);
"else"                                  return TOKEN(TELSE);
"for"                                   return TOKEN(TFOR);
"while"                                 return TOKEN(TWHILE);
"return"                                return TOKEN(TRETURN);

"int"                                   SAVE_TOKEN; return TINTTYPE; 
"double"                                SAVE_TOKEN; return TDOUBLETYPE;
"char"                                  SAVE_TOKEN; return TCHARTYPE;
"void"                                  SAVE_TOKEN; return TVOIDTYPE;

[a-zA-Z_][a-zA-Z0-9_]*                  SAVE_TOKEN; return TIDENTIFIER;
-?[0-9]+\.[0-9]*                        SAVE_TOKEN; return TDOUBLE;
-?[0-9]+                                SAVE_TOKEN; return TINTEGER;
['].[']                                 SAVE_TOKEN; return TCHAR;
["].*["]                                SAVE_TOKEN; return TSTRING;

"="                                     return TOKEN(TEQUAL);

"=="                                    return TOKEN(TCEQ);
"!="                                    return TOKEN(TCNE);
"<"                                     return TOKEN(TCLT);
"<="                                    return TOKEN(TCLE);
">"                                     return TOKEN(TCGT);
">="                                    return TOKEN(TCGE);

"&&"                                    return TOKEN(TAND);
"||"                                    return TOKEN(TOR);

"&"                                     return TOKEN(TAMPERSAND);

"("                                     return TOKEN(TLPAREN);
")"                                     return TOKEN(TRPAREN);
"{"                                     return TOKEN(TLBRACE);
"}"                                     return TOKEN(TRBRACE);
"["                                     return TOKEN(TLBRACK);
"]"                                     return TOKEN(TRBRACK);

"."                                     return TOKEN(TDOT);
","                                     return TOKEN(TCOMMA);
";"                                     return TOKEN(TSEMICOLON);

"+"                                     return TOKEN(TPLUS);
"-"                                     return TOKEN(TMINUS);
"*"                                     return TOKEN(TMUL);
"/"                                     return TOKEN(TDIV);
"++"                                     return TOKEN(TINC);
"--"                                     return TOKEN(TDEC);

"\n"                                    lineNumber += 1;

.                                       printf("Unknown token!n"); yyterminate();

%%