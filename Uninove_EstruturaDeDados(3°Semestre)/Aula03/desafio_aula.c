#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int maiin () {
    // declaração das strings
    char palavra [20], palavra_invertida [20];
    int i, j=0, tam;
    // leitura da string
    printf ("*** Digite a string ***\n");
    gets (palavra);
    tam = strlen (palavra); // tam armazenará o tamanho da string
    for (i = tam-1; i>=0; i--){
          palavra_invertida [j] = palavra [i]; 
          j++;
    }
    palavra_invertida [j] = '\0';
    if  (strcmp (palavra, palavra_invertida) == 0){
    	  printf ("\n A palavra e um palindromo!");	
	}
    else {
    	printf ("\n A palavra e nao palindromo!");	
	}  
    system ("PAUSE");
    return 0;
    
}
