n1 = int(input('Digite um numero inteiro: '))
tot = 0
for c in range(1, n1 + 1):
    if n1 % c == 0:
        print('\033[33m', end='')
        tot = tot + 1
    else:
        print('\033[31m', end='')
    print(f'{c}', end=' ')
print(f'\n\033[m0 O numero {n1} foi divisivel {tot} vezes')
if tot == 2:
    print('E por isso ele é primo!!')
else:
    print('E por isso ele não é primo!!')