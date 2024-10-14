c = 0
s = 0
for cont in range(1, 7):
    n1 = int(input('Digite um numero inteiro: '))
    if n1 % 2 == 0:
        s = s + n1
        c = c + 1
print(f'A soma dos {c} numeros pares é {s}')
