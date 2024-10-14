idade = 0
homem = 0
mulher = 0
totidade = 0
maior = 0

while True:
    idade = int(input('Digite sua idade: '))
    if idade >= 18:
        totidade = totidade + 1
    sexo = ' '
    while sexo not in 'MF':
       sexo = str(input('Digite seu sexo [M/F]:')).strip().upper()[0]
    if sexo == 'M':
        homem = homem+1
    else:
        mulher = mulher+1

    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break

print(f'Total de pessoas maiores que 18 anos é {totidade}.')
print(f'A quantidade de homem é {homem}.\nE a de mulher é {mulher}.')
print('Acabou.')