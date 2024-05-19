#include <stdio.h>
#include <stdlib.h>
#define limite 5 //Maximo de valores na filla

int main (){
	funcaoFila();
	return 0;
}
void funcaoFila(){
	int opc=0,a=0,fim=0;
	int elementos[limite],inicio=0,i=0;
	do{
		system("cls");
        printf("1 - Inclui elemento na fila\n");
        printf("2 - Exclui elemento da fila\n");
        printf("3 - Lista fila\n");
        printf("0 - Sair da fila\n");
        scanf("%d", &opc);
        
        if (opc == 1){
        	if(i>=limite){
        		 printf("Lista ja Ocupou seu tamnho maximo\n");
        		 	system("pause");
			}
			else{
				printf("Digite o Valor do Ekemento %i",i+1);
        		scanf("%d", &elementos[i]);
        		i++;
        		fim++;
			}
		}
		else if(opc == 2){
			if(i<=0){
        		printf("Nao ha Elementos para serem deletados\n");
        		system("pause");
			}
			else{
				printf("Else");
				printf("Valor i %i",i);
				printf("Valor Fim %i",fim);
				for(i = inicio;i<fim; i++){ //Nesse bloco atribuimos o valor de i com o valor de incio que sera = 0 desta maneira o (i) ira percorrer todo o array ate o fim
//					printf("Else");
					elementos[i] = elementos[i+1]; //aqui atribuimos o valor do elemento anteriao o valor do elemento posterior
					 //Adicionado para que subtraia 1 assim o usuario teria que colocar 5 numeros
				}
				fim--;
				printf("Valor Fim: %i",fim);
					system("pause");
			}			
		}
		else if (opc==3){
			for(a = inicio;a < fim;a++){
				printf("Elemento %i : %i\n",a+1,elementos[a]);
			}
			system("pause");
			
		}
	}
	while(opc != 0);
}
