extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

while True:
    escolha = int(input('Qual número você quer ver escrito por extenso? \nNúmero: '))
    if 0 <= escolha <= 20:
        break
    
print(f'O número que você escolheu escrito por extenso é {extenso[escolha]}')
