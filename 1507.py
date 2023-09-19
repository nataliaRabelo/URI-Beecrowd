def ehSubSequencia(palavra, query):
    idx_query = 0
    for idx_palavra in range(len(palavra)):
    #{
        if(palavra[idx_palavra] == query[idx_query]): #só damos match na query, se os elementos em suas respectivas posições forem iguais
            idx_query += 1
        if(len(query) == idx_query): #é subsequência pois percorremos a query toda. E, se percorremos a query toda, demos match em todos os seus elementos
            return True
    #}
    return False

qtdTestes = int(input())

for i in range(qtdTestes):
    palavraLida = input()
    qtdQueries = int(input())

    for j in range(qtdQueries):
        queryLida = input()
        if(ehSubSequencia(palavraLida, queryLida)):
            print("Yes")
        else:
            print('No')