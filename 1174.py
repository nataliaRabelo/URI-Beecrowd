def select():
    A= [0]*100
    for i in range(len(A)):
        A[i] = float(input())
        if A[i] <= 10:
            print('A[{}] = {}'.format(i,A[i]))
            
    return None
    
select()