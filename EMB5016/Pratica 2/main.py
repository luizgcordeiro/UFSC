def Fib(n):
    '''
    Retorna os elementos F[n-1] e F[n] da sequencia de Fibonacci em uma lista
    [F[n-1],F[n]], em que
        F[0]=F[1]=1, F[n+2]=F[n]+F[n+1]
    (exceto no caso em que n=0, que retorna somente [F[0]])
    '''
    if n==0:
        return [1]
    elif n==1:
        return [1,1]
    else:
        L=Fib(n-1)#=[F[n-2],F[n-1]]
        #F[n]=L[0]+L[1]
        return [L[1],L[0]+L[1]]
    #end if-else
#end def

n=995
print(f"Fib({n})={Fib(n)[1]}")



#Fib(6)=Fib(5)+Fib(4)
#    =Fib(4)+2*Fib(3)+Fib(2)
#    =Fib(3)+3*Fib(2)+3*Fib(1)+Fib(0)
#    =Fib(2)+7*Fib(1)+4*Fib(0)
#    =8*Fib(1)+5*Fib(0)
#Fib(7)=...a*Fib(1)+b*Fib(0),.... em que a+b=21 ~~2^7