function gerarTabuada() {
    var numeroTexto = document.getElementById('num').value
    var resposta = document.getElementById('res')
    var tabuada = document.getElementById('selTab')

    if (numeroTexto == 0) {
        alert('[ERRO] informe um número válido')
    } else {
        var numeroInt = Number(numeroTexto)
        for (let c = 0; c < 11; c++) {
            var calculo = numeroInt * c
            let item = document.createElement('option')
            item.text = `${numeroInt} x ${c} = ${calculo}`
            tabuada.appendChild(item)
        }
        
    }
}