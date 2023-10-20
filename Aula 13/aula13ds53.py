frase = str(input('Insira um frase para ver se ela é um palidromo. \nFrase: ')).strip().upper()

palavra = frase.split()
junto = ''.join(palavra)
inverso = ''

for letra in range(len(junto) - 1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print('TEMOS UM PALINDROMO')
else:
    print('A frase digitado não é um palíndromo')

