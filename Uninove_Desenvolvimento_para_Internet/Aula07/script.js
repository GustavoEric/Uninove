selectUf = document.getElementById('selectUf')
    fetch('cidades.json')
    .then(response => response.json())
        .then(estados =>{
            form.innerHTML = ""
            estados.map(estado =>{
                const optEstados = document.createElement("option")
                optEstados.setAttribute('value', estado.uf);
                optEstados.innerText = estado.uf
                selectUf.appendChild(optEstados)
                
            })
    })
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