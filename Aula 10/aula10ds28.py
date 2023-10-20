import random

nc = random.randint(0,5)
ne = int(input('Escolha um número entre 0 e 5: '))

print('------------------------')

print('O numero sorteado foi {}'.format(nc))

if ne == nc:
    print('Parabéns!! Você acertou!')
else:
    print('Você errou. Tente novamente!')

