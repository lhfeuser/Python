frase = '   Curso em Vídeo O    '

print(frase[3]) 
print(frase[3:13])
print(frase[:13])
print(frase[1:])
print(frase[1:15:2])

print('---------------------------------')

print(frase.count('o')) # Conta a letra definada
print(frase.upper().count('O')) # Coloca pra maiusculo a frase e conta a letra definada
print(len(frase)) # Conta quantos caracteres tem a frase 
print(len(frase.strip())) # Conta sem os espaços antes e depois da frase
print(frase.replace('Curso', 'Aula')) # Troca o que quiser pelo que foi definido
print('Curso' in frase) # Mostra se a palavra definida está na frase
print(frase.find('Curso')) # Mostra a Posição da palavra definida dentro da frase quando não e existe = -1
print(frase.split()) # Printa a frase separada por palavras
