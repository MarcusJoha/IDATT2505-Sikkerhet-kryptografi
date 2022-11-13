#pragma once
#include <stdlib.h>
#include <string.h>

char *replace(const char* S, const char* oldWord, const char* newWord)
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

	i = 0;

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
