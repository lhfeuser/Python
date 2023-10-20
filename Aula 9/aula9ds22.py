nome = str(input('Digite seu nome completo: ')).strip()  

print('Seu nome é {}'.format(nome))
print(' ')
print('Seu nome em maiúsculo é: ', nome.upper())    
print(' ')
print('Seu nome em minusculo é: ', nome.lower())
print(' ')
print('Seu nome tem {} letras'.format(len(nome)-nome.count(' ')))
print(' ')
print('Seu primeiro nome tem {} letras.'.format(nome.find(' ')))

