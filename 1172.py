def lerNumeros():
    valores = []
    for i in range(10): #vou executar o código abaixo 0 vezes. incrementando [i = i + 1] a cada vez que executar as linhas
        valorLido = input();
        if(valorEhValido(valorLido) == True):
            valores.append(int(valorLido))
        else:
            valores.append(1);
    return valores;


def valorEhValido(valor):
    try:
        if(int(valor) > 0):
            return True;
    except: 
        return False;

numerosLidos = lerNumeros();

for i in range(len(numerosLidos)):
    print('X[' + str(i) + '] = ' + str(numerosLidos[i]));