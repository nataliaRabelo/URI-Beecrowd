def lerNumero():
    numero = int(input())
    if (valorEhValido(numero) == True): # tudo ok, fera
        return numero; # show
    else:
        return lerNumero(); # deu merda. volte 1 casa e tente ler de novo.
        
def valorEhValido(valor):
    return valor < 50;

def printarLista(lista):
    for i in range(len(lista)):
        print('N['+ str(i) +'] = ' + str(lista[i]))
    
numeroLido = lerNumero();
lista = [];
lista.append(numeroLido);

for i in range(9):
    lista.append(lista[i]*2)

printarLista(lista)