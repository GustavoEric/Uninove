#include<stdio.h>

int main(){
	int inicio,fim;
	printf("Digite um numero de inicio: ");
	scanf("%d",&inicio);
	printf("Digite um numero de fim: ");
	scanf("%d",&fim);
	for(inicio;inicio<=fim;inicio++){
		if(inicio%2!=0){
			printf("Impar: %d \n",inicio);
		}
	}
	return 0;
}
