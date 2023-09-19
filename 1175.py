def lerNumeros():
    lista = []
    for i in range(20):
        valorLido = input()
        lista.append(int(valorLido))
    return lista;

numerosLidos = lerNumeros();

for i in range(len(numerosLidos)):
    print('N['+ str(i) +'] = ' + str(numerosLidos[19 - i]))