def lerValor():
    valor = int(input())
    while valor <= 0:
        valor.append(valor)
    return valor

def divisores(valorOriginalQueEuDigiteiNoInicioLa): # 20
    resultado = []
    for i in range(valorOriginalQueEuDigiteiNoInicioLa +1):
        if(i > 0):
            restoDaDivisao = valorOriginalQueEuDigiteiNoInicioLa % i;
            if(restoDaDivisao == 0):
                resultado.append(i); # é divisor!
    return resultado;

valorLido = lerValor()
resultado = divisores(valorLido)

limite = len(resultado)

for i in range(limite):
    print(resultado[i])