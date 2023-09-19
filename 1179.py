def printarMeuArray(ehPar, lista):
    for i in range(len(lista)):
        if(ehPar):
            palavra = 'par'
        else:
            palavra = 'impar'
        print(palavra + '[' + str(i) + '] = ' + str(lista[i]))

def lerValores(pares, impares):
    for i in range(15):
        valorLido = int(input())
        if(valorEhPar(valorLido)):
            pares.append(valorLido)
        else:
            impares.append(valorLido)
        if(len(pares) == 5):
            printarMeuArray(ehPar = True, lista = pares)
            pares = []
        if(len(impares) == 5):
            printarMeuArray(ehPar = False, lista = impares)
            impares = []
    
    if(len(impares) > 0):
        printarMeuArray(ehPar = False, lista = impares)
        impares = [];
    if(len(pares) > 0):
        printarMeuArray(ehPar = True, lista = pares)
        pares = [];
    
    return None

def valorEhPar(valorLido):
    try:
        if(int(valorLido) % 2 == 0):
            return True
    except:
        return False

pares = []
impares = []
lista = lerValores(pares, impares)