from datetime import date

ma = 0
mn = 0 

for c in range(7):
    ano = int(input('Insira o ano em que a pessoa nasceu. \nAno: '))
    id = date.today().year - ano 
    if id >= 18:
        ma += 1
    elif id < 18:
        mn += 1
print('O número de pessoas ainda na menoridade é de {} e já na maioridade é de {}'.format(mn, ma))
