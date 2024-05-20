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
 
void operafila()
{
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
        switch (opc)
        {
            case 1: // Insere elementos na fila
                if( cheia() )
                { 
                    printf("Numero maximo de elementos atingido\n");
                    getch();
                }
                else
                {
                    printf("Digite o %i elemento da fila: ", i + 1);
                    scanf("%d", &elementos[i]);
                    i++;
                    fim++;
                }
                break;
            case 2: 
                elementos[inicio] = 0;
                inicio ++;
                if( inicio == fim ) 
                {
                    inicio = 0;
                    fim = 0;
                }
                break;
            case 3: // Lista fila
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
                break;
        }
    }while( opc != 0); 
}
 
void inicializa()
{
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
