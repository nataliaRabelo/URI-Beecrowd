leds = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
       #0 #1 #2 #3 #4 #5 #6 #7 #8 #9

def lerQuantidadeDeTestes():
    n = int(input())
    while (n < 1 or n > 2000):
        n = int(input())
    return n

def lerLed():
    n = None
    try:
        n = float(input())
    except :
        pass
    if (n is None or int(n) < 1 or int(n) > 10**100):
        return lerLed()
    return n

qtdTestes = lerQuantidadeDeTestes()

for i in range(qtdTestes):
    meuLedLido = input()
    soma = 0
    for letraDoLed in meuLedLido: #letra do led aqui é uma string
        quantidadeDeLedsDestaLetra = leds[int(letraDoLed)] #buscando no meu array(banco de dados) a quantidade de leds que vou precisar pra construir a letra
        soma = soma + quantidadeDeLedsDestaLetra #é preciso reconverter para int, para usá-lo como índice
    print(str(soma) + ' leds')