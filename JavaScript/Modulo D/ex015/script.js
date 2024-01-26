function verificar() {
    var data = new Date()
    var anoAtual = data.getFullYear()
    var txtIdade = document.getElementById('txt1')
    var valorIdade = Number(txtIdade.value)
    var resposta = document.getElementById('res')
    
    if (txtIdade.value == 0 || valorIdade > anoAtual) {
        alert("Veirifique os dados e tente novamente!")
    } else {
        var radioSex = document.getElementsByName('radsex')
        var idade = anoAtual - valorIdade
        var genero = ''
        var img = document.createElement('img')
        img.setAttribute('id','foto')

        if (radioSex[0].checked) {
            genero = 'Homem'
            
            if (idade >= 0 && idade < 10) {
                img.setAttribute('src','bebe.jpg')
                alert(`${idade} criança`)
                document.body.style.background = 'red'
                
            } else if (idade < 21) {
                alert(`${idade} adolescente`)
                img.setAttribute('src','adolescente homen.jpg')
    
            } else if (idade < 50) {
                alert(`${idade} adulto`)
                img.setAttribute('src','homem.jpg')
            } else {
                alert(`${idade} idoso`)
                img.setAttribute('src','senhor.jpg')
            }
        } else if (radioSex[1].checked) {
            genero = 'Mulher'
            if (idade >= 0 && idade < 10) {
                alert(`${idade} criança`)
                img.setAttribute('src','bebe.jpg')

            } else if (idade < 21) {
                alert(`${idade} adolescente`)
                img.setAttribute('src','adolescente mulher.jpg')
    
            } else if (idade < 50) {
                alert(`${idade} adulto`)
                img.setAttribute('src','mulher.jpg')
                
            } else {
                alert(`${idade} idoso`)
                img.setAttribute('src','senhora.jpg')
            }
        }
        resposta.style.textAlign = 'center'
        resposta.innerHTML = `detectamos ${genero} de ${idade} anos.`
        resposta.appendChild(img)
    }
    }
