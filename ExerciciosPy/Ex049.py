n = int(input('Digite um numero: '))
print(f'A Tabuada do numero {n} é:')

for cont in range(1, 11):
    print(f'{n} X {cont} = {n*cont}')