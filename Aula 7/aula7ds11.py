lar = float(input('Digite a largura da sua parede: '))
alt = float(input('Digite a altura da sua parede: '))
area = lar * alt
tinta = area / 2

print('A área da sua parade é de {:.2f}m² e você precaisaria de {:.2f} litros de tinta para pinta-la'.format(area,tinta))