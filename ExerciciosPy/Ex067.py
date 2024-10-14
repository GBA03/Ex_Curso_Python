import math
while True:
    n = int(input('Qual numero você quer ver a tabuada? '))
    print('=-=' * 30)
    if n < 0:
        break
    print(f'A tabuada do numero {n} é:')
    for c in range(1, 11):
        print(f'{n} X {c} = {n*c}')
    print('=-='*30)

print('Fim.')