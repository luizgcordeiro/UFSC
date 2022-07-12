import random
import numpy as np
import time

def criar_primos(n):
    '''Cria uma lista com n primos'''

    primos=list(range(n))
    primos[:4]=[2,3,5,7]
    len_primos=4

    ind_maior=0
    numero_a_checar=9
    while len_primos<n:
        #encontra o maior primo<=sqrt(numero_a_checar)
        while primos[ind_maior+1]**2<=numero_a_checar:
            ind_maior+=1
        #end while

        #verifica se numero_a_checar e primo
        achou_divisor=False
        for i in range(1,ind_maior+1):
            if numero_a_checar%primos[i]==0:
                achou_divisor=True
                break
            #end if
        #end if

        if not(achou_divisor):
            primos[len_primos]=numero_a_checar
            len_primos+=1
        #end if

        numero_a_checar+=2
    #end while

    return primos
#end def

def miller_rabin(n,t=1):
    '''Determina se o numero e provavelmente primo utilizando Rabin-Miller.
    
    n : numero a ser testado
    
    t: numero de testes
    
    A chance de dar errado e <4^(-t)'''
    #Wiki https://en.wikipedia.org/wiki/Miller%E2%80%93Rabin_primality_test#cite_note-damg%C3%A5rd-landrock-pomerance-9
    
    #Primeiro, escrevemos n=2^s*d+1, com d impar
    s=0
    d=n-1
    while d%2==0:
        d//=2    
        s+=1
    #end while

    bases=list(range(t))
    for i in range(t):
        bases[i]=random.randrange(2,n-1)
    #end for

    for a in bases:
        #x=a^d mod n
        x=pow(a,d,n)
        #Se x for 1 ou -1 modulo n, vai embora. Caso contrario, temos que fazer
        #testes para ver se da problema
        if x!=1 & x!=n-1:
            r=1
            while r<s:
                x=x*x%n
                if (x==n-1):
                    break
                #end if
                r+=1
            #end while

            if (r==s):
                return False
            #end if-else
        #end while
    #end for

    return True
#end def

def e_primo(n):
    '''Determina se n e primo'''
    primeiros_primos=criar_primos(min(1000,n))

    i=0

    for p in primeiros_primos:
        if n==p:
            return True
        if n%p==0:
            return False
        #end if
        i+=1
    #end for

    #Neste ponto, nao e divisivel por um dos primeiros primos

    return miller_rabin(n)
#end def

def primo_grande(k):
    '''Cria um primo grande com k bits.'''

    for i in range(1000):#Tenta 1000 vezes e sai caso contrario
        n=random.randrange(2**(k-1),2**k)

        if e_primo(n):
            return n
        #end if
    #end for

    return None
#end def

def bezout(x,y):

    a=[1,0]
    b=[0,1]
    r=[x,y]

    #r=ax+by
    while (r[1]%r[0])!=0:
        q=r[1]//r[0]
        r_novo=r[1]%r[0]
        #print(str(r[1]) + "=" + str(q) + "*" + str(r[0]) + "+" +str(r_novo))
        a_novo=a[1]-q*a[0]
        b_novo=b[1]-q*b[0]
        a[1]=a[0]
        a[0]=a_novo
        b[1]=b[0]
        b[0]=b_novo
        r[1]=r[0]
        r[0]=r_novo
    #end
    return [r[0],a[0],b[0]]#r=ax+by
#end

def numero_para_texto(mensagem):
    '''Traduz uma mensagem conforme o TGR.
    
    Parametros
    ----------
    mensagem : int ou string
        Mensagem numerica.

    Saida
    -----
    traduz_mensagem: string
        Mensagem legivel, feita pela conversao
        A : 11
        B : 12
        ...
        Z : 36
        Caracteres acentuados em sequencia.'''

    tabela=list(range(100))
    for i in range(11,37):
        tabela[i]=chr(i+54)#ASCII for the win
    #end for
    tabela[37:49]=['Â','Ã','Á','Ê','É','Î','Í','Ô','Õ','Ó',',','.']
    tabela[99]=' '

    m=str(mensagem)#converter para string de fato
    mensagem_levigel=""
    l=len(m)

    mensagem_legivel=""
    for i in range(0,l-1,2):
        mensagem_legivel+=tabela[int(m[i]+m[i+1])]
    #end for
    
    return mensagem_legivel
#end def

