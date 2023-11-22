resultado = document.getElementById("divResultado")
resultado2 = document.getElementById("divResultado2")

function botao1() {
    resultado.innerHTML= ""
    n1 = document.getElementById("txt1").value
    n2 = document.getElementById("txt2").value
    for (var i=0;i<=n2;i++){
        result = `<p>${n1} X ${i} = ${(n1*i)}</p>`
        console.log(result)
        resultado.innerHTML+=result
        // resultado.style.gridTemplateColumns = "repeat(4,25%)"
    }
}
function botao2() {
    resultado2.innerHTML= ""
    var rows = 1
    n1 = document.getElementById("txt3").value
    n2 = document.getElementById("txt4").value
    final = document.getElementById("txt5").value
    for (n1=n1;n1<=n2;n1++){
        const tabuada = document.createElement("div")
        tabuada.setAttribute('id', "tabuada"+n1);
        for (var i=0;i<=final;i++){
            result = `<p>${n1} X ${i} = ${(n1*i)}</p>`
            console.log(result)
            tabuada.innerHTML+=result
            // console.log(exibir)
            // 
        }
        resultado2.appendChild(tabuada)
    }
    if (n2>10){
        rows= n2/2
        resultado2.style.gridTemplateColumns = (`repeat(${n2},${(100/n2)}%)`)
        // resultado2.style.gridTemplateRows = (`repeat(${n2},${(100/n2)}%)`)
    }
    else{
        resultado2.style.gridTemplateColumns = (`repeat(${n2},${(100/n2)}%)`)
    }

}