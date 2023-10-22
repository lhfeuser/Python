lista = ('Caneta', 2.00,
         'Lápis', 1.89,
         'Caderno', 20.90,
         'Regua', 0.50,
         'Mochila', 98.97,
         'Penal', 35.90,
         'Apostila', 498.90)
print('-' * 40)
print(f'{"LISTA DE PREÇO":^40}')
print('-' * 40)

for posiçao in range(0, len(lista)):
    if posiçao % 2 == 0:
        print(f'{lista[posiçao]:.<30}', end=' ')
    else:
        print(f'R${lista[posiçao]:.2f}')
print('-' * 40)