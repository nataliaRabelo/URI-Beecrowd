qtd_testes = int(input())

while qtd_testes > 0:
    for x in range(qtd_testes):
        linha = list(map(int, input().split()))
        alternativas = ['A', 'B', 'C', 'D', 'E']
        alternativas_marcadas = []

        for i in range(len(linha)):
            if(linha[i] <= 127):
                alternativas_marcadas.append(alternativas[i])

        if(len(alternativas_marcadas) == 1):
            print(alternativas_marcadas[0])
        else:
            print('*')
    
    qtd_testes = int(input())
