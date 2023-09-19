def escreverPalavrasCombinadas(qtdLinhas):
    for i in range (qtd):
        linha = input().split()
        listaOrdenada = sorted(linha, key = len)
        tamanhoPalavraMaior = len(listaOrdenada[len(linha) -1 ])
        resultado = ''
        for j in range (tamanhoPalavraMaior):
            for palavra in linha:
                if (j < len(palavra)):
                    resultado += palavra[j]

        print(resultado)


qtd = int(input())
escreverPalavrasCombinadas(qtd)