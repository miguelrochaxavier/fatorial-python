# Fatorial é igual a um numero multiplicado ate chegar ao 1. 
# Exemplo : 3! = 3.2.1!

import math

print('Calculadora de fatorial')
print('1- Fatorial simples')
print('2- Fatorial dupla')
print('3- Fatorial tripla')
esc = int(input('#'))

if esc == 1 :

    def fatorial(n) :
        if n == 0 or n == 1 :
            return 1
        else : 
            return n * fatorial (n-1)

    x = int(input('Digite seu numero aqui : '))
    print(f'O fatorial de {x}! é {fatorial(x)}')


# Colocar calculadora de fração com uma icognita divindo por partes, k = parte de cima da fração & l = parte de baixo da fração
