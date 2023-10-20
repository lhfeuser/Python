dis = float(input('Qual a  distância da sua viagem em km: '))

print('-----------------------')

if dis <= 200:
    valor = dis * 0.50
    print('O valor da sua viagem é de R${:.2f}'.format(valor))
else:
    valor = dis * 0.45
    print('O valor da sua passagem é de R${:.2f}'.format(valor))
print('------------------------')
print('Boa Viagem!')