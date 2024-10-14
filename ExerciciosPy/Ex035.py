r1 = float(input('Digite a 1° reta:'))
r2 = float(input('Digite a 2° reta:'))
r3 = float(input('Digite a 3° reta:'))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Os segmentos acima podem formar triangulo!')
else:
    print('Os segmento acima não podem formar triangulo!')