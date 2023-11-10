selectUf = document.getElementById('selectUf')
selectCidade = document.getElementById('selectCidade')
botaoEnviar = document.getElementById('btnEnviar')
fetch('uf.json')
    .then(response => response.json())
        .then(estados =>{
            estados.map(estado =>{
                const optEstados = document.createElement("option")
                optEstados.setAttribute('value', estado.uf);
                optEstados.setAttribute('name', "optEstado");
                optEstados.innerText = estado.estado
                selectUf.appendChild(optEstados)
                
            })
    })

selectUf.addEventListener("change", function () {
    optEstado = selectUf.options[selectUf.selectedIndex].value;
    console.log(optEstado)
    selectCidade.disabled = false
    buscarCidades(optEstado)

})
function buscarCidades(uf){
    selectCidade.innerHTML= ""
    fetch('cidades.json')
    .then(response => response.json())
        .then(cidades =>{
            cidades.map(cidade =>{
                if (cidade.uf == uf){
                    const optCidades = document.createElement("option")
                    optCidades.setAttribute('value', cidade.cidade);
                    optCidades.setAttribute('name', "optCidade");
                    optCidades.innerText = cidade.cidade
                    selectCidade.appendChild(optCidades)
                }
                
            })
    })
}
addAluno("gustavo","guga1234","franco","sp")
function addAluno(nome,senha,cidade,uf){
    ra = Math.floor(Math.random() * 9999999) + 100000;
    const AlunoObjeto = {
        Nome:nome,
        RA: ra,
        Senha: senha,
        Cidade:cidade,
        UF:uf
      };
      console.log(AlunoObjeto)
}