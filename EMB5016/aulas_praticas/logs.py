import time

def pot(x,n):
    if n<0:
        return 1/pot(x,-n)
    
    p=1
    for i in range(n):
        p*=x
    
    return p
###
def log2(x):
    '''Logaritmo em base 2.'''
    if x<1:
        return -log2((1/x))
    
    #Acha l tal que 2^l<x<=2^(l+1)
    l=0
    while pot(2,l+1)<x:
        l+=1
    
    l_ant=l-1
    x_=x/pot(2,l)
    n=0
    while l_ant!=l:
        n+=1
        x_sq=x_*x_
        if x_sq<=2:
            x_=x_sq
        else:
            x_=x_sq/2
            l_ant=l
            l+=pot(2,-n)
    
    return l

def ln(x):
    '''Logaritmo em base natural'''
    l_ant=-1
    l=0
    n=0
    while abs(l_ant-l)>pot(2,-51)*l:
        n+=1
        l_ant=l
        l-=pot(1-x,n)/n
    
    return l

time_start=time.time()

for i in range(1000):
    ln(1.5)
#end for

time_end=time.time()

print(time_end-time_start)

print(ln(1.5))

time_start=time.time()

log2e=log2(2.71828182845904523)

for i in range(1000):
    log2(1.5)/log2e
#end for

time_end=time.time()

print(time_end-time_start)

print(log2(1.5)/log2e)

print("log_2(e)="+str(log2e))