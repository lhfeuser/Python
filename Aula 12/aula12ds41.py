from datetime import date

ano = int(input('Insira o ano em que o atleta nasceu \n' 'Ano: '))
id = date.today().year - ano


if id < 9:
    print('\nO atleta é da categoria MIRIM')
elif id >= 9 and id < 14:
    print('\nO atleta é da categoria INFANTIL')
elif id >= 14 and id < 19:
    print('\nO atleta é da categoria JUNIOR')
elif id >= 19 and id < 20:
    print('\nO atleta é da categoria SÊNIOR')
else:
    print('\nO atleta é da categoria MASTER')