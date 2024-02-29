#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Pessoa{
	char nomePessoa[20];
    int idadePessoa;
    double pesoPessoa;
    
    void message(){
    	printf("Dados Cadastrados \n\n");
	    printf("Nome: %s\n",nomePessoa);
	    printf("Idade: %d\n Anos",idadePessoa);
	    printf("Peso: %.2lf Kilos\n",pesoPessoa);
	    printf("Idade Objeto: %d\n",idadePessoa);
	}
};
main(){
	int inicio,limite;
	//Referenciando Objeto Pessoa
	struct Pessoa pessoa;
	
	//Atribuindo valores no Objeto
    printf("Digite seu nome: ");
    scanf("%[^\n]",&pessoa.nomePessoa);
    printf("Digite sua idade: ");
    scanf("%d",&pessoa.idadePessoa);
    printf("Digite seu peso: ");
    scanf("%lf",&pessoa.pesoPessoa);
   	pessoa.message();
	printf("Voce quer saber os numeros entre: ");
    scanf("%d",&inicio);
    printf("ate: ");
    scanf("%d",&limite);
    
    for (inicio;inicio<=limite;inicio++){
    	if (inicio%2==0){
    		printf("\nPar: %d\n",inicio);
    		
		}
		else{
			printf("\nImpar: %d\n",inicio);
		}
	}
    return 0;
}
