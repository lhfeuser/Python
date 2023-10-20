sal = float(input('Digite seu salário: '))

print('----------------------')

if sal <= 1250:
    aum = (sal * 0.15) + sal
    print('Seu salário agora é de R${:.2f}'.format(aum))
else:
    aum = sal + sal * 0.10
    print('Seu salário agora é de R${:.2f}'.format(aum))
    
print('----------------------')
