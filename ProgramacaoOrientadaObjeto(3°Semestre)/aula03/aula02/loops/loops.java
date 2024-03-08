/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
public class Main
{
	public static void main(String[] args) {
	    for(int i =0;i<=40;i++){
	        if(i%2>0){
	            System.out.println("Impar: "+i);       
	        }
	    }
	    String nomes[] = { "Marcos", "Leo", "Gus"}; 
	    
	    //Comparação de for que seria semelhanda ao for in com for normal mostrando itens de um array
	    /*
	    */
	    for(String nome : nomes){
	        System.out.println("Loop 1: "+nome);    
	    }
	    int x = 0;
	    while(x<=10){
	        System.out.println("Loop 2: "+x);      
	        x++;
	    }
	}
}
