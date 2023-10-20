qntd = 0
valor = 0
resposta = str(input('Você que inserir um número? [ S ] / [ N ] \nResposta: ')).upper()
media = 0
maior = 0
menor = 99999999999999999999999999999999999999999999999999999999999999999999
print('{:=^20}'.format('-='))

while resposta == 'S':
    num = int(input('Entre com um valor \nValor: '))
    print('{:=^20}'.format(''))

    # Maior menor
    if num > maior:
        maior = num

    if num < menor:
        menor = num

    # Média dos valores
    qntd += 1
    valor += num
    media = valor / qntd

    resposta = str(input('Você que inserir um número? [ S ] / [ N ] \nResposta: ')).upper()
    print('{:=^20}'.format(''))


print('A média entre os valores é de {:.2f}, o maior número é {:.2f} e o menor número é {:.2f}'.format(media, maior, menor))