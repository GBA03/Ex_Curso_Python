n1 = int(input('Digite um valor:'))
i = 1
for c in range(n1, 0, -1):
    i = i*c
    print(f'{n1} x {c}', end=' | ')
print(f'O fatorial de {n1} é {i}')