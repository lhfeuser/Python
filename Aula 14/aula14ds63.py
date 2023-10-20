print('{:=^51}'.format(' SEUQENCIA DE FIBONACCI '))
valor = int(input('Quantos termos você quer mostrar? \nTermos: '))
print('{:=^51}'.format(' SEUQENCIA DE FIBONACCI '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1,t2), end='')

cont = 3 

while cont <= valor:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    cont += 1
print(' -> FIM')
