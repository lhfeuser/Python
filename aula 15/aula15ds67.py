tabuada = 0

while True:
    print('{:=^30}'.format(' GERADOR DE TABUADA '))
    tabuada = int(input('Digite o valor que você quer saber a tabuada \nValor: '))
    if tabuada < 0:
        break
    else:
        print('{:=^30}'.format(' GERADOR DE TABUADA '))
        print(f'0 x {tabuada} = ', tabuada * 0)
        print(f'1 x {tabuada} = ', tabuada * 1)
        print(f'2 x {tabuada} = ', tabuada * 2)
        print(f'3 x {tabuada} = ', tabuada * 3)
        print(f'4 x {tabuada} = ', tabuada * 4)
        print(f'5 x {tabuada} = ', tabuada * 5)
        print(f'6 x {tabuada} = ', tabuada * 6)
        print(f'7 x {tabuada} = ', tabuada * 7)
        print(f'8 x {tabuada} = ', tabuada * 8)
        print(f'9 x {tabuada} = ', tabuada * 9)
        print(f'10 x {tabuada} = ', tabuada * 10)

print('{:=^30}'.format(' FIM DO SISTEMA '))
