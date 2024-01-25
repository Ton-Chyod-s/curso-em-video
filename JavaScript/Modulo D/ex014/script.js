function carregar() {
    var agora = new Date()
    var hora = agora.getHours()
    var p01 = document.getElementById('pg01') 
    var img = window.document.getElementById('imagem')
    
    p01.innerText = `Agora são exatamente ${hora} Horas!`
    
    if (hora >=0 && hora < 12) {
        document.body.style.background = '#BD7E8D'
        img.src = 'manhã.jpg'
    } else if (hora >= 12 && hora < 18) {
        document.body.style.background = '#592D11'
        img.src = 'tarde.jpg'
    } else {
        img.src = 'noite.jpg'
        document.body.style.background = '#362943'
    }
}

