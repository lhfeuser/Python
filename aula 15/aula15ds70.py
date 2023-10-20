mais_de_mil_reais = 0
produto_mais_barato = ''
menor_preço = 9999999999999999999999
total_compra = 0

while True:
    nome_produto = str(input('Qual é o nome do produto inserido \nNome: '))
    print('-' * 20)
    valor = float(input('Qual o valor do produto inserido? \nValor: '))
    print('-' * 20)
    cadastrar = ' '
    while cadastrar not in 'SN': 
        cadastrar = str(input('Você quer cadastrar mais produtos? [ S ] / [ N ] Resposta: ')).strip().upper()
    print('-' * 20)
    # total da compra
    total_compra += valor
    # custam mais de mil 
    if valor > 1000:
        produto_mais_barato += 1
    # produto mais barato 
    if valor < menor_preço:
        produto_mais_barato = nome_produto
        menor_preço = valor
    # break
    if cadastrar == 'N':
        break

print(f'O produto mais barato é o/a {produto_mais_barato}, o total da sua compra foi de {total_compra :.2f} e você {mais_de_mil_reais} produtos acima de mil reais')