def texto_para_numero(mensagem):
    '''Traduz uma mensagem conforme o TGR.
    
    Parametros
    ----------
    mensagem : int ou string
        Mensagem legivel.

    Saida
    -----
    traduz_mensagem: string
        Mensagem numerica, feita pela conversao
        A : 11
        B : 12
        ...
        Z : 36
        Caracteres acentuados em sequencia.'''

    tabela={
        'A':11,
        'B':12,
        'C':13,
        'D':14,
        'E':15,
        'F':16,
        'G':17,
        'H':18,
        'I':19,
        'J':20,
        'K':21,
        'L':22,
        'M':23,
        'N':24,
        'O':25,
        'P':26,
        'Q':27,
        'R':28,
        'S':29,
        'T':30,
        'U':31,
        'V':32,
        'W':33,
        'X':34,
        'Y':35,
        'Z':36,
        'Â':37,
        'Ã':38,
        'Á':39,
        'Ê':40,
        'É':41,
        'Î':42,
        'Í':43,
        'Ô':44,
        'Õ':45,
        'Ó':46,
        ',':47,
        '.':48,
        ' ':99
   }

    l=len(mensagem)
    mensagem_numerica=""
    for i in range(l):
        mensagem_numerica+=str(tabela[mensagem[i]])
    #end for
    
    return mensagem_numerica
#end def

def codificar_rsa(p,q,e,mensagem):
    '''Codificacao RSA.
    
    Parametros
    ----------
    p,q : inteiros primos grandes e distintos
    e : inteiro em [1,(p-1)(q-1)), coprimo com (p-1)(q-1)
    mensagem : string
        Mensagem legivel.
    
    Saida
    -----
    codifica_rsa : [string,[m,e],d]
        Mensagem codificada ilegivel seguida da chave
        publica e da chave privada.
        '''

    m=p*q
    #(m,e) é a chave publica

    M=str(texto_para_numero(mensagem))

    blocos=criar_blocos(M,m)

    C=blocos
    for i in range(len(C)):
        C[i]=pow(int(blocos[i]),e,m)
    #end for

    return C
#end while

def criar_blocos(M,m):
    blocos=[]
    
    #Separa em blocos de tamanho 2
    i=0
    while i<len(M):
        if i+2<=len(M):
            blocos+=[M[i:i+2]]
        else:
            blocos+=[M[i]]
        #end if-else
        i+=2
    #end while

    #Agora, vamoss tentar juntar cada bloco com o proximo
    i=0
    while i<len(blocos)-1:
        #Vamos tentar juntar o bloco i com o proximo
        if int(blocos[i]+blocos[i+1])<m:
            #se puder, junta
            blocos[i]=blocos[i]+blocos[i+1]
            blocos.pop(i+1)
        else:
            #Caso contrario, vai pro proximo bloco
            i+=1
        #end if-else
    #end while

    return blocos
#end while

def descodificar_rsa(m,chave_privada,mensagem_codificada):
    '''
    Decifra uma mensagem criptografada em RSA.

    Parametros
    ----------
    mensagem_codificada : string [C[0],C[1],...] de blocos de mensagem
        mensagem a ser decifrada. Cada C[i] e uma string numerica
    chave_privada : inteiro
        

    Saida
    -----
    descodificar_rsa: string
        Mensagem decifrada e legível
    '''

    C=mensagem_codificada
    d=chave_privada

    M=""
    for i in range(len(C)):
        M+=str(pow(C[i],d,m))
    #end for

    return numero_para_texto(M)
#end def

def fatorar(m):
    '''Cria uma lista com os fatores primos de m.'''

    primos=[2,3]
    fatores=[]
    x=m
    #Primeiro, vamos tirar todos os fatores 2 e 3 de x
    while x%2==0:
        x//=2
        fatores+=[2]
    #end while
    while x%3==0:
        x//=3
        fatores+=[3]
    #end while

    #Agora, x e um numero impar, e nenhum da lista de primos
    #divide x

    #Se o ultimo termo da lista passar da raiz de x,
    #x sera primo

    talvez_proximo_primo=primos[-1]
    while primos[-1]**2<=x:
        #Neste ponto, nenhum termo da lista divide x
        #Vamos achar o proximo primo.
        achou_divisor=True

        while achou_divisor:
            talvez_proximo_primo+=2
            #Vamos verificar se talvez_proximo_primo e primo
            i=1
            achou_divisor=False
            while primos[i]**2<=talvez_proximo_primo:
                #Sempre vai ter um momento que passa... Sempre existe um primo entre n e 2n
                if talvez_proximo_primo%(primos[i])==0:
                    achou_divisor=True
                    break
                #end if
                i+=1
            #end while
        #end while

        #Vai sair do loop exatamente quando nao achar divisor

        primos+=[talvez_proximo_primo]

        #Vamos por os fatores desse novo primo em x
        while x%talvez_proximo_primo==0:
            x//=talvez_proximo_primo
            fatores+=[talvez_proximo_primo]
        #end while
    #end while

    #Vai sair do loop exatamente quando x for primo

    return fatores+[x]
#end def

def hacker_rsa(m,e,mensagem_codificada):
    ''''Hackeia uma mensagem codificada sabendo a chave
    publica (m,e) e a mensagem codificada'''

    #Primeiro, temos que fatorar o modulo m. Sabemos que vai ter exatamente 2 fatores
    [p,q]=fatorar(m)
    #Agora, precisamos da chave privada
    chave_privada=bezout(e,(p-1)*(q-1))[1]%((p-1)*(q-1))

    return descodificar_rsa(m,chave_privada,mensagem_codificada)
