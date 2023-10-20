sal = float(input('Digite seu salário: '))
va = sal * 0.15
ns = sal + va

print('Seu salário agora é de R${:.2f} e você teve um aumento de R${:.2f}'.format(ns,va))