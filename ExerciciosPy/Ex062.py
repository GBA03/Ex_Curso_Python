p = int(input('Digite o primerio termo dessa PA: '))
r = int(input('Digite a razão dessa PA: '))

termo = p
cont = 1
total = 0
n = 10
while n != 0:
    total = total + n
    while cont <= total:
        print(f'{termo} >> ', end=' ')
        termo = termo + r
        cont = cont + 1
    print('PAUSA')
    n = int(input('Quantos termos você quer mostrar a mais? '))


print(f'Fim. A progreção foi finalizada mostrando {total} termos!!')