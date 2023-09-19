def lerMatrixDoTeclado():
    resultado = []

    for i in range(4):
        linhaLida = input()
        resultado.append(linhaLida)

    return resultado

def pegarF(matrix):
    resultado = ''
    for eixoX in range(len(matrix)):
        resultado += matrix[eixoX][0]
    return int(resultado)

def pegarL(matrix):
    resultado = ''
    for i in range(len(matrix)):
        resultado += matrix[i][len(matrix[i]) - 1]
    return int(resultado)

def decodificarMatrix(F,L, matrix):
#{
    palavra = ''
    for eixoX in range(1,len(matrix[0])-1):
    #{
        elementosNaColuna = ''
        for j in range(len(matrix)):
        #{
            elementosNaColuna += matrix[j][eixoX]
        #}
        colunaAsInteiro = int(elementosNaColuna)
        calculo = ((meuF * colunaAsInteiro) + meuL) % 257
        palavra += chr(calculo)
    #}
    return palavra
#}

matrix = lerMatrixDoTeclado()
meuF = pegarF(matrix)
meuL = pegarL(matrix)

palavraFinal = decodificarMatrix(meuF, meuL, matrix)

print(palavraFinal)