tupla = (int(input('Entre com um número \nNúmero: ')), int(input('Entre com um número \nNúmero: ')), int(input('Entre com um número \nNúmero: ')), int(input('Entre com um número \nNúmero: ')))

print(tupla)
print(f'O número nove apareceu {tupla.count(9)} vezes')
if 3 in tupla:
    print(f'O número 3 apareceu na {tupla.index (3) + 1}ª posição')
else: 
    print('O valor três não apareceu nenhuma vez')

for n in tupla:
    if n % 2 == 0:
        print(n, end=' ')