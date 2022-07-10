import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sin(x*x)*2**x
#end def

x_low=-1
x_high=1
tamanho_intervalo=(x_high-x_low)

n=1000
x=np.linspace(x_low,x_high,n+1)

y=x.copy()
for i in range(n+1):
    y[i]=f(x[i])
#end for

fig, ax = plt.subplots()

exato=ax.fill(np.concatenate([[x[0]],x,[x[-1]]]), np.concatenate([[0],y,[0]]), 'b', alpha=0.4)
exato=ax.plot(x,y, 'b')
grid=ax.grid(True, zorder=5)

fig.suptitle("Integral de f(x)=sin(x²)*(2^x)",fontsize=16)
#plt.plot(x,y)

fig.savefig("1.integral_exata.png",format="png")

numero_particao=8
x_particao=np.random.random(numero_particao)#Tamanhos proporcionais dos intervalos

x_particao=(tamanho_intervalo/(2*numero_particao))+(tamanho_intervalo/2)*x_particao/sum(x_particao)#Tamanhos reais dos intervalos
x_particao[0]=x_low+x_particao[0]#Final do 0-esimo intervalo
for i in range(1,numero_particao):
    x_particao[i]=x_particao[i-1]+x_particao[i]
#end for

x_particao=np.concatenate([[x_low],x_particao])

ax.plot(x_particao,np.zeros(numero_particao+1),'og')
for i in range(numero_particao+1):
    ax.plot((x_particao[i],x_particao[i]),[0,f(x_particao[i])],':g')
#end for
fig.savefig("2.integral_particao.png",format="png")

t=np.random.random(numero_particao)
for i in range(numero_particao):
    t[i]=x_particao[i]+t[i]*(x_particao[i+1]-x_particao[i])
#end for

ax.plot(t,np.zeros(numero_particao),'xr')

for i in range(numero_particao):
    ax.plot([t[i],t[i]],[0,f(t[i])],"r:")
    ax.plot([t[i]],[f(t[i])],"ro")
#end for
fig.savefig("3.integral_pontuada.png",format="png")

for i in range(numero_particao):
    ax.plot([x_particao[i],x_particao[i+1]],[f(t[i]),f(t[i])],'r')
#end for

fig.savefig("4.integral_funcao_aproximada.png",format="png")

x_soma_de_riemann=[x_particao[0]]
y_soma_de_riemann=[0]
for i in range(numero_particao):
    x_soma_de_riemann+=[x_particao[i],x_particao[i+1]]
    y_soma_de_riemann+=[f(t[i]),f(t[i])]
#end for
x_soma_de_riemann+=[x[-1]]
y_soma_de_riemann+=[0]

ax.fill(x_soma_de_riemann,y_soma_de_riemann,'r',alpha=0.4)
fig.savefig("5.integral_aproximada.png",format="png")

ax.clear()

for numero_particao in range(1,101):

    exato=ax.fill(np.concatenate([[x[0]],x,[x[-1]]]), np.concatenate([[0],y,[0]]), 'b', alpha=0.4)
    exato=ax.plot(x,y, 'b')
    grid=ax.grid(True, zorder=5)

    fig.suptitle("Integral de f(x)=sin(x²)*(2^x)",fontsize=16)

    x_particao=np.random.random(numero_particao)#Tamanhos proporcionais dos intervalos

    x_particao=(tamanho_intervalo/(2*numero_particao))+(tamanho_intervalo/2)*x_particao/sum(x_particao)#Tamanhos reais dos intervalos
    x_particao[0]=x_low+x_particao[0]#Final do 0-esimo intervalo
    for i in range(1,numero_particao):
        x_particao[i]=x_particao[i-1]+x_particao[i]
    #end for

    x_particao=np.concatenate([[x_low],x_particao])

    ax.plot(x_particao,np.zeros(numero_particao+1),'og')
    for i in range(numero_particao+1):
        ax.plot((x_particao[i],x_particao[i]),[0,f(x_particao[i])],':g')
    #end for

    t=np.random.random(numero_particao)
    for i in range(numero_particao):
        t[i]=x_particao[i]+t[i]*(x_particao[i+1]-x_particao[i])
    #end for

    ax.plot(t,np.zeros(numero_particao),'xr')

    for i in range(numero_particao):
        ax.plot([t[i],t[i]],[0,f(t[i])],"r:")
        ax.plot([t[i]],[f(t[i])],"ro")
    #end for

    for i in range(numero_particao):
        ax.plot([x_particao[i],x_particao[i+1]],[f(t[i]),f(t[i])],'r')
    #end for

    x_soma_de_riemann=[x_particao[0]]
    y_soma_de_riemann=[0]
    for i in range(numero_particao):
        x_soma_de_riemann+=[x_particao[i],x_particao[i+1]]
        y_soma_de_riemann+=[f(t[i]),f(t[i])]
    #end for
    x_soma_de_riemann+=[x[-1]]
    y_soma_de_riemann+=[0]

    ax.fill(x_soma_de_riemann,y_soma_de_riemann,'r',alpha=0.4)
    fig.savefig("6/6." + str(numero_particao).zfill(3) + ".integral_aproximada.png",format="png")

    ax.clear()
#end for 

exato=ax.fill(np.concatenate([[x[0]],x,[x[-1]]]), np.concatenate([[0],y,[0]]), 'b', alpha=0.4)
exato=ax.plot(x,y, 'b')
grid=ax.grid(True, zorder=5)


fig.suptitle("Integral de f(x)=sin(x²)*(2^x)",fontsize=16)

numero_particao=8
x_particao=np.random.random(numero_particao)#Tamanhos proporcionais dos intervalos

x_particao=(tamanho_intervalo/(2*numero_particao))+(tamanho_intervalo/2)*x_particao/sum(x_particao)#Tamanhos reais dos intervalos
x_particao[0]=x_low+x_particao[0]#Final do 0-esimo intervalo
for i in range(1,numero_particao):
    x_particao[i]=x_particao[i-1]+x_particao[i]
#end for

x_particao=np.concatenate([[x_low],x_particao])
y_particao=np.zeros(numero_particao+1)
for i in range(numero_particao+1):
    y_particao[i]=f(x_particao[i])
#end for

for i in range(numero_particao+1):
    ax.plot((x_particao[i],x_particao[i]),[0,f(x_particao[i])],':r')
    ax.plot((x_particao[i],x_particao[i]),[0,f(x_particao[i])],'or')
#end for

x_soma_de_riemann=np.concatenate([[x_low],x_particao,[x_high]])
y_soma_de_riemann=np.concatenate([[0],y_particao,[0]])

ax.fill(x_soma_de_riemann,y_soma_de_riemann,'r',alpha=0.4)
ax.plot(x_particao,y_particao,'r')
fig.savefig("7.trapezio.png",format="png")

plt.show()

ax.clear()