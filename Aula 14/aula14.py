c = 1 
np = 0
ni = 0
'''while c < 10:
    print(c)
    c+=1'''

while c != 0:
    c = int(input('Digite um número: '))
    if c != 0:
        if c % 2 == 0:
            np+=1
        else:
            ni+=1

print('FIM')
print('Total de números pares é de {} e de ímpares é de {}'.format(np,ni))