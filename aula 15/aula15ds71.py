print('=' * 30)
print('{:^30}'.format(' Banco Feuser '))
print('=' * 30)

valor = int(input('Insira o valor que você deseja sacar \nValor: R$'))
total = valor 
cedula = 50
total_cedulas = 0

while True:
    if total >= cedula:
        total -= cedula
        total_cedulas += 1
    else: 
        print(f'O total de {total_cedulas} cédulas de R${cedula} ')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        if total == 0:
            break


