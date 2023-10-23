numeroPergunta=1
function carregar(id){
    fetch('perguntas.json')
    .then(response => response.json())
        .then(perguntas =>{
            const form = document.querySelector('#formTI')
            perguntas.map(pergunta =>{
                if(pergunta.id == id){
                    const Perguntalbl = document.createElement("label")
                    Perguntalbl.innerHTML = pergunta.pergunta
                    
                    const altA = document.createElement("p")
                    altA.innerHTML = pergunta.alternativaA
                    rdbA = document.createElement('input')
                    rdbA.setAttribute('type', 'radio');
                    rdbA.setAttribute('name', 'alt');
                    rdbA.setAttribute('value', 'A');

                    const altB = document.createElement("p")
                    altB.innerHTML = pergunta.alternativaB
                    rdbB = document.createElement('input')
                    rdbB.setAttribute('type', 'radio');
                    rdbB.setAttribute('name', 'alt');
                    rdbB.setAttribute('value', 'B');

                    const altC = document.createElement("p")
                    altC.innerHTML = pergunta.alternativaC
                    rdbC = document.createElement('input')
                    rdbC.setAttribute('type', 'radio');
                    rdbC.setAttribute('name', 'alt');
                    rdbC.setAttribute('value', 'C');

                    const altD = document.createElement("p")
                    altD.innerHTML = pergunta.alternativaD
                    rdbD = document.createElement('input')
                    rdbD.setAttribute('type', 'radio');
                    rdbD.setAttribute('name', 'alt');
                    rdbD.setAttribute('value', 'D');

                    // alert(pergunta.pergunta)
                    // alert(pergunta.alternativaA)
                    // alert(pergunta.alternativaB)
                    // alert(pergunta.alternativaC)
                    // alert(pergunta.alternativaD)
                    alternativaCorreta = pergunta.correta
                    form.appendChild(Perguntalbl)
                    altA.appendChild(rdbA)
                    form.appendChild(altA)
                    altB.appendChild(rdbB)
                    form.appendChild(altB)
                    altC.appendChild(rdbC)
                    form.appendChild(altC)
                    altD.appendChild(rdbD)
                    form.appendChild(altD)
                }
            })
    })
}
carregar(numeroPergunta)
botao = document.querySelector('#responder')
proxima = document.querySelector('#proxima')

botao.addEventListener("click", function () {
    resposta = document.querySelector('[name="alt"]:checked').value

    if (resposta!=alternativaCorreta){
        alert("Errado")
        proxima.disabled = false
        resposta.disabled = true
    }
    else{
        alert("Certo")
        proxima.disabled = false
    }
});
proxima.addEventListener("click", function () {
        proxima.disabled = true
        numeroPergunta+=1
        carregar(numeroPergunta)
});