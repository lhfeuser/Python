primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1) * razão

for c in range(primeiro, decimo + razão, razão):
    print('{} '.format(c), end=' -> ')
print('ACABOU')