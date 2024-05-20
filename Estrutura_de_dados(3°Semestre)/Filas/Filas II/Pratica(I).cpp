#include <stdio.h>
#include <stdlib.h>
#define MAX 10  // Numero maximo de elementos da fila
 
void operafila();
int elementos[MAX], inicio = 0, fim = 0, i = 0;

int main(int argc, char *argv[]) 
{
    inicializa();
     
    operafila();
    return 0;
}
void operafila(){
	int opc = 0;
    int a;
    do
    {
        system("cls");
        printf("1 - Inclui elemento na fila\n");
        printf("2 - Exclui elemento da fila\n");
        printf("3 - Lista fila\n");
        printf("0 - Sair da fila\n");
        scanf("%d", &opc);
        
        if(opc ==1){
        	if( cheia() )
                { 
                    printf("Numero maximo de elementos atingido\n");
                    getch();
                }
	            else{
		        	printf("Digite o valor do elemento %i ",i+1);
		        	scanf("%d", &elementos[i]);
		        	i++;
		        	fim++;
	        	}
		}
	}
	while(opc!=0){
		
	}
	
}

void inicializa(){
    if( vazia() )
    {
        inicio = 0;
        fim = 0;
    }
}
int vazia()
{
   return inicio == 0 && fim == 0;
}
int cheia()
{
    return (fim >= MAX);
}
