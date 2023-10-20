from datetime import date

ano = int(input('Você quer saber da sua situação militar? Insira o ano em que você nasceu. '))

print('-----------------------')

idade = date.today().year - ano

if idade < 18:
    print('Você ainda terá que se alistar no exercito.')
elif idade == 18:
    print('Você precisa se alistar no exercito este ano.')
else:
    print('Já passou da hora de você se alistar.')