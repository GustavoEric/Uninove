# Filas

* As Filas tem carcteristicas de fifo (fist in fist out) ou seja o primeiro que entra é o primeiro que sai
* Podemos considerar isso no exemplo de excluirmos um valor de uma fila o primeiro valor acionado é excluido e assim por diante

* Exemplo: Lista[1,2,3,4,5,6] ExcluirElemento()->Lista[2,3,4,5,6]
* AdicionarElemento()->Lista[ , , , , ] Quando criamos um Array com 5 posições imagine ele assim
* e quando vamos adicionar um valor precisamos referenciar a posição que este valor vai ser colocado no nosso array
* Exemplo: Lista[2] = 3 -> Lista[ , ,3, , ] olhando inicialmente você deve achar que o valor 3 deveria ter sido adicionado na posicão anterior mas quando falamos de array o incio dele começa em **zero** então um array de 5 posições o valor da ultima posição será 4
* MostrarElementos Levando em consideração que o array começa na posição zero usamos isso no comando for para mostrar todos os elementos
* Exemplo for (int i=0;i < limiteArray; i++) digamos que o limite do array é 5 então a ultima posição terá o numero 4
* Por isso dizemos que i < imiteArray por que nessa situação o nosso for irá de 0 até 4 se ultizarmos desta maneira i <= imiteArray
* Nosso for iria de 0 até 5 e não é o que queremos pois quebraria o código