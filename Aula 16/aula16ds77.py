palavras = ('aula', 'casa', 'escola', 'curso', 'banana', 'roupa', 'mercado', 'programar')

for w in palavras:
    print(f'\nNa palavra {w.upper()} temos ', end='')
    for letra in w:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')