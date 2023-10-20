import random
from time import sleep
# Escolha Computador
ec = ['Pedra', 'Papel', 'Tesoura']
sort = random.choice(ec)

# Escolha Jogador
eu = str(input('Escolha entre Pedra, Papel ou Tesoura \nSua escolha: ')).title().strip()
print('-==-' * 11)

print('Pedra')
sleep(1)
print('Papel')
sleep(1)
print('Tesoura')

print('-==-' * 11)

if eu == sort:
    print('EMPATE')
elif eu == 'Tesoura' and sort == 'Papel' or eu == 'Pedra' and sort == 'Tesoura' or eu == 'Papel' and sort == 'Pedra':
    print('Você GANHOU')
else:
    print('Computador VENCEU')




print('-==-' * 11)
print(sort)