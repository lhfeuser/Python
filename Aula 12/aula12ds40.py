n1 = float(input('Insira a primeira nota: \n'))
n2 = float(input('Insira a segunda nota: \n'))
med = (n1 + n2) / 2

if med < 5.00:
    print('----REPROVADO----') 
elif med >= 5.00 and med < 6.00:
    print('----EM RECUPERAÇÃO----')
else:
    print('----APROVADO----')


