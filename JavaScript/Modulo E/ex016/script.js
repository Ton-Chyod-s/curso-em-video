function contar() {
    var inicio = Number(document.getElementById('inicio').value)
    var fim = Number(document.getElementById('fim').value)
    var passo = Number(document.getElementById('passo').value)
    var divRes = document.getElementById('res')
    
    if (inicio === 0 || fim === 0 || passo === 0) {
        divRes.innerHTML = 'Impossivel contar!'
        //alert('[Erro] faltam dados!!')
        
    } else {
        divRes.innerHTML = 'Contando ...<br> ' 
        if (inicio < fim) {
            for (let c = inicio; c <= fim; c += passo) {
                divRes.innerHTML += `${c} \u{1F449}`
            }
        } else {
            for (let c = inicio; c >= fim; c -= passo) {
                divRes.innerHTML += `${c} \u{1F449}`
            }
        }
        divRes.innerHTML += `\u{1f3c1}`
    } 
}


