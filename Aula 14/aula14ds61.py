print('{:-^30}'.format(' GERADOR DE PA '))
primeiro = int(input('Digite o primeiro termo \nPrimeiro termo: '))
print('{:-^30}'.format(' GERADOR DE PA '))
razao = int(input('\nInsira a razão da sua PA \nRazão: '))
print('{:-^30}'.format(' GERADOR DE PA '))
termo = primeiro
cont = 1

while cont <= 10:
    print('{} -> '.format(termo), end='')
    termo += razao
    cont += 1
print('FIM')
