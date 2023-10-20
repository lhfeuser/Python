nome = str(input('Qual seu nome: ')).strip().lower()

print('-------------------')

if nome == 'lucas':
    print('Que nome bonito você tem!!')
elif nome == 'pedro' or nome == 'ana':
    print('Seu nome é bem popular no Brasil.')
elif nome in 'beatriz mariana roberta bruna':
    print('Belo nome feminino você tem')
else:
    print('Que nome normal você tem')
print('Tenha um bom dia, {}!'.format(nome.title()))