valores = []
cont = 1
maior = 0 

for v in range(0, 5):
    valores.append(int(input(f'Entre com o {cont}º valor da lista \nValor: ')))
    cont += 1
print(f'Sua lista é a {valores}\n')

print('=-' * 90)
print(f'O menor número que você digitou foi o {min(valores)} e ele se encontra na {valores.index(min(valores)) +1 }ª posição,', end=' ')
print(f'e o maior número que você digitou foi o {max(valores)} e ele se encontra na {valores.index(max(valores)) +1 }ª posição')