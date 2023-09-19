def lerInputColuna():
#{
    resultado = int(input())
    if(resultado < 0 or resultado > 11): # se for inválido..... 
    #{
        return lerInputColuna() # tente novamente
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
    for i in range(tamanhoColuna):
   #{
        arrayAuxiliarQueSeRenovaACadaIteracao = []
        for j in range(tamanhoLinha):
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

def realizarOperacao(tabuleiroDaFuncao, devoTirarMediaDaFuncao, colunaASerAnalisada):
#{
    resultadoSoma = 0
    for i in range(len(tabuleiro)):
    #{
        for j in range(len(tabuleiro[i])):
        #{    
            if(j == colunaASerAnalisada): # se isso é verdade, então eu já tô dentro da coluna q eu quero
            #{
                meuElementoNaPosicao_linha_coluna = tabuleiroDaFuncao[i][j]
                resultadoSoma = resultadoSoma + meuElementoNaPosicao_linha_coluna
            #}
        #}
    #}      
    if(devoTirarMediaDaFuncao):
        resultadoSoma = resultadoSoma / len(tabuleiroDaFuncao)
    return resultadoSoma
#}

colunaQueVouAnalisar = lerInputColuna()
devoTirarMedia = ehSoma() == False
tabuleiro = construirTabuleiro(12, 12)

resultadoDaOperacao = realizarOperacao(tabuleiro, devoTirarMedia, colunaQueVouAnalisar)

print("{:.1f}".format(resultadoDaOperacao))