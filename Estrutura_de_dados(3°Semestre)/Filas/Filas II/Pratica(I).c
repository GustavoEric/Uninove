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
		else if (opc ==2){
			elementos[inicio] = 0; // Aqui zerams o valor do primeiro elemento e a nossa variavel inicio e adicionada +1 assim desconsideramos a posicao zerada 
			inicio++;
			if (inicio == fim){ // quando o incio avancar ate o valor do fim quer dizer que temos apenas um elemento no nosso array
				inicio = 0;
                fim = 0;
			}
		}
		else if (opc==3){
			system("cls");
                int a;
                if( vazia() )
                {
                    printf("A fila esta vazia !!!\n\n\n");
                    getch();
                }
                else
                {
                    for(a = inicio; a < fim; a++) 
                    {
                        printf("%2d%c elemento: %2i\n", a+1, 167, elementos[a]);
                    }
                    getch();
                }
		}
	}
	while(opc!=0);
	
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
