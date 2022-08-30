1;

function F=fibonacci(n)
  %Calcula o n-esimo termo da sequencia de fibonacci
  a=1;F=1;
  for i=2:n
    x=a;
    a=F;
    F+=x;
  endfor
endfunction
