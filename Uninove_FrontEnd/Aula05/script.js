function clickMenu(){
    divMenu = document.getElementById('menuId')
    SpanMenu = document.getElementById('spanMenu')
    //Operador Ternário
    divMenu.style.display = (divMenu.style.display == 'block') ? "none" : "block"
    SpanMenu.innerHTML = (SpanMenu.innerHTML =='☰') ? "&#9747;" : "☰"
    /*if (divMenu.style.display == 'block'){
        SpanMenu.innerHTML ='&#9776;'
        divMenu.style.display = ''
        
    }
    else{
        SpanMenu.innerHTML ='&#9747;'
        divMenu.style.display = 'block'
    }*/
}