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