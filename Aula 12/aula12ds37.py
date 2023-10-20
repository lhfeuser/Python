nm = int(input('Digite o número a ser criptografado: '))
print('--------------------')
print('''Escolha para qual base você deseja converter esse número
[1] Binário
[2] Octal
[3] Hexadicmal ''')
escolha = int(input('Digite qual você escolheu \nEscolha: '))

print('--------------------')
if escolha == 1:
    print('A conversão do número escolhido é {}'.format(bin(nm)[2:]))
elif escolha == 2:
    print('A conversão do número escolhido é {}'.format(oct(nm)[2:]))
elif escolha == 3:
    print('A conversão do número escolhido é {}'.format(hex(nm)[2:]))
else:
    print('OPÇÃO INVÁLIDA')