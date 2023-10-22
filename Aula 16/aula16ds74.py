from random import randint

tupla = (randint(1,100), randint(1,100), randint(1,100), randint(1,100), randint(1,100))
print('=-' * 20)
print(f'Sorteei os valores {tupla}')
print('=-' * 20)
print(f'O maior valor sorteado foi {max(tupla)} e menor valor foi de {min(tupla)}')
print('=-' * 20)