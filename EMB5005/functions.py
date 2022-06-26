import numpy as np

def matrix_to_latex(A,begin="\\begin{bmatrix}",end="\\end{bmatrix}"):
    """Converts a numpy matrix to LaTeX code.
    
    Returns LaTeX code for matrix A

    Parameters
    ----------
    A : array-like of dimension 2.
    begin : string, optional
        LaTeX code to be put before the matrix code.
    end : string, optional
        LaTeX code to be put after the matrix code.

    Returns
    -------
    matrix_to_latex : str
        LaTeX code to write down A.
    """

    string=begin #Start the string

    [m,n]=np.shape(A) #Matrix size

    for i in range(m-1):
        for j in range(n-1):
            string+=str(A[i][j]) + "&"
        #end for
        string+=str(A[i][n-1])+"\\\\"
    #end for

    i=m-1

    for j in range(n-1):
        string+=str(A[i][j]) + "&"
    #end for

    string+=str(A[m-1,n-1])+end

    return string
#end def

#############################################
#############################################
#############################################
#############################################
#############################################
#############################################

def unimodular(m,li=10):
    """Returns random unimodular matrix.
    
    Parameters
    ----------
    m : positive integer
        Matrix order.
    li : positive number-like, optional
        Soft control on order of entries of output.

    Returns
    -------
    unimodular : 2-dimensional numpy array with int entries
        Random unimodular matrix of order m.
    """

    #Create random lower and upper triangular matrices L and U
    #with diagonal entries +-1.
    L=np.random.randint(low=-li,high=li,size=(m,m))
    U=np.random.randint(low=-li,high=li,size=(m,m))

    for i in range(m):
        L[i,i]=np.random.choice([1,-1])
        U[i,i]=np.random.choice([1,-1])
        for j in range(i+1,m):
            L[i,j]=0
            U[j,i]=0
        #end for
    #end for

    #Swap first row of L with another one
    p=np.random.choice(list(range(m)))
    x=L[0,:].copy()
    L[0,:]=L[p,:]
    L[p,:]=x

    #Swap first column of U with another one
    p=np.random.choice(list(range(m)))
    x=U[:,0].copy()
    U[:,0]=U[:,p]
    U[:,p]=x

    return np.matmul(L,U)
#end def

#############################################
#############################################
#############################################
#############################################
#############################################
#############################################

