#include <stdio.h>
#include <stdlib.h>

void select_sort(int x[], int n);

int main() {

  int qtde = 0;

  printf("Digite a quantidade de numeros: ");
  scanf("%i", &qtde);
 
  int nums[qtde];
  int I=0;
  for(I = 0; I < qtde; I++){
      printf("Digite o %i* numero: ", I+1);
      scanf("%i", &nums[I]);
  }

  select_sort(nums, qtde);
 
  for(I = 0; I < qtde; I++){
      printf("\nO %i* numero eh %i", I+1, nums[I]);
  }
 
  return 0;
}

void select_sort(int x[], int n)
{
    int i, indice, j, maior;
    for(i= n-1; i> 0; i--)
    {
        maior = x[0];
        indice = 0;
        for (j = 1; j <= i; j++) {
            if (x[j] > maior)
            {
                maior = x[j];
                indice = j;
            }
        }
        x[indice] = x[i];
        x[i]      = maior;
    }
}
