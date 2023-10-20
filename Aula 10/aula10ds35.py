t1 = float(input('Insira o primeiro segmento: '))
t2 = float(input('Insira o primeiro segmento: '))
t3 = float(input('Insira o primeiro segmento: '))

print('------------------')

if t1 < t2 + t3 and t2 < t1 + t3 and t3< t1 + t2:
    print('\033[31mOs segmentos acima podem ser um triângulo')
else:
    print('Os segmentos acima não podem ser um triângulo')