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

        if (radioSex[0].checked) {
            genero = 'Homen'
            if (idade >= 1 || idade < 6) {
            } else if (idade >= 16 || idade < 18) {
                alert(`${idade} adolescente`)
    
            } else if (idade >= 18 || idade < 65) {
                alert(`${idade} adulto`)
                
            } else {
                alert(`${idade} idoso`)
            }
        } else if (radioSex[1].checked) {
            genero = 'Mulher'

        } 
        resposta.innerText = `detectamos ${genero} de ${idade}`
        
    }
    }
