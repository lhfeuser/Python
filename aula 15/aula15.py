n = s = 0 

while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    s += n
# print('A soma vale {}'.format(s))
print(f'Soma dos vale {s}')