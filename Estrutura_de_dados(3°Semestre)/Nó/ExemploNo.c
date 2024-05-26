#include <stdio.h>
#include <stdlib.h>

struct no{
	int valor;
	struct no *prox; //ponteiro prox que ira apontar para o proximo no ou para null
};
typedef struct no No; //definindo o tipo assim nao precisamos chamar struct no apenas chamomos No
typedef struct {
	No *inicio; //Ponteiro para o primiro no
}Lista;
void imprimirLista(Lista *l){ //Parametro da funcao e uma lista que recebe um ponteiro porque iremos trabalhar como referencia
	No *aux;
	aux = l->inicio; //recebendo o ponteiro para o primeiro no
	if (aux == NULL){
		printf("LISTA VAZIA");
	}
	else{
		printf("\nValores na LISTA");
		while (aux != NULL){
			printf(" %i ",aux->valor);
			aux = aux->prox; //Variavel auxiliar recebe o prox de no 
		}
	}
}
void buscarNo(Lista *l){
	No *aux;
	aux = l->inicio;
	int valorBuscado,encontrou=0;
	if (aux == NULL){
		printf("Lista Vazia Valor nao Encontrado");
	}
	else{
		printf("Digite o valor Buscado: ");
		scanf("%i",&valorBuscado);
		while (aux != NULL){
			if( valorBuscado == aux->valor){
				printf("Valor %i Encontrado",aux->valor);
				encontrou++;
				break; //Nao roda mais o if se ja encontrou o valor
			} 
			else{
				aux = aux->prox;
				
			}
		}
		if (encontrou == 0){
			printf("Valor nao Encontrado na lista");
		}
	}
}
void main(){
	No *no1,*no2; // criamos as variaveis no1 e no2 como ponteiros por conta do malloc que sempre retorna um ponteiro 
	//porque o malloc cria uma area e retorna um ponteiro para aquela area
	Lista l;
	
	//Criando areas dinamicamente baseado no tamanho da struct No
	no1 = malloc(sizeof(No));
	no2 = malloc(sizeof(No));
	
	//Preenchendo no
	no1->valor = 10;
	// Utilizamos -> por conta que a variavel no1 e um ponteiro
	no2->valor = 20;
	no1->prox = no2;
	//Aqui dizemos que o proximo do no1 aponta para o no2
	no2->prox = NULL;
	//Aqui dizemos que o proximo do no2 aponta para NULL por nao existir mais nenhum no depois dele
	l.inicio = no1;
	//Depois o l.inicio aponta para o primeiro elemento da nossa lista
	buscarNo(&l);
	imprimirLista(&l);
}
