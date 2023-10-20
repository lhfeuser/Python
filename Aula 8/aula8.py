import math
# from math import sqrt,floor
num = int(input('Digite um número: '))
raiz = math.sqrt(num)
# raiz = sqrt(num)
print('a raiz de {:.2f} é {:.2f}'.format(num, math.ceil(raiz)))