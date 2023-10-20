'''from math import factorial

valor = int(input('Entre com o valor que você que saber o fatorial \nValor: '))
f = factorial(valor)
print(f)'''

valor = int(input('Entre com o valor que você que saber o fatorial \nValor: '))
c = valor
f = 1 

while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = {}'.format(f), end='')
    f *= c
    c -= 1


