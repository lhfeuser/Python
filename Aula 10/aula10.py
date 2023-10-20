tempo = int(input('Seu carro tem quantos anos? '))
print('---------------------------')
if tempo <= 3:
    print('carro novo')
else:
    print('carro velho')

print('---------------------------')

nome = str(input('Qual seu nome? ')).strip().lower()
print('---------------------------')
if nome == 'lucas':
    print('Que nome bonito você tem!!!')
else:
    print('Seu nome é tão normal :(')
print('Bom dia, {}!'.format(nome))

print('---------------------------')

n1 = float(input('Digite a nota n1: '))
n2 = float(input('Digite a nota n2: '))
m = (n1 + n2) / 2
print('---------------------------')

print('Sua média foi de {:.2}'.format(m))

if m >= 7:
    print('APROVADO')
else:
    print('REPROVADO')

print('---------------------------')
