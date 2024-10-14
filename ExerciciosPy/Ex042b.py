r1 = float(input('Digite a 1° reta: '))
r2 = float(input('Digite a 2° reta: '))
r3 = float(input('Digite a 3° reta: '))

if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print(f'Os segmentos {r1}, {r2} e {r3} podem formar triangulo ', end=' ')
    if r1 == r2 == r3:
        print('Equilatero!')
    if r1 == r2 or r1 == r3 or r2 == r3:
        print('Isoscele!')
    if r1 != r2 != r3 != r1:
        print('Escaleno!')
else:
    print(f'Os segmentos {r1}, {r2} e {r3}1 não podem formar triangulo!!')