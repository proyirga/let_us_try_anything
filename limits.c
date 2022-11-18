#include <limits.h>
#include <stdio.h>
#include <stdlib.h>
/**
 * main - Entry point
 * Return: EXIT_SUCCESS
 *
 * Description: This is to test the limit.h header
 *
 */

int main(){
      char c;

      c = CHAR_MIN;
      while(c != CHAR_MAX){
              printf("%d\n", c);
              c = c+1;
      }

      exit(EXIT_SUCCESS);
}
