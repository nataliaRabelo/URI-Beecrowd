import sys
def lowest():
    n = int(input())
    x = input().split()
    temp = (sys.maxsize, -1)
    for i in range(len(x)):
        val = int(x[i])
        if int(val) < temp[0]:
            temp = (val, i)
    print(f"Menor valor: {temp[0]}")
    print(f"Posicao: {temp[1]}")
    
lowest()