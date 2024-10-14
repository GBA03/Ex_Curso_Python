s = 0
c = 0
for cont in range(1, 501, 2):
    if cont % 3 == 0:
        s += cont
        c = c + 1
print(f'O somatorio dos numeros impares {c} multiplos por 3 é {s}')