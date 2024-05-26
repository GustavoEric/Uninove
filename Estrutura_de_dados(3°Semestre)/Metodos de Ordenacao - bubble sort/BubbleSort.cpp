#include <stdio.h>
#include <stdlib.h>
#define limite 10

int main (){	
	int numeros [limite]= {2,5,3,1,8,9,7,3,5,10};
	int x,y;
	int temp;
	for(x=0;x<limite;x++){
		for(y=0;y<limite;y++){
			if(numeros[y]>numeros[y+1]){
				temp=numeros[y];
				numeros[y]=numeros[y+1];
				numeros[y+1] = temp;
			}
		}
	}
	printf("1: %i\n",numeros[0]);
	printf("2: %i\n",numeros[1]);
	printf("3: %i\n",numeros[2]);
	printf("4: %i\n",numeros[3]);
	printf("5: %i\n",numeros[4]);
	printf("6: %i\n",numeros[5]);
	printf("7: %i\n",numeros[6]);
	printf("8: %i\n",numeros[7]);
	printf("9: %i\n",numeros[8]);
	printf("10: %i\n",numeros[9]);
	return 0;
	 
}
