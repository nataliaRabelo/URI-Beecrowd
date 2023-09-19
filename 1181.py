def lerInputLinha():
#{
    resultado = int(input())
    if(resultado < 0 or resultado > 11): # se for inválido..... 
    #{
        return lerInputLinha() # tente novamente
    #}
    return resultado
#}

def lerElementoDoTabuleiro():
    try:
        resultado = float(input())
        return resultado;
    except EOFError as e : pass

def ehSoma():
    resultado = input()
    if(resultado == 'S'):
        return True;
    elif(resultado == 'M'):
        return False;
    else:
        return ehSoma()

def construirTabuleiro(tamanhoLinha, tamanhoColuna):
#{
    resultado = [];
    for i in range(tamanhoLinha):
   #{
        arrayAuxiliarQueSeRenovaACadaIteracao = []
        for j in range(tamanhoColuna):
        #{
            novoNumeroDoTabuleiro = lerElementoDoTabuleiro()
            arrayAuxiliarQueSeRenovaACadaIteracao.append(novoNumeroDoTabuleiro)
        #}
        resultado.append(arrayAuxiliarQueSeRenovaACadaIteracao)
   #}
    return resultado;
#}         

def printarTabuleiroBonitinho(tabuleiro):
    for i in range(len(tabuleiro)): #percorrer verticalmente (linhas)
        print(tabuleiro[i]) # printar linha toda

def realizarOperacao(tabuleiroDaFuncao, devoTirarMediaDaFuncao, linhaASerAnalisada):
#{
    resultadoSoma = 0
    for indiceLinha in range(len(tabuleiro)):
    #{
        if(indiceLinha == linhaASerAnalisada):
        #{
            minhaLinhaTodaComoArray = tabuleiroDaFuncao[indiceLinha]
            for elementoDaLinha in minhaLinhaTodaComoArray:
            #{
                resultadoSoma = resultadoSoma + elementoDaLinha
            #}
            if(devoTirarMediaDaFuncao):
                resultadoSoma = resultadoSoma / len(minhaLinhaTodaComoArray)
            return resultadoSoma
        #}
    #}      
#}

linhaQueVouAnalisar = lerInputLinha()
devoTirarMedia = ehSoma() == False
tabuleiro = construirTabuleiro(12, 12)

resultadoDaOperacao = realizarOperacao(tabuleiro, devoTirarMedia, linhaQueVouAnalisar)

print("{:.1f}".format(resultadoDaOperacao))