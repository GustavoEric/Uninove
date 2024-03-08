# IDE utiilizada: 
* `Eclipse`
* o Eclipse tem o conceito de perspectiva que é um conjunto de janelas que faclita em um desenvovimento específico

# Dicas
* Na parte superior direita tem uma janela que se chama open perspective
* iremos trabalha com a janela `JAVA`

# Analogia Orientação Orientada a Objetos
* Pense em uma forma com o bolo e pense na forma como se fosse a Class e o bolo como se fosse o Objeto.

* A Classe pode produzir diversos objetos

# Classe (Class)
* Toda Class tem um nome exemplo (Carro)
* Todo carro tem caracteristicas (Marca,Modelo,Cor ...)
* Está Class irá produzir objetos carro com este formato

# Objeto (Object)

* Quando criamos uma Class as caracteristicas da Class vai para dentro do Object
* Dentro de cada Object são colocadas informações que são informações unicas (os Atributos) que vão para o Banco de Dados

# Exemplo de Funcionamento da Programação Orientada á Objetos

* O usuario acessa a view que seria o FrontEnd aonde ele preenche os dados do carro (marca,modelo,cor)
* Após pressionar o botão de cadastrar é mandada uma solicitação para a classe para criar um objeto carro e dentro do objeto terá as caracteristicas da classe, após isso as informações enviadas pelo usuario são inseridas no Object `carro` 
* Uma vez isso feito agora o próximo passo é enviar o Object para o Banco de Dados
* No Banco de Dados existira a Tabela tbCarro com as colunas (`marca`,`modelo` e `cor`)