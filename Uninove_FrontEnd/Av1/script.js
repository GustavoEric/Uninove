numeroPergunta=1
redes = 0
function carregar(id){
    fetch('perguntas.json')
    .then(response => response.json())
        .then(perguntas =>{
            const form = document.querySelector('#formTI')
            const quantidadePerguntas = document.querySelector('h1')
            quantidadePerguntas.innerHTML ="Perguntas "+ id+"/15"
            form.innerHTML = ""
            perguntas.map(pergunta =>{
                if(pergunta.id == id){
                    const img = document.createElement("img")
                    img.src = "imagens/img2.png"
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
                    form.appendChild(img)
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
    botao.disabled = true
    respostaRdb = document.querySelectorAll('[name="alt"]')
    try{
    resposta = document.querySelector('[name="alt"]:checked').value

    if (resposta!=alternativaCorreta){
        alert("Errado")
        proxima.disabled = false

    }
    else{
        alert("Certo")
        proxima.disabled = false
        if(numeroPergunta<6){
            redes+=1
        }
        console.log(redes)
    }
    }
    catch{
        alert('Responda')
    }
});
proxima.addEventListener("click", function () {
        botao.disabled = false
        proxima.disabled = true
        numeroPergunta+=1
        carregar(numeroPergunta)
});