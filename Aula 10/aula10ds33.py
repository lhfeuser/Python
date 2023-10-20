n1 = int(input('Informe um número: '))
n2 = int(input('Informe um número: '))
n3 = int(input('Informe um número: '))

print('-------------------------')

# Verificando qual é menor
menor = n1
if n2 < n1 and n2 < n3: 
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

# Verificando quem é o maior 
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = 3

print('-------------------------')

print('O número maior é o {}'.format(maior))
print('O número menor é o {}'.format(menor))