print('{:-^30}'.format(' GERADOR DE PA '))
primeiro = int(input('Digite o primeiro termo \nPrimeiro termo: '))
print('{:-^30}'.format(' GERADOR DE PA '))
razao = int(input('\nInsira a razão da sua PA \nRazão: '))
print('{:-^30}'.format(' GERADOR DE PA '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print('{} -> '.format(termo), end='')
        termo += razao
        cont += 1
    print('PAUSA')
    print('{:-^30}'.format(' GERADOR DE PA '))
    mais = int(input('Quantos números mais você quer? \nMais: '))
print('{:-^30}'.format(' GERADOR DE PA '))
print('Progressão finalizada com {} termos mostrados'.format(total))
