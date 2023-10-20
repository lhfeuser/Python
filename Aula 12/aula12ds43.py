alt = float(input('Qual é sua altura \nAltura: '))
ps = float(input('Qual é o seu peso: \nPeso: '))
print('----------------------')

imc = ps / (alt * alt)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc >= 18.5 and imc < 25:
    print('Você está no peso ideal')
elif imc >= 25 and imc < 30:
    print('Você está com sobrepeso')
elif imc >= 30 and imc < 40:
    print('Você está obeso')
else:
    print('Você está com obesidade morbida')

print('\nE seu IMC é de {:.2f}'.format(imc))