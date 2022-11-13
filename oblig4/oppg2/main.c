#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* replace(const char* S, const char* oldWord, const char* newWord)
{
	char* result;
	int i, cnt = 0;
	int newLen = strlen(newWord);
	int oldLen = strlen(oldWord);

	for (i = 0; S[i] != '\0'; i++)
	{
		if (strstr(&S[i], oldWord) == &S[i])
		{
			cnt++;

			// hopper til index etter ordet
			i += oldLen -1;
		}
	}

	result = (char*)malloc(i + cnt *(newWord - oldWord) + 1);

	int i = 0;

	while (*S) {
		// compare substring with result
		if (strstr(S, oldWord) == S) {
			strcpy(&result[i], newWord);
			i += newLen;
			S += oldLen;
		}
		else 
		{
			result[i++] = *S++;
		}
	}

	result[i] = '\0';
	return result; 
}


int main() 
{

	char wordsN[3][5] = {"&amp", "&lt", "&gt"};
	char wordsO[3][2] = {"<", "&", ">"};

	char str[] = "< < & & > >";

	printf("Old string: %s\n", str);

	char* result1 = NULL;
	char* result2 = NULL;
	char* result3 = NULL;

	// Terrible implementation
	// but it works
	result1 = replace(str, wordsO[1], wordsN[1]);
	result2 = replace(result1, wordsO[0], wordsN[0]);
	result3 = replace(result2, wordsO[2], wordsN[2]);


	printf("New string: %s\n ", result3);

	free(result1);
	free(result2);
	free(result3);

	
 
	return 0;
}
