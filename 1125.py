G, P = map(int, input().split())
while (G != 0 and P != 0):
    def somarColunasDePontos(todas_as_corridas, posicao_do_player, sistema_de_pontuacao):
        pontos = 0
        for corrida in todas_as_corridas:
            posicao_do_jogador_na_corrida = corrida[posicao_do_player]
            if(posicao_do_jogador_na_corrida <= sistema_de_pontuacao[0]):
                pontos += sistema_de_pontuacao[posicao_do_jogador_na_corrida]
        return pontos
        

    corridas = []
    sistemas_pontuacao = []
    pontos_totais = []

    for p in range(P):
        pontos_totais.append([p,0])

    for i in range(G):
        linhaLida = list(map(int, input().split()))
        corridas.append(linhaLida)

    qtd_sistemasDePontuacao = int(input())
    for i in range(qtd_sistemasDePontuacao):
        linhaLida = list(map(int, input().split()))
        sistemas_pontuacao.append(linhaLida)
    

    for sistema in sistemas_pontuacao:
        jogador_vencedor_desse_sistema = None
        pontos_jogador_vencedor_desse_sistema = None
        todos_os_pontos = []
        for player in range(P):
            qtd_pontos_vencedor = somarColunasDePontos(corridas, player, sistema)
        #{
            if(pontos_jogador_vencedor_desse_sistema is None or qtd_pontos_vencedor > pontos_jogador_vencedor_desse_sistema):
            #{
                jogador_vencedor_desse_sistema = player + 1
                pontos_jogador_vencedor_desse_sistema = qtd_pontos_vencedor
            #}
            todos_os_pontos.append([player, qtd_pontos_vencedor])
        #}
        #print(jogador_vencedor_desse_sistema)
    
        vencedores = []
        for i in range(len(todos_os_pontos)):
            if(todos_os_pontos[i][1] == pontos_jogador_vencedor_desse_sistema):
                vencedores.append(todos_os_pontos[i][0])
    
        for i in range(len(vencedores)):
            print(vencedores[i] + 1, end = "")
            if(i < len(vencedores) - 1):
                print(" ", end="")
            else:
                print("")
    G, P = map(int, input().split())
    
