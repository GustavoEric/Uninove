import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner ler = new Scanner(System.in);
        double salario, resultado = 0;
        int porcentagemDesconto = 0;
        System.out.println("Digite um Salário");
        salario = ler.nextDouble();
        if (salario >= 5000 && salario <= 7000) {
            resultado = salario - (salario * 0.18);
            porcentagemDesconto = 18;
        } else if (salario >= 2000 && salario <= 5000) {
            resultado = salario - (salario * 0.09);
            porcentagemDesconto = 9;
        } else if (salario >= 1500 && salario <= 2000) {
            resultado = salario;
            porcentagemDesconto = 0;
        }
        System.out.println("Valor sem Desconto: " + salario + "\nValor com Desconto: " + resultado
                + "\nPorcentagem de Desconto " + porcentagemDesconto + "%");
    }
}
