from datetime import date

ano = int(input('Qual ano você deseja analisar ou coloque zero para analisar o ano atual: '))

print('-----------------------')
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or 400 == 0:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))