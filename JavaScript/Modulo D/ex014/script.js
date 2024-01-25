var agora = new Date()
var hora = agora.getHours()
var p01 = document.getElementById('pg01') 

p01.innerText = `Agora são exatamente ${hora} Horas!`

if (hora < 12) {
    document.body.style = 'red'
} else if (hora >= 18) {
    document.body.style = 'back'
} else {
    
}