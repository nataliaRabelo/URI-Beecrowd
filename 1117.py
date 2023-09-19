def checarValor(val): # 1
    try:
        numero = float(val)
        
        #if(numero >= 0 and numero <= 10)
        #    return True;
        #else:
        #    return False;
        # o código acima é a MESMA coisa que a linha abaixo
        return numero >= 0 and numero <= 10;
        
    except Exception:
        return False;
        
valores = []

while(len(valores) < 2): #enquanto houver menos que 2 elementos no meu array.....faça:
    
    numeroLido = input() #ler numero - (1)
    valorEhValido = checarValor(numeroLido) #verificar se numero é inválido - (2)
    
    if(valorEhValido): #(se e somente se valor for válido) - 3
        valorConvertidoParaFloat = float(numeroLido)
        valores.append(valorConvertidoParaFloat) #adicionar o valor ao array de valores
    else:
        print('nota invalida');

def calcularMedia(a, b):
    return (a + b) / 2
    
resultado = calcularMedia(valores[0], valores[1])

print('media = {0:.2f}'.format(resultado))