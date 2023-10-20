num = int(input('Digite um número \nNúmero: '))
soma = 0
qntd = 0

while num != 999:
    soma +=num
    qntd += 1
    num = int(input('Digite um número \nNúmero: '))

print('Você digitou um total de {} números e a soma entre eles é de {}'.format(qntd,soma))