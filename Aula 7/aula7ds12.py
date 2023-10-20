pc = float(input('Digite o preço: '))
vd = pc * 0.05
nv = pc - vd

print('Você teve um valor de {:.2f} de desconto e o novo preço é de {:.2f}'.format(vd,nv))