print('{:=^30}'.format(' Casdastro de Pessoas '))
maiores = 0
qntd_homem = 0
mulher_maisde_vinte = 0 

while True:
    # entrada de dados 
    idade = int(input('Insira a idade \nIdade: '))
    print('-' * 20)
    sexo = ' '
    while sexo not in 'MF': 
        sexo = str(input('Insira o sexo [ M ] / [ F ] \nSexo: ')).strip().upper()
    print('-' * 20)
    mais = ' '
    while mais not in 'SN':
        mais = str(input('Você quer cadastrar mais alguém? [ S ] / [ N ] \nReposta: ')).strip().upper()
    print('-' * 20)
    # quantos são maiores de idade
    if idade >= 18:
        maiores += 1
    # quantidade de homens
    if sexo == 'M':
        qntd_homem += 1
    # mulheres que tem menos de vinte anos 
    if sexo == 'F' and idade < 20:
        mulher_maisde_vinte += 1
    # break
    if mais == 'N':
        break

print(f'Neste cadastremento você teve {qntd_homem} homens cadastrados, {maiores} pessoas de maior e {mulher_maisde_vinte} mulher com menos de vinte anos')



