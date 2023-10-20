import random
ip = ''
valor = 0
qntdV = 0
soma = 0

print('{:-^40}'.format(' JOGO DO PAR OU ÍMPAR '))

while True:
    npc = random.randrange(1,10)
    valor = int(input('Digite um valor \nValor: '))
    ip = str(input('Escolha [ P ] / [ I ] \nEsolha: ')).strip().upper()
    print('{:-^40}'.format(' JOGO DO PAR OU ÍMPAR '))

    if ip == 'P':
        ippc = 'I'
    if ip == 'I':
        ippc = 'P'
    
    if ip == 'P':
        soma = valor + npc
        if soma % 2 == 0 and ip == 'P':
            qntdV += 1
            print('Parabéns, Você Venceu')
            print('{:-^40}'.format(' JOGO DO PAR OU ÍMPAR '))

    if ip == 'I':
        soma = valor + npc
        if soma % 2 != 0 and ip == 'I':
            qntdV += 1
            print('Parabéns, Você Venceu')
            print('{:-^40}'.format(' JOGO DO PAR OU ÍMPAR '))
    else:
        print('{:=^30}'.format(' GAME OVER '))
        print(f'Você perdeu mas ganhou {qntdV} vezes')
        break
    