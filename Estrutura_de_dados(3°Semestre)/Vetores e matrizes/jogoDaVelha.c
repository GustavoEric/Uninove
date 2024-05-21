#include <stdio.h>
#include <stdlib.h>
#define limite 3
int jogoDaVelha[limite][limite]; // Declaracao de matriz com 3x3 
int main(){
	int fim=1;
	carregar(jogoDaVelha);
	do{
	int posicaoy;
	char posicaox;
	printf("Escolha a Posicao entre A,B,C \n");
	scanf("%s",&posicaox);
	printf("Escolha o Numero:");
	scanf("%i",&posicaoy);
	posicaoy--;
	printf("%i",posicaoy);
	if(posicaox == 'A'){
		printf("Escolheu A\n");
		jogoDaVelha[0][posicaoy]=1;
		exibir(jogoDaVelha);
	}
	else if(posicaox == 'B'){
		printf("Escolheu B\n");
		jogoDaVelha[1][posicaoy]=1;
		exibir(jogoDaVelha);
	}
	else if(posicaox == 'C'){
		printf("Escolheu C\n");
		jogoDaVelha[2][posicaoy]=1;
		exibir(jogoDaVelha);
	}
	system("pause");
	
	}
	while(fim!=0);
}
void carregar(int matriz[limite][limite]){
	int x,y;
	for(x = 0;x<limite;x++){
		for(y = 0;y<limite;y++){
			matriz[x][y]=0;
			printf("%i",matriz[x][y]);
		}
		printf("\n");
	}
}
void exibir(int matriz2[limite][limite]){
	int x,y;
	for(x = 0;x<limite;x++){
		for(y = 0;y<limite;y++){
			printf("%i",matriz2[x][y]);
		}
		printf("\n");
	}
}
