import math 

ang = float(input('Insira o valor do ângulo: '))
rad = math.radians(ang)
print('O seno do angulo é {:.2f} o cesseno é {:.2f} e a tangente é {:.2f}'.format(math.sin(rad), math.cos(rad), math.tan(rad)))