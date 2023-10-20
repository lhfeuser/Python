vi = float(input('Qual o valor do imóvel que você deseja comprar? '))
sal = float(input('Qual é o seu salário? '))
anos = int(input('Em quantos anos você pretende paagr este imovel? '))

print('----------------------')

ps = sal * 0.30
apm = anos * 12
vp = vi / apm

if vp > ps:
    print('Empréstimo negado')
else:
    print('Empréstimo aprovado!!! Sua parcela será de {:.2f} por {} anos'.format(vp,anos))