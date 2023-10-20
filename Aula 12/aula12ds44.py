print('{:=^40}'.format(' LOJAS FEUSER '))
preço = float(input('QuaL o valor total das compras \nTotal: R$'))

print('''FORMAS DE PAGAMENTO
[ 1 ] À Vista ou Cheque
[ 2 ] À Vista Cartão
[ 3 ] 2x Cartão
[ 4 ] 3x ou mais no cartão''')
op = int(input('Qual a opção: '))

if op == 1:
    vp = preço - (preço * 0.10)
    print('O valor a pagar é de R${:.2f}'.format(vp))
elif op == 2:
    vp = preço - (preço * 0.05)
    print('O valor a pagar é de R${:.2f}'.format(vp))
elif op == 3:
    print('O valor a pagar é de R${:.2f}'.format(preço))
elif op == 4:
    parcelamento = int(input('Em quantas vezes você gostaria de fazer? \nNúmero de parcelas: '))
    if parcelamento >= 3:
        vp = preço + preço * 0.30
        vdp = vp / parcelamento
        print('O valor a pagar é de R${:.2f} e o valor da parcela será de R${:.2f}'.format(vp,vdp))
    else:
        print('{:=^40}'.format(' LOJAS FEUSER '))
        print('{:=^50}'.format(' Insira uma opção válida de parcelamento '))
else:
    print('{:=^30}'.format(' Insira uma opção válida '))
























''''vc = float(input('Insira o valor total da compra \Valor: '))
fg = str(input('Insira a forma de pagamento: avista/Cheque, a vista cartao, 2x Cartão, 3x ou + Cartão \Forma de pagamento: ')).strip().lower()
print('----------------------')

if fg == 'avista' or fg == 'cheque':
    vf = vc - (vc * 0.10)
    print('O valor com desconto será de R${:.2f}'.format(vf))
elif fg == 'a vista cartao':
    vf = vc - (vc * 0.05)
    print('O valor com desconto será de R${:.2f}'.format(vf))'''
            