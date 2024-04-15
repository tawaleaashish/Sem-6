%{
#include<stdio.h>
#include<string.h>
%}

%%
(a|b)*abb  printf("Valid String\n");
%%
  
int yywrap(void){}  
int main()
{   
    yylex();
    return 0;
}