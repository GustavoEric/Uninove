package veiculos;

public class ProgramaPrincipal{
	
	public static void main(String[] args) {
		
		Carro novoCarro = new Carro();
		novoCarro.setMarca("Chevrolet");
		novoCarro.setModelo("Onix");
		novoCarro.setCor("Preto");
		novoCarro.setKm(22350);
		novoCarro.setCapacidadeTanque(45);
		novoCarro.setKmPorLitro(10);
		novoCarro.setPreco(30000);
		
		System.out.println("Marca: " + novoCarro.getMarca());
		System.out.println("Modelo: " + novoCarro.getModelo());
		System.out.println("Cor: " + novoCarro.getCor());
		System.out.println("Km: " + novoCarro.getKm());
		System.out.println("Capacidade Tanque: " + novoCarro.getCapacidadeTanque());
		System.out.println("Km Por Litro: " + novoCarro.getKmPorLitro());
		System.out.println("Rodagem do Veículo: " + novoCarro.calcularKm());
		System.out.println("Preço: " + novoCarro.getPreco());
		System.out.println("Desconto: " + novoCarro.calcularDesconto(2.5,2));
		System.out.println("Valor do Carro: " + novoCarro.getValorComDesconto());
		System.out.println();
		
		Carro novoCarro2 = new Carro();
		novoCarro2.setMarca("Chevrolet");
		novoCarro2.setModelo("Onix");
		novoCarro2.setCor("Preto");
		novoCarro2.setKm(22350);
		novoCarro2.setCapacidadeTanque(45);
		novoCarro2.setKmPorLitro(10);
		novoCarro2.setPreco(30000);
		
		System.out.println("Marca: " + novoCarro2.getMarca());
		System.out.println("Modelo: " + novoCarro2.getModelo());
		System.out.println("Cor: " + novoCarro2.getCor());
		System.out.println("Km: " + novoCarro2.getKm());
		System.out.println("Capacidade Tanque: " + novoCarro2.getCapacidadeTanque());
		System.out.println("Km Por Litro: " + novoCarro2.getKmPorLitro());
		System.out.println("Rodagem do Veículo: " + novoCarro2.calcularKm());
		System.out.println("Preço: " + novoCarro2.getPreco());
		System.out.println("Desconto: " + novoCarro2.calcularDesconto(2.5,2));
		System.out.println("Valor do Carro: " + novoCarro2.getValorComDesconto());
		System.out.println();
		
		Carro novoCarro3 = new Carro();
		novoCarro3.setMarca("Fiat");
		novoCarro3.setModelo("Palio");
		novoCarro3.setCor("Prata");
		novoCarro3.setKm(0);
		novoCarro3.setCapacidadeTanque(47);
		novoCarro3.setKmPorLitro(14);
		novoCarro3.setPreco(33650);
		
		System.out.println("Marca: " + novoCarro3.getMarca());
		System.out.println("Modelo: " + novoCarro3.getModelo());
		System.out.println("Cor: " + novoCarro3.getCor());
		System.out.println("Km: " + novoCarro3.getKm());
		System.out.println("Capacidade Tanque: " + novoCarro3.getCapacidadeTanque());
		System.out.println("Km Por Litro: " + novoCarro3.getKmPorLitro());
		System.out.println("Rodagem do Veículo: " + novoCarro3.calcularKm());
		System.out.println("Preço: " + novoCarro3.getPreco());
		System.out.println("Desconto: " + novoCarro3.calcularDesconto(2.5,2));
		System.out.println("Valor do Carro: " + novoCarro3.getValorComDesconto());
		System.out.println();
		
	}
}

