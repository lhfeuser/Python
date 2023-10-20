print('{:=^40}'.format(' CALCULADORA '))
n1 = float(input('Digite o primeiro valor \nValor: '))
n2 = float(input('Digite o segundo valor \nValor: '))
opção = 0
calculo = 0

print('{:=^40}'.format(' CALCULADORA '))
print('{:-^21}'.format(' OPÇÕES '))

print(''' 
[ 1 ] Somar
[ 2 ] Multiplicar 
[ 3 ] Maior
[ 4 ] Novos Valores
[ 5 ] Sair do Programa
''')
print('{:=^40}'.format(' INSIRA A OPÇÃO  '))
opção = float(input('Opção: '))

while opção == 1 or opção == 2 or opção == 3 or opção == 4 and opção != 5:
    if opção == 1:
        calculo = n1 + n2
        print('A soma dos valores é {:.2f}'.format(calculo))
        print('{:=^40}'.format(' INSIRA A OPÇÃO  '))
        opção = float(input('Opção: '))

    elif opção == 2:
        calculo = n1 * n2
        print('A multiplicação dos valores é de {:.2f}'.format(calculo))
        print('{:=^40}'.format(' INSIRA A OPÇÃO  '))
        opção = float(input('Opção: '))

    elif opção == 3:
        if n1 > n2:
            print('O maior número é o número 1 com o valor de {:.2f}'.format(n1))
            print('{:=^40}'.format(' INSIRA A OPÇÃO  '))
            opção = float(input('Opção: '))

        else:
            print('O maior número é o número 2 com valor de {:.2f}'.format(n2))
            print('{:=^40}'.format(' INSIRA A OPÇÃO  '))
            opção = float(input('Opção: '))
    elif opção == 4:
        n1 = float(input('Digite o primeiro valor \nValor: '))
        n2 = float(input('Digite o segundo valor \nValor: '))
        print('{:=^40}'.format(' INSIRA A OPÇÃO  '))
        opção = float(input('Opção: '))

print('{:-^50}'.format(' VOCÊ SAIU DO PROGRAMA '))
