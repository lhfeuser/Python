frase = str(input('Digite uma frase: ')).lower().strip()          

print('Na sua frase tem {} letras A '.format(frase.count('a')))
print('O primeiro A aparece na posição {}'.format(frase.find('a')+1)) # Vai achar o que foi pedido da left for right e mostrar a posição
print('A última letra a aparece na posição {}'.format(frase.rfind('a')+1)) # Vai achar o que foi pedido da right for left e mostrar a posição