#include <unistd.h>
#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <crypt.h>

int main()
{
   printf("%s\n",crypt("abc","ab"));
    exit(0);
}
    
 