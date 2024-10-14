p = int(input('Digite o 1 termo dessa PA: '))
r = int(input('Digite a razão dessa PA: '))
d = p + (10-1)*r
for cont in range(p,d+r, r):
    print(f'{cont}', end='..')
print('Fim!!')
