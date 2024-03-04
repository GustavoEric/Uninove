#include <stdio.h>

int main(void) {
	int x,y,divisoes;
	for(x=0;x<=1000;x++){
		for(y-0;y<=x;y++){
			if(y%2!=0){
				if (y%x==0){
					divisoes +=1;
				}
			}
			if(divisoes ==0){
							printf("Primos %d",y);
				}
		}
		printf("%d ",divisoes);
		divisoes=0;
		
	}
	return 0;
}
