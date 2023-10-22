# listas - variáveis compostas
# listas utilzam []
# .append adiciona um element no final da lista
# .insert(0,'....') insere o elemento desejado na posição desejada 
# del lanche[3] ou lanche.pop(3) ou .remove('') todos apagam um elemento da lista 
  
num = [91, 2, 3, 4, 5]
num[3] = 5834 # muda o terceiro valor da lista
num.append(1234) # adicona um valor 
num.sort() # colocaem ordem .sort(reserve=True) = ordem inversa
num.insert(2,900) # add na posição 2 o valor 900
num.pop() # apaga o último elemnto 
num.pop(4) # apaga o quarto elemento                 


print(num)
print(f'Essa lista tem {len(num)} elementos')

print('=' * 40)
print(f'{"NOVO EXEMPLO":^40}')
print('=' * 40)

valores = []
valores.append(5)
valores.append(6)
valores.append(7)

for v in valores:
    print(f'{v}')

for c, v in enumerate(valores):
    print(f'Na posição {c} tem os valores {v}')

