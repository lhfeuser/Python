nm = int(input('Insira um número: '))
tot = 0

for c in range(1, nm + 1):
    if nm % c == 0:
        tot += 1
        print('\033[32m', end='')
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')

print('\033[0m O número {} foi divisível {} vezes'.format(nm, tot))
if tot == 2:
    print('\nO número {} é PRIMO'.format(nm))
else: 
    print('\nO número {} NÃo é um númnero PRIMO'.format(nm))