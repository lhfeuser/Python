qntd = 0
soma = 0
c = 0

while True:
    c += 1
    valor = int(input(f'Digite um valor {c}: '))
    if valor == 999:
        break
    qntd += 1
    soma += valor

print(f'Você digitou {qntd} números e a soma entre eles é de {soma}')
