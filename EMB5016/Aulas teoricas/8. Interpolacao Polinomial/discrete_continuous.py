import numpy as np
import matplotlib.pyplot as plt

a=[-1+2*np.random.rand() for i in range(4)]
b=[-1+2*np.random.rand() for i in range(4)]

def f(x):
    return a[0]*np.sin(b[0]*x)+a[1]*np.cos(b[1]*x)+a[2]*np.sin(b[2]*x)+a[3]*np.cos(b[3]*x)

x=np.linspace(0,60,10000)
y=np.vectorize(f)(x)

f_plot = plt.plot(x,y,'b')
#plt.plot(x,[1000000]*10000,'b')
#plt.plot([62746],[1000000],'o')

plt.savefig('fig1.png')


discrete=np.random.choice(x,size=12,replace=False)

plt.plot(discrete,np.vectorize(f)(discrete),'or')
plt.savefig('fig2.png')

(f_plot.pop(0)).remove()
plt.savefig('fig3.png')

tabela=open("tabela.txt","w")# Cria tabela em latex com os valores discretos
tabela.write("\\begin{array}{cc}\nx&f(x)\\\\\\hline\n")
for x in discrete:
    tabela.write(f"{x:.4f}&{f(x):.4f}\\\\\n")
tabela.write("\\end{array}")
tabela.close()
#a=np.round(2**10)
#b=np.round(2**17)
#i=2

#plt.text(a,f(a),"x="+str(a))
#plt.text(b,f(b),"x="+str(b))
#i+=1
#plt.savefig('fig' + str(i) + ".png")
#while abs(b-a)>1:
    #x=(a+b)//2
    #if f(x)>10**6:
        #b=x
    #else:
        #a=x
    #
#    plt.plot([x],[f(x)],'og')
    #plt.text(x,f(x),"x="+str(x))
    #i+=1
    #plt.savefig('fig' + str(i) + ".png")
#end
       

#x=(a+b)//2

#plt.plot([x,x],[.25*10**6,10**6],'g--')
#plt.text(x,.25*10**6,"x="+str(x))
#i+=1
#plt.savefig('fig' + str(i) + ".png")