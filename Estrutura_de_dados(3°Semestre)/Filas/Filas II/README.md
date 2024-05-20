# Filas II

* Nesse Exemplo adicionamos uma correção á maneira de exclusão que fizemos no primeiro programa por conta de não ser muito peformatico em relação a mover todos os elemento quando se trata de excluir apenas um 

* visivelmente possa ser que você não veja problemas nisso quando se trata de um programa pequeno mas pense em uma escala maior um array com 100 a 500 elementos a cada elemento que você excluisse seu programa moveria os outros 499 para depois continuar outros processos

* Para resolver isso usamos uma maneira simples, simplesmente dizemos que o inicio do nosso array sera a proxima posição um exemplo:

* ListNum[1,2,3,4] inicio = 0 ListNum[0] == 1

* Quando usamos a função de excluir acontece o seguinte:

* ListNum[0] = 0 inicio ++ assim quando usarmos de novo a função acontecerá o seguinte:

* ListNum[0,2,3,4] inicio = 1 ListNum[1] == 2

* Desta maneira de forma eficiente conseguimos excluir um numero e apenas passamos o inicio para o proximo elemento comparando com o exemplo de existir um array de 500 elementos não iremos mais mover 499 elementos