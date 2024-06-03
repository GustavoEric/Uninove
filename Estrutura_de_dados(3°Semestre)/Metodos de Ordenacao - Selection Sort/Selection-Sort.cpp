#include <stdio.h>
#include <stdlib.h>
void selecao(int vet[],int n){
	int menor,aux;
	for(int i=0;i<n-1;i++){ // Aqui o nosso loop vai ate o penultimo numero do vetor
		for(int j=i+1;j<n;j++){ // E aqui o nosso loop vai ate o ultimo numero do vetor mas comeca pelo segundo valor assim eliminando comparacoes desnecessarias
			menor=i;
			if (vet[menor]>vet[j]){
				menor=j;
			}
			if (i!=menor){
				aux = vet[i];
				vet[i] = vet[menor];
				vet[menor] = aux;
			}
		}
	}
	
}
int main(){
	int n = 10;
	int Vetor[n]={1,6,3,9,3,2,56,2,1,3};
	selecao(Vetor,n);
	for(int i=0;i<n;i++){
		printf("%d - ",Vetor[i]);
	}
	system("pause");
	return 0;
}
