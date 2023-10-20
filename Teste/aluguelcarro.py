dias = int(input('Por quantos dias você alugou o carro? '))
km = float(input('Quantos kilometros você rodou como o carro? '))
pago = dias * 60 + km * 0.15
print('Total a pagar: {:.2f}'.format(pago))