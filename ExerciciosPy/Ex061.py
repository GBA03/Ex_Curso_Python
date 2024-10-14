p = int(input('Digite o 1 termo dessa PA: '))
r = int(input('Digite a razão dessa PA: '))
termo = p
cont = 1
while cont <= 10:
    print(f'{termo} >> ', end=' ')
    termo = termo+r
    cont = cont+1
print('Fim')