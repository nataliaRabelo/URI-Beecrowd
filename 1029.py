chamadas = 0

def lerNum():
    num = int(input())
    while(num < 1 or num > 39):
        num = int(input())
    return num

def getCalls(n):
    cl = [0] * (n+1)
    cl[1] = 0
    for i in range(2,n+1):
        cl[i] = cl[i-1] + cl[i-2] + 2
    cl[1] = 1
    return cl[n]

def fib(numeroBase, memoria={}):

    def sub_fib(num):
        if(num <= 1):
            return num
        if(num not in memoria):
            memoria[num] = sub_fib(num - 1) + sub_fib(num - 2)
        return memoria[num]
    
    resultado = sub_fib(numeroBase)
    calls = getCalls(numeroBase)
    return resultado, calls

testCases = int(input())

while(testCases > 0):
    num = lerNum()
    resultado = fib(num)
    print('fib(' + str(num) + ') = ' + str(resultado[1]) + ' calls = ' + str(resultado[0]))
    testCases = testCases - 1

