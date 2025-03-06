# Fatorial é igual a um numero multiplicado ate chegar ao 1. 
# Exemplo : 3! = 3.2.1!

import math

def fatorial(n) :
    if n == 0 or n == 1 :
        return 1
    else : 
        return n * fatorial (n-1)

print('Calculadora de fatorial')
print('1- Fatorial simples')
print('2- Fatorial dupla')
print('3- Fatorial tripla')
esc = int(input('#3'))

if esc == 1 :
    x = int(input('Digite seu numero aqui : '))
    print(f'O fatorial de {x}! é {fatorial(x)}')

