def lerEnigmas():
    listaDeEnigmas = []
    teste = int(input())
    for enigmaPaula in range(teste):
        enigmaPaula = input()
        listaDeEnigmas.append(enigmaPaula)
    return listaDeEnigmas

def resolverEnigmas(listaDeEnigmas):
#{
    for linha in listaDeEnigmas:
    #{
        numero1 = int(linha[0])
        letra = linha[1]
        numero2 = int(linha[2])
        resultado = None
        if (numero1 == numero2):
        #{
            resultado = numero1 * numero2
        #}
        elif (letra.islower() == True):
        #{
            resultado = numero1 + numero2
        #}
        else:
        #{
            resultado = numero2 - numero1 
        #}
        print(resultado)
    #}
    
#}

enigmasLidos = lerEnigmas()
resolverEnigmas(enigmasLidos)

