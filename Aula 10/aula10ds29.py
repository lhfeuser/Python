vel = int(input('Insira a velocidade que você passou: '))

print('------------------------------')

if vel > 80:
    print('VocÊ foi multado!')
    vm = (vel - 80) * 7
    print('O valor da multa é de R${:.2f}'.format(vm))
else:
    print('Você não foi multado.')

print('------------------------------')
