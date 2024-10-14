n1 = int(input('Digite um valor: '))
i = n1
f = 1
print(f'Calculando o {n1}!', end=' ')
while i > 0:
    print(f'{i}', end='')
    print(' X ' if i > 1 else ' = ', end='')
    f = f * i
    i = i - 1
print(f'{f}.')