def triangularization(A,tol=1.0e-10,pivoting="partial",write_latex=False,verbose=False,):
    """Triangularizes a matrix.

    Parameters
    ----------
    A : array-like of dimension 2
        Matrix to be triangularized
    tol : float, optional
        Numerical precision
    pivoting : pivoting scheme.
        Currently implemented options are:
            - "partial" : Partial pivoting for float data; pivots are chosen in the
                respective column with maximum absolute value.
            - "integer" : Pivoting for integer data. Uses a procedure similar to Euclid's
                algorithm for finding GCDs of entries in a column.
        "total" or "complete" still to be implemented.
    write_latex : boolean, optional
        Determines if the return contains a string which with LaTeX code that explains
        how the triangularization was done. To be used as a teaching resource.
    verbose : boolean, optional
        To print steps explanations.
    

    Returns
    ----------
    triangularization : list
        Has the form [T,P,S,X], where
            T : array-like of dimension 2
                Triangularized form of A
            P : List of integers
                The entries are the indices of the columns of T which contain the pivots.
            S : None if parameter "write_latex" is False. Otherwise, string with relevant LaTeX code.
            X : Permutation of list [0,1,...,n-1],  where n is the number of columns of A
                (or T), corresponding to the column exchanges made during the triangularization
                process. (Note that it is simply [0,1,...,n-1] except only for total pivoting.)
    """

    T=(np.matrix(A).copy())
    P=[]
    S=("" if write_latex else None)
    
    #Record shape
    [n_linhas,n_colunas]=np.shape(T)
    
    X=list(range(n_colunas))

    #Vê quantos pivôs já foram achados
    numero_de_pivos=0

    #Column being worked
    j=0

    if verbose:
        print("Vamos triangularizar a matriz")
        print(T)
    #end if

    while (j<n_colunas and numero_de_pivos<n_linhas):
        if verbose:
            print("=====")
            print("Vamos pivotear a coluna " + str(j) + ".")
        #end if verbose

        #Encontra o pivô
        if pivoting=="partial":
            #Let pivot be the largest entry in the column
            pivot_position=np.argmax(abs(T[numero_de_pivos:,j]))+numero_de_pivos
            
            if abs(T[p,j])>tol:

                #verboseprint("O pivô da coluna " + str(j) " está na linha " + str(p) + ".")

                #Encontramos um pivô.
                #Troca linhas caso necessário
                if pivot_position!=numero_de_pivos:
                    if verbose:
                        print("Precisamos trocar a linha " + \
                        str(numero_de_pivos) + " com a linha " + str(pivot_position) + ".")
                    #end if verbose
                    l=T[pivot_position,:].copy()
                    T[pivot_position,:]=T[numero_de_pivos,:]#.copy() já é feito automaticamente
                    T[numero_de_pivos,:]=l
                    if verbose:
                        print(T)
                    #end ifverbose
                #end if

                #Pivoteia abaixo
                for k in range(numero_de_pivos+1,n_linhas):
                    if abs(True[k,j])>tol:
                        multiplicador=T[k,j]/T[numero_de_pivos,j]
                        T[k,j+1:]=T[k,j+1:]-multiplicador*T[numero_de_pivos,j+1:]
                        T[k,j]=0;
                    #end if
                #end for
                if verbose:
                    print("Aniquila as entradas abaixo:")
                    print(T)
                #end if verbose

                #Conta o pivô a mais
                numero_de_pivos+=1
                P.append(j)
            else:
                if verbose:
                    print("A coluna " + str(j) + " não tem pivô.")
                #end if verbose
            #end if
        #passa pra próxima coluna

        elif pivoting=="integer":
            # In the integer case, we perform in a manner similar to Euclid's Algorithm for finding GCD
            # It all depends on how many nonzero entries in the (relevant part of the) column there are:
            # The possible cases 0,  1 and >1 are treated differently, and in the latest two we even need
            # to know where the smallest nonzero (in absolute value is)
            positions_nonzeros=[]
            len_positions_nonzeros=0#Calculate length is O(n), so better avoid it
            T_nonzeros=[]


            for i in range(numero_de_pivos,n_linhas):
                if T[i,j] != 0:
                    positions_nonzeros+=[i]
                    len_positions_nonzeros+=1
                    T_nonzeros+=[T[i,j]]
                #end if
                print("Encontramos uma entrada não nula")
            #end for

            while len_positions_nonzeros>=2:
                #Find the smallest one
                pivot_position=positions_nonzeros[np.argmin(np.abs(T_nonzeros))]

                for i in positions_nonzeros:
                    if i!=pivot_position:
                        multiplicador=(T[i,j] // T[pivot_position,j])
                        

                        T[i]=np.subtract(T[i],np.multiply(multiplicador,T[pivot_position]))

                        if verbose:
                            print("Subtract " + str(multiplicador) + " times row " + str(pivot_position) + " from row " + str(i) + ".")
                            print(T)
                    #endif
                #end for

                positions_nonzeros=[]
                len_positions_nonzeros=0
                T_nonzeros=[]
                for i in range(numero_de_pivos,n_linhas):
                    if T[i,j]!=0:
                        positions_nonzeros+=[i]
                        len_positions_nonzeros+=1
                        T_nonzeros+=[T[i,j]]
                    #end if
                #end for
            #end while

            if len_positions_nonzeros==1:
                pivot_position=positions_nonzeros[np.argmin(np.abs(T_nonzeros))]
                if (pivot_position!=numero_de_pivos):
                    l=T[pivot_position,:].copy()
                    T[pivot_position,:]=T[numero_de_pivos,:]#.copy() já é feito automaticamente
                    T[numero_de_pivos,:]=l
                    if verbose:
                        print("Precisamos trocar a linha " + \
                        str(numero_de_pivos) + " com a linha " + str(pivot_position) + ".")
                        print(T)
                    #end if verbose
                
                numero_de_pivos+=1
                P.append(j)
            #end if

        #end if-else

        j+=1
    #end while

    return [T,P,S,X]
#end def