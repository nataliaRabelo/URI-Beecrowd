#ABCD
#AB
#C
#---------------
#ABEDCS
#
#
#---------------
#EDSMB
#MSD
#A
#---------------
#
#
#
#---------------
#IWANTSODER
#SOW
#RAT
def addMatriz(matriz, letra):
    existe = False
    for elemento in matriz:
        if(elemento[0] == letra):
            existe = True
            elemento[1] += 1
    if(existe == False):
        matriz.append([letra,1])
    
    return matriz

def ehCheater(dieta, cafeDaManha, almoco):
    
    comi = cafeDaManha + almoco
    coisasQueComi = []

    for letra in comi:
        if(letra not in dieta):
            return True
        coisasQueComi = addMatriz(coisasQueComi, letra)
    
    if(len(dieta) == 1):
        if(coisasQueComi[0][1] > 1):
            return True    

    return False

def pegarCoisasQueNaoComi(dieta, cafeDaManha, almoco):
    
    resultado = ''
    tudo = cafeDaManha + almoco

    for letra in dieta:
        if(letra not in tudo):
            resultado += letra
    
    return resultado

qtd_testes = int(input())
for i in range(qtd_testes):
    linhas = []

    for j in range(3):
        linhas.append(input())

    if(ehCheater(linhas[0], linhas[1], linhas[2])):
        print("CHEATER")
    else:
        resultado = pegarCoisasQueNaoComi(linhas[0], linhas[1], linhas[2])
        resultado = ''.join(sorted(resultado))
        print(resultado)
    
    