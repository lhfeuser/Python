times = ('Botafogo', 'Bragantino', 'Flamengo', 'Grêmio', 'Palmeiras', 'Athletico - PR', 'Atlético - MG', 'Fortaleza', 'Fluminense', 'Cuiabá', 'São Paulo', 'Bahia', 'Internacional', 'Corinthias', 'Cruzeiro', 'Goiáis', 'Vasco da Gama', 'Santos', 'Coritiba', 'América - MG')

# cinco primeiros colocados
print(f'\nOs cinco primeiros colocados são {times[0:5]} \n')

# os lanterninhas 

print(f'Os lanterninhas do Campeonato Brasileiro são {times[19:15:-1]} \n')

# ordem alfabética

print(f'A ordem alfabética dos time é a {sorted(times)} \n')

# posição do time Atlético - MG
posicao_time = times.index('Atlético - MG')
posiçao_real_time = posicao_time + 1
print(f'O time Atlético - MG está na {posiçao_real_time}ª posição da tabela \n')