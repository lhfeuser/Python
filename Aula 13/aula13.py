# estrutura de repetições for
'''
print('OI')
print('OI')
print('OI')
print('OI')
print('OI')
print('OI')
print('OI')
print('OI')
'''

'''for oi in range(0, 6):
    print('OI')
print('FIM')'''

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))

for c in range(i, f+1, p):
    print(c) # input no lugar do print vai de  um em um pelo enter
print('FIM')
