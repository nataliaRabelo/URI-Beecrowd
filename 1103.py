def verificarSeEhMesmoDia(hora1, minuto1, hora2, minuto2):
    if(hora2 < hora1):
        return False
    elif(hora2 == hora1 and minuto2 <= minuto1):
        return False
    else:
        return True

def calculaResultado(mesmoDia, hora1, minuto1, hora2, minuto2):
    totalMinutosHora1 = hora1*60 + minuto1
    totalMinutosHora2 = hora2*60 + minuto2
    resultado = abs(totalMinutosHora2 - totalMinutosHora1)

    if(mesmoDia == False):
        if(hora2 == 0):
            hora2 = 24
        resultado = ((24*60) - resultado)
    
    return resultado

linhaLidaDoTeclado = input()
SOMA = -1

while(SOMA != 0):

    horas = list(map(int, linhaLidaDoTeclado.split()))

    hora1,minuto1 = horas[0], horas[1]
    hora2,minuto2 = horas[2], horas[3]
    
    SOMA = hora1 + minuto1 + hora2 + minuto2

    if(SOMA != 0):
        mesmoDia = verificarSeEhMesmoDia(hora1, minuto1, hora2, minuto2)
        resultado = calculaResultado(mesmoDia, hora1, minuto1, hora2, minuto2)

        print(resultado)
        linhaLidaDoTeclado = input()
