maior = 0
menor = 0

for p in range(1, 6):
    peso = float(input('peso pessoa {}: '.format(p)))
    if p == 1: 
        maior = peso
        menor = peso
    else: 
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print('O maior peso listado é {:.2f} e o menor é {:.2f}'.format(maior,menor))