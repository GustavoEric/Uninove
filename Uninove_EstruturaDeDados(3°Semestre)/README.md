# 08/04 Ponteiros
* Com os ponteiros você define em espaço na memória especifico aonde você irá receber um dados que será alocado em algum espaço na memória assim o ponteiro não espera o dado e sim está esperando o endereço de memória em que ele está apontando
* Exemplo
* int *number
* O ponteiro indica para o endereço da variavel referenciada a ele
* Como nesse Código:
  #include <stdio.h>
  #include <stdlib.h> 
 
 main(){
     int x = 15;
     int *px;
     px = &x;
     printf ("Endereco de memoria de x = %p\n", &x);
     printf ("Conteudo da variavel x por meio do ponteiro px = %d\n", *px);
     printf ("Conteudo da variavel px = %p\n", px);
     printf ("Endereco de memoria de px = %p\n", &px);
     system ("PAUSE");
 }  
