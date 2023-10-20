sexo = str(input('Insira o sexo [ M ] / [ F ] \nSexo: ')).upper()

while sexo != 'M' and sexo != 'F':
    print('Digite novamnete')
    sexo = str(input('Insira o sexo [ M / F ] Sexo: ')).upper()
    
print('Você digitou corretamente')