function selecionar(img){
    //divmax = document.getElementById('max').getAttribute('img')
    if (img ==1){
        document.getElementById('img1').style.animation='none'
        img1 = document.getElementById('img1').style.display=''
        img2 = document.getElementById('img2').style.display='none'
        img3 = document.getElementById('img3').style.display='none'
    }
    else if (img ==2){
        img1 = document.getElementById('img1').style.display='none'
        document.getElementById('img2').style.animation='none'
        img2 = document.getElementById('img2').style.display=''
        img3 = document.getElementById('img3').style.display='none'
    }
    else if (img==3){
        img1 = document.getElementById('img1').style.display='none'
        img2 = document.getElementById('img2').style.display='none'
        document.getElementById('img3').style.animation='none'
        img3 = document.getElementById('img3').style.display=''
    }
    else{
        document.getElementById('img1').style.animation=''
        document.getElementById('img2').style.animation=''
        document.getElementById('img3').style.animation=''
        img1 = document.getElementById('img1').style.display=''
        img2 = document.getElementById('img2').style.display=''
        img3 = document.getElementById('img3').style.display=''
    }

}