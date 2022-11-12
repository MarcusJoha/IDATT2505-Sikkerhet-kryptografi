#include "utility.h"
#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

extern int LLVMFuzzerTestOneInput(const uint8_t* S, const uint8_t* oldWord, const uint8_t* newWord) {
  
  size_t size1 = sizeof(S);
  size_t size2 = sizeof(oldWord);
  size_t size3 = sizeof(newWord);
  
  char *str1 = (char *)malloc(sizeof(char) * size1 + 1);
  char *str2 = (char *)malloc(sizeof(char) * size2 +1 );
  char *str3 =(char *)malloc(sizeof(char) * size3 +1);
  
  memcpy(str1, S, size1);
  memcpy(str2, oldWord, size2);
  memcpy(str3, newWord, size3);
  
  str1[size1] = '\0';
  str2[size2] = '\0';
  str3[size3] = '\0';
  
  replace(str1, str2, str3);
  
  free(str1);
  free(str2);
  free(str3);
  
  return 0; 
}