#end def


print("====================")
print("Vamos criar as chaves publica e privada")

tempo_inicial=time.time()
ppp=1000000
primos_pequenos=np.load("primos_pequenos.npy")#criar_primos(ppp)
#np.save("primos_pequenos.npy",primos_pequenos)
while False:
    p=random.choice(primos_pequenos[int(0.9*ppp):])
    q=random.choice(primos_pequenos[int(0.8*ppp):int(0.9*ppp)])
    #p=primo_grande(24)
    #q=primo_grande(24)
    m=p*q

    e=random.choice(primos_pequenos[:1000])
    #end while
    #chave publica (m,e)
    d=bezout(e,(p-1)*(q-1))[1]%((p-1)*(q-1))

    #d=chave privada
    tempo_chaves=time.time()-tempo_inicial

    mensagem="TODAS AS MENSAGENS PODEM SER CODIFICADAS"

    tempo_inicial=time.time()
    mensagem_codificada=codificar_rsa(p,q,e,mensagem)
    tempo_cod=time.time()-tempo_inicial

    print("Os primos escolhidos foram")
    print("    p="+str(p))
    print("e")
    print("    q="+str(q))
    print("O modulo e")
    print("    m=p*q="+str(m))
    print("A chave publica e")
    print("    e="+str(e))
    print("A chave privada e")
    print("    d="+str(d))
    print("Para criar as chaves, foram gastos")
    print(str(tempo_chaves) + " segundos")
    print("====================")
    print("\nA mensagem e")
    print("    \"" + mensagem + "\"")
    print("====================")
    print("A mensagem codificada e")
    print("    " + str(mensagem_codificada))
    print("Para codificar a mensagem, foram gastos")
    print(str(tempo_cod) + " segundos")
    print("====================")
    tempo_inicial=time.time()
    mensagem_descodificada=descodificar_rsa(m,d,mensagem_codificada)
    tempo_desc=time.time()-tempo_inicial
    print("A mensagem descodificada e")
    print("    " + mensagem_descodificada)
    print("Para descodificar a mensagem, foram gastos")
    print(str(tempo_desc) + " segundos")
    print("====================")
    tempo_inicial=time.time()
    #mensagem_hackeada=hacker_rsa(m,e,mensagem_codificada)
    tempo_hack=time.time()-tempo_inicial
    print("A mensagem hackeada e")
    print("    " + mensagem_hackeada)
    print("Para hackear a mensagem, foram gastos")
    print(str(tempo_hack) + " segundos")
#end while

print("====================")
#Primos com n digitos: [x for x in primos_pequenos if 10**n<=x <10**(n+1)]

p=np.zeros(100)
q=np.zeros(100)

tempo=np.zeros(20)
b=np.array(0)

for tamanho in range(6,11):
    if tamanho==6:
        A=np.array([[6,1]])
    else:
        A=np.concatenate([A,[[tamanho,1]]])
    #end
    print("Testando tamanho "+str(tamanho))

    if tamanho<12:
        num_testes=50
    elif tamanho==12:
        num_testes=10
    elif tamanho==13:
        num_testes=5
    elif tamanho==14:
        num_testes=2
    else:
        num_testes=1
    #end if-else
    

    n=tamanho//2
    m=tamanho-n
    primos_n=[x for x in primos_pequenos if 10**n<=x <10**(n+1)]
    primos_m=[x for x in primos_pequenos if 10**m<=x <10**(m+1)]
    for i in range(num_testes):
        p[i]=np.random.choice(primos_n)
        q[i]=p[i]
        while q[i]==p[i]:
            q[i]=np.random.choice(primos_m)
        #end while
    #end for

    time_inicial=time.time()

    for i in range(num_testes):
        fatorar(p[i]*q[i])
    #end for
    tempo[tamanho]=time.time()-time_inicial
    tempo[tamanho]/=num_testes
    print("tamanho " + str(tamanho) + ":"+ str(tempo[tamanho]) + " segundos")
    if tamanho==6:
        b=np.array([np.log2(tempo[tamanho])])
    else:
        b=np.concatenate([b,[np.log2(tempo[tamanho])]])
    #end
#984770904450021093547

#tamanho 4:0.0 segundos
#tamanho 5:0.0 segundos
#tamanho 6:0.004686379432678222 segundos
#tamanho 7:0.004686379432678222 segundos
#tamanho 8:0.050209450721740725 segundos
#tamanho 9:0.06416759490966797 segundos
#tamanho 10:0.9779461860656739 segundos
#tamanho 11:1.2196856021881104 segundos
#tamanho 12:11.136761736869811 segundos
#tamanho 13:31.86756761074066 segundos
#tamanho 14:79.98657655715942 segundos

X=np.linalg.lstsq(A,b)