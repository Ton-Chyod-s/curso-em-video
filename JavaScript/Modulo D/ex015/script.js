function verificar() {
    var data = new Date()
    var anoAtual = data.getFullYear()
    var txtIdade = document.getElementById('txt1')
    var valorIdade = Number(txtIdade.value)
    var resposta = document.getElementById('res')
    var masculino = document.getElementById('masc')
    var idade = anoAtual - valorIdade 
    if (valorIdade < anoAtual) {
        if (idade >= 1 && idade < 6) {
            alert(idade)

        } else if (idade >= 16 && idade < 18) {
            alert(`${idade} adolescente`)

        } else if (idade >= 18 && idade < 65) {
            alert(`${idade} adulto`)
            
        } else {
            alerto(`${idade} idoso`)
        }
    } else {
        alert(`deu algo errado ae`)
    }
}