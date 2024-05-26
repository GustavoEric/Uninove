O método bolha (bubble sort) é um método de ordenação por trocas. Ele envolve repetidas comparações e, se necessário, a troca de dois elementos adjacentes (SCHILDT, 1995, p. 504). Consiste, em cada etapa, em "borbulhar" o maior elemento para o fim da lista. Veremos a seguir a ilustração desse método. Os seguintes números são para serem colocados em ordem:

8     4     3     9

Vamos verificar o método passo a passo:

![Imagem Exemplo metodo bubble sort](https://img.uninove.br/static/0/0/0/0/0/0/0/1/9/6/7/196721/a03i01_estrdados80_100.png)(compara-se o par 8 com 4)

![Imagem Exemplo metodo bubble sort](https://ead.uninove.br/ead/disciplinas/web/_g/estrdados80_100/imagens/a03i02_estrdados80_100.png)(trocou o par comparado ilustrado e compara-se o próximo par adjacente)

![Imagem Exemplo metodo bubble sort](https://img.uninove.br/static/0/0/0/0/0/0/0/1/9/6/7/196722/a03i03_estrdados80_100.png)(trocou o par comparado anterior e compara-se o próximo par adjacente)

![Imagem Exemplo metodo bubble sort](https://ead.uninove.br/ead/disciplinas/web/_g/estrdados80_100/imagens/a03i07_estrdados80_100.png)(não trocou e, finalmente, acabaram-se as comparações)

Agora, repete-se todo o procedimento e continua assim até que fique tudo ordenado.

![Imagem Exemplo metodo bubble sort](https://img.uninove.br/static/0/0/0/0/0/0/0/1/9/6/7/196724/a03i04_estrdados80_100.png)(trocou o par comparado mostrado)

![Imagem Exemplo metodo bubble sort](https://img.uninove.br/static/0/0/0/0/0/0/0/1/9/6/7/196723/a03i05_estrdados80_100.png)(trocou o par comparado anterior e compara-se o próximo par adjacente)

![Imagem Exemplo metodo bubble sort](https://ead.uninove.br/ead/disciplinas/web/_g/estrdados80_100/imagens/a03i06_estrdados80_100.png)(compara-se o próximo par adjacente)

![Imagem Exemplo metodo bubble sort](https://img.uninove.br/static/0/0/0/0/0/0/0/1/9/6/7/196725/a03i08_estrdados80_100.png) (não trocou e, finalmente, acabaram-se as comparações. Está ordenado)

Clique aqui e veja uma simulação animada do método bolha.

Comentários sobre o método bolha
Ao analisarmos um método de ordenação, devemos levar em conta o número de comparações e trocas que são realizadas para o menor, médio e pior casos. Estes dependem de como estão inicialmente dipostos os números, ou seja, eles podem já estar praticamente ordenados, ou bem desordenados inicialmente. Nesse caso, o esforço para a ordenação seria maior. Para desenvolvermos um programa de computador que implemente esse método são necessários dois laços aninhados (um dentro do outro), de modo que, especificamente para esse método, o número de comparações é sempre o mesmo, porque os dois laços repetem o número especificado de vezes, estando a lista inicialmente ordenada ou não. Isso significa que a ordenação bolha sempre executa Imagem.

Comparações, em que "n" é o número de elementos a ser ordenado (SCHIDT, 1995, p. 504). Não está previsto para esta disciplina explicar a origem dessa fórmula ou aprofundar mais o assunto, mas só para se ter uma noção da problemática dessa complexidade de ordenação, o método bolha é uma ordenação n-quadrática, pois seu tempo de execução é da ordem de n2. Esse tipo de ordem pode ser representada em uma notação que se escreve assim: O(n2). Este tipo de algorítmo é muito ineficiente quando é aplicado a um número muito grande de elementos.

A título de exemplo, ignorando-se as trocas que possam ser feitas e levando-se em conta apenas as comparações, vamos supor que cada comparação leva 0.001s para ser processada. Então, para ordenar 10 elementos são gastos 0.05s; para ordenar 100 elementos serão gastos 5 segundos e para ordenar 100.000 elementos levaria em torno de 5.000.000 de segundos, ou 1.400 hs ou por volta de 2 meses de ordenação (SCHILDT ,1995, p. 506). Isso está bom para você?