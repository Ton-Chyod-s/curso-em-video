let tabuada = document.getElementById('tab')
let paragrafo = document.getElementById('terceiroParagrafo')
let numTxt = document.getElementById('num')
var resultado = document.getElementById('res')
let valores = []

function inLista (n, l) {
    if (l.indexOf(Number(n) != -1)) {
        return true
    } else {
        return false
    }
}

function isNumero (n) {
    if (Number(n) >= 1 && Number(n) <= 100)  {
        return true
    } else {
        return false
    }
}

function verificar(){
    if (isNumero(numTxt.value) && inLista(numTxt.value, valores)) {
        resultado.innerText = ""
        var item = document.createElement('option')
        item.text = `Valor ${numTxt.value} Adicionado!`
        tabuada.appendChild(item)
        valores.push(Number(numTxt.value))

    } else {
        alert('[ERRO] informe um número válido')
    }
    num.value = ""
    numTxt.focus()
}

function finalizar () {
    if (valores.length == 0) {
        alert('[ERROR] Lista vazia')
    } else {
        var maior = 0;
        for (let i = 0; i < valores.length; i++) {
            if (valores[i] > maior) {
                maior = valores[i]
            }
        }
        var menor = valores[0];
        for (let i = 0; i < valores.length; i++) {
            
            if (valores[i] < menor) {
                menor = valores[i]
            }
        }
        var soma = 0;
        for (let i = 0; i < valores.length; i++) {
            soma += valores[i]
        }

        resultado.innerHTML = `Ao todo temos ${valores.length} números cadastrados.<br><br>O maior valor informado foi ${maior}.<br><br>O menor valor informado foi ${menor}.<br><br>Somando todos os valores, temos ${soma}.<br><br>A média dos valores digitados é ${(soma / valores.length).toFixed(2)}.`
 
    }
}