qtdTestes = int(input())

def jaPulou(carneiro, lista):
    for c in lista:
        if c == carneiro:
            return True
    return False

for i in range(qtdTestes):
    qtdCarneirinhos = int(input())
    carneirinhosQuePularam = input().split()
    listaCarneirinhosDistintos = len(list(set(carneirinhosQuePularam)))
    
    print(listaCarneirinhosDistintos)