t1 = float(input('Insira o primeiro segmento: '))
t2 = float(input('Insira o primeiro segmento: '))
t3 = float(input('Insira o primeiro segmento: '))

print('------------------')

if t1 < t2 + t3 and t2 < t1 + t3 and t3< t1 + t2 and t1 == t2 and t2 == t3:
    print('Os segmentos acima podem ser um triângulo Equilátero')

elif t1 < t2 + t3 and t2 < t1 + t3 and t3< t1 + t2 and t1 == t2 != t3 or t2 == t3 != t1 or t1 == t3 != t2:
    print('Os segmentos podem formar um triângulo Isósceles')
elif t1 < t2 + t3 and t2 < t1 + t3 and t3 < t1 + t2 and t1 != t2 and t2 != t3:
    print('Os segmentos podem formar um triângulo Escaleno')

else:
    print('Os segmentos acima não podem ser um triângulo')