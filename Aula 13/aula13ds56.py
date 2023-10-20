h = 0
m = 0 
idade_mulher = 0
idade_homem = 0
mnv = 0
mmv = 0
nomevelho = ''

for c in range(4):
    nome = str(input('Insira seu nome \nNome: '))
    print('{:=^20}'.format(''))
    idade = int(input('Insira sua idade \nIdade: '))
    print('{:=^20}'.format(''))
    sexo = int(input('Insira o sexo. [ 1 ] para homem e [ 2 ] para mulher \nSexo: '))
    print('{:=^20}'.format(''))
    
    if idade < 20 and sexo == 2:
        mnv+=1
    if sexo == 1:
        h+=1
        idade_homem += idade
    elif sexo == 2:
        m+=1
        idade_mulher += idade
        
if idade_homem > 1:
    imh = idade_homem / h
    print('A idade média entre os homens é de {:.2f} anos'.format(imh))
elif idade_mulher > 1:
    imm = idade_mulher / m
    print('A idade média entre as mulheres é de {:.2f} anos'.format(imm))
print('{:=^20}'.format(''))

if mnv > 1:   
    print('No grupo tem {} mulheres com menos de 20 anos'.format(mnv))
else:
    print('Não há mulheres com menos de vinte anos no grupo')


