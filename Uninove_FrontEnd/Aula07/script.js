function validar(usuario,senha){
    if (usuario == 'admin'  && senha == 'uninove'){
        console.log('a')
        window.location.href = 'http://facebook.com'
    }
    else{
        console.log('a')
        alert('Usuario ou senha Invalidos');    
    }
}
function lembrar(){
    principal = document.getElementById('principal').innerHTML='<div id="Lembrasenha">Usuario: admin <br> Senha: uninove</div>'
}
function alterar(bt){
    principal = document.querySelector('main')
    console.log(principal)
    if (bt == 'missao'){
        principal.innerHTML= '<h2>Missão</h2><p>A proposta pedagógica do Colégio UNINOVE privilegia o ensino enquanto construção do conhecimento, o desenvolvimento pleno das potencialidades e habilidades dos alunos e sua inserção no ambiente social estimulando, sobretudo a reflexão, a pesquisa e o debate, trabalhados em sua contextualização</p>'
    }
    else{
        principal.innerHTML= '<h2>Cursos</h2><p>Os cursos de saúde da UNINOVE promovem uma rápida empregabilidade pela excelência de sua formação conceitual e prática, em seus laboratórios de simulação realística e atendimento multiprofissional em clínicas próprias, qualificando profissionais para os cuidados diagnósticos e preventivos de saúde, atendimento pacientes crônicos, acidentados, idosos, atendimento domiciliar, em uma vasta rede de clínicas e hospitais.</p>'
        
    }
}
function alternarModo(){
    modo = document.getElementById('btTest')
    console.log(modo.value)
    console.log(modo.innerContents)
}