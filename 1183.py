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

def construirArrayResultante(arrayOriginal):
    posicaoLinha = 0
    resultado_array = []
    for posicaoColuna in range(len(arrayOriginal[posicaoLinha]) - posicaoLinha - 1): # percorrer um caminho com tamanho_total - posicao_atual [12-0 = 12 elementos]..[12-1 = 11 elementos]..[12-2]....
        tamanhoADireita = len(arrayOriginal[posicaoColuna])
        for colunaAtual in range(posicaoLinha+1, tamanhoADireita): # percorrer os elementos à direita da diagonal
            #começando da posição da linha atual/coluna, sempre pulando a diagonal. (por isso o posicaoLinha+1)
            #posicaoLinha é a posição do elemento da diagonal atual
            if(colunaAtual < len(arrayOriginal[posicaoColuna])): # verificação para não extrapolar meu array. vou percorrer tudo à minha direita, desde q eu não extrapole meu array
                resultado_array.append(arrayOriginal[posicaoLinha][colunaAtual])
        posicaoLinha = posicaoLinha + 1; #forçando a sempre pular linha e coluna ao mesmo tempo. De modo a obter a posição da minha diagonal. 
    return resultado_array               #O primeiro for pula as colunas. E essa linha de cód. força eu pular a linha

def printarResultado(ehMedia, arrayResultante):
    resultado = sum(arrayResultante)
    if(ehMedia == True):
        resultado = resultado / len(arrayResultante)
    print("{:.1f}".format(resultado))

devoTirarMedia = ehSoma() == False
tabuleiro = construirTabuleiro(12, 12)
tabuleiro = construirArrayResultante(tabuleiro)
printarResultado(devoTirarMedia, tabuleiro)