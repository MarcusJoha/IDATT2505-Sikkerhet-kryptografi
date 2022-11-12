#include "utility.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() 
{

	char wordsN[3][5] = {"&amp", "&lt", "&gt"};
	char wordsO[3][2] = {"<", "&", ">"};

	char str[] = "< < & & > >";

	printf("Old string: %s\n", str);

	char* result1 = NULL;
	char* result2 = NULL;
	char* result3 = NULL;


	result1 = replace(str, wordsO[1], wordsN[1]);
	result2 = replace(result1, wordsO[0], wordsN[0]);
	result3 = replace(result2, wordsO[2], wordsN[2]);


	printf("New string: %s\n ", result3);

	free(result1);
	free(result2);
	free(result3);
	
	return 0;
 
}
