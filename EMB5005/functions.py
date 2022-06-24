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
        matrix order
    li : positive number-like, optional
        Soft control on order of entries of output

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

