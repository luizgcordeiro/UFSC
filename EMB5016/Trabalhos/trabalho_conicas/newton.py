def exp(x):
    soma_old=0
    soma_new=1
    termo=1
    indice=0

    while soma_old!=soma_new:
        indice+=1
        termo*=(x/indice)

        soma_old=soma_new
        soma_new+=termo
    #end while

    return soma_new
#end def

def pot(x,n):
    if n==0:
        return 1
    else:
        return x*pot(x,n-1)
    #endif-else
#end def

def sin(x):
    soma_old=0
    soma_new=x
    termo=x
    indice=1

    while soma_old!=soma_new:
        indice+=1
        termo*=-(x/(2*indice-2))*(x/(2*indice-1))

        soma_old=soma_new
        soma_new+=termo
    #end while

    return soma_new
#end def

def cos(x):
    soma_old=0
    soma_new=1
    termo=1
    indice=0

    while soma_old!=soma_new:
        indice+=1
        termo*=-(x/(2*indice-1))*(x/(2*indice))

        soma_old=soma_new
        soma_new+=termo
    #end while

    return soma_new
#end def

def bissection(f,a,b,verbose=False):
    x_beg=float(a)
    x_end=float(b)
    iter=0

    if f(x_end)==0:
        return x_end
    #end

    if f(x_beg)==0:
        return x_beg
    #x_end

    while (f(x_beg)*f(x_end)<0):
        x_new=(x_beg+x_end)/2
        if f(x_new)*f(x_end)<0:
            x_beg=x_new
        else:
            x_end=x_new
        #end

        iter+=1
    #end while
#end

def falsa_posicao(f,a,b,verbose=False):
    x_beg=float(a)
    x_end=float(b)
    iter=0

    if f(x_end)==0:
        return x_end
    #end

    if f(x_beg)==0:
        return x_beg
    #x_end

    while (f(x_beg)*f(x_end)<0):
        x_new=x_beg-((f(x_beg)*(x_end-x_beg))/(f(x_end)-f(x_beg)))
        if f(x_new)*f(x_end)<0:
            x_beg=x_new
        else:
            x_end=x_new
        #end

        iter+=1
    #end while
#end

def newton(f,a,fprime=None,maximum_iterations=1.0e300,tol=1.0e-14,verbose=False):
  def verboseprint(s='',end='\n'):
    if verbose:
      print(s,end)
    #end if
  #end def

  if fprime==None:
    def der(x,y):
      return (f(x)-f(y))/(x-y)
    #end def
  else:
    def der(x,y):
      return fprime(x)
    #end def
  #end if

  x_old=a+1
  x_new=a
  number_of_iterations=0
  error=1.0e300

  while number_of_iterations<maximum_iterations and error>tol*x_new:
    val_f=f(x_new)
    deltax=-val_f/der(x_old,x_new)
    x_old=x_new
    x_new+=deltax
    error=abs(x_new-x_old)
    verboseprint('-----')
    verboseprint('Iteração '+ str(number_of_iterations)  + ':')
    verboseprint('x=')
    verboseprint(x_new)
    verboseprint('f(x)=')
    verboseprint(val_f)

    number_of_iterations+=1

  #end while

  verboseprint("Total: " + str(number_of_iterations) + " iterações.")
  return x_new
#end def

def f(x):
    return sin(x)*exp(x)-1
#end def

def der_f(x):
    return exp(x)*(sin(x)+cos(x))
#end  def

#comment
