numeroPergunta=20
// numeroPergunta=1
redes = 0
programacao = 0
design = 0
seguranca = 0
const form = document.querySelector('#formTI')
function carregar(id){
    fetch('perguntas.json')
    .then(response => response.json())
        .then(perguntas =>{
            const quantidadePerguntas = document.querySelector('h1')
            quantidadePerguntas.innerHTML ="Perguntas "+ id+"/20"
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
        // alert("Errado")
        proxima.disabled = false

    }
    else{
        // alert("Certo")
        proxima.disabled = false
        if(numeroPergunta<6){
            redes+=1
        }
        else if(numeroPergunta>5 && numeroPergunta<11){
            programacao+=1
        }
        else if(numeroPergunta>10 && numeroPergunta<16){
            design+=1
        }
        else{
            seguranca+=1
        }
        console.log(redes)
        console.log(programacao)
        console.log(design)
        console.log(seguranca)
    }
    }
    catch{
        // alert('Responda')
        botao.disabled = false
    }
});
proxima.addEventListener("click", function () {
        botao.disabled = false
        proxima.disabled = true
        numeroPergunta+=1
        if (numeroPergunta <=20){
            carregar(numeroPergunta)
        }
        else{
            form.innerHTML= ""
            botao.remove()
            proxima.remove()
            if(redes > programacao && redes > design && redes >seguranca){
                vocacao = "Redes"
            }
            else if(programacao > redes && programacao > design && programacao >seguranca){
                vocacao = "Programação"
            }
            else if(design > redes && design > programacao && design >seguranca){
                vocacao = "Design"
            }
            else if(seguranca > redes && seguranca > programacao && seguranca >design){
                vocacao = "Segurança"
            }
            const pontuacaoTotal = document.createElement("p")
            const Desempenho = document.createElement("div")
            pontuacaoTotal.innerHTML = redes+programacao+design+seguranca+"/20"
            const pontuacaoRedes = document.createElement("p")
            pontuacaoRedes.innerHTML = redes+"/5"
            const pontuacaoProgramacao = document.createElement("p")
            pontuacaoProgramacao.innerHTML = programacao+"/5"
            const pontuacaoDesign = document.createElement("p")
            pontuacaoDesign.innerHTML = design+"/5"
            const pontuacaoSeguranca = document.createElement("p")
            pontuacaoSeguranca.innerHTML = seguranca+"/5"
            form.appendChild(pontuacaoTotal)
            Desempenho.appendChild(pontuacaoRedes)
            Desempenho.appendChild(pontuacaoProgramacao)
            Desempenho.appendChild(pontuacaoDesign)
            Desempenho.appendChild(pontuacaoSeguranca)
            form.appendChild(Desempenho)
            alert(vocacao)
        }
});