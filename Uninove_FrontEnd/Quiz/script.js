botao = document.getElementById('btFinalizar')
questao1 = document.getElementsByName('q1')
questao2 = document.getElementsByName('q2')
questao3 = document.getElementsByName('q3')
pontuacao = document.querySelector('#pontuacao')

pontuacao.style.display = 'none'

console.log(pontuacao)
botao.addEventListener("click", function () {
    var pontos = 0;
    if (questao1[1].checked){
        pontos+=3,3
    }
    if(questao2[0].checked){
        pontos+=3,3
    }
    if(questao3[3].checked){
        pontos+=4
    }
    pontuacao.style.display = ''
    pontuacao.innerHTML = ''
    pontuacao.innerHTML += '<p>Pontos</p>'
    pontuacao.innerHTML += '<p>'+pontos+'</p>'
});