import random

print('{:=^54}'.format('JOGO DO ACERTO'))

nc = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
spc = random.choice(nc)
jogador = int(input('Escolha um número \nNúmero: '))
tentativas = 0

print('{:=^54}'.format('JOGO DO ACERTO'))
while spc != jogador:
    spc = random.choice(nc)
    jogador = int(input('Escolha um número \nNúmero: '))
    tentativas+=1
    print('{:=^54}'.format('JOGO DO ACERTO'))
    
print('PARABÉNS, VOCÊ VENCEU... mas precisou de {} tentativas'.format(tentativas))

