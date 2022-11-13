#include "utility.h"
#include <assert.h>
#include <string.h>

#include <stdio.h>

int main() {

    char sentence[] = "< < & & > >";
    char old_w[] = "<";
    char new_w[] = "&amp";
    char new_sentence[] = "&amp &amp & & > >";
    

    char* result = NULL;

    result = replace(sentence, old_w, new_w);
//    pritnf(result);


    assert(strcmp(result,new_sentence) == 0);

}
