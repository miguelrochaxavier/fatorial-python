import math

print('Calculadora de fatorial')
print('1- Fatorial simples')
print('2- Fatorial dupla')
print('3- Fatorial tripla')
print('4- Soma de fatoriais')
esc = int(input('#'))

if esc == 1 :

    def fatorial(n) :
        if n == 0 or n == 1 :
            return 1
        else : 
            return n * fatorial (n-1)

    x = int(input('Digite seu numero aqui : '))
    print(f'O fatorial de {x}! é {fatorial(x)}')

elif esc == 2 :

    def fatorialDuplo(n) :
        if n == 0 or n == 1 :
            return 1
        else : 
            return n * fatorialDuplo (n-2)
    
    x = int(input('Digite seu numero aqui : '))
    print(f'O fatorial de {x}!! é {fatorialDuplo(x)}')


elif esc == 3 :

    def fatorialTripla(n) :
        if n == 0 or n == 1 :
            return 1 
        else : 
            return n * fatorialTripla (n-3)
        
    x = int(input('Digite seu numero aqui : '))
    print(f'O fatorial de {x}!!! é {fatorialTripla(x)}')

elif esc == 4 :
    
    def fatorial(n) :
        if n == 0 or n == 1 :
            return 1
        else : 
            return n * fatorial (n-1)
    
    def fatorialk(n) :
        if n == 0 or n == 1 :
            return 1
        else : 
            return n * fatorial (n-1)
        
    y = int(input('Digite seu numero aqui : '))
    x = int(input('Digite seu numero novamente aqui : ')) # ajustar
    print(f'O fatorial de {x}! é {fatorial(x)}')
    

else :
    print('Erro número não encontrado. Tente novamente!')
