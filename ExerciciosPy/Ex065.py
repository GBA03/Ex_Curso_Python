import math
esc = 'Ss'
soma = 0
quant = 0
n1 = 0
media = 0
maior = 0
menor = 0

while esc in 'Ss':
    n1 = int(input('Digite um numero: '))
    soma = soma + n1
    media = soma/2
    quant = quant + 1
    if quant == 1:
        maior = menor = n1
    else:
        if n1 > maior:
            maior = n1
        if n1 < menor:
            menor = n1
    esc = str(input('Quer continuar? [S/N]')).strip()[0].upper()

print(f'A media entre todos os valores lidos {quant} é: {media}')
print(f'O maior valor é: {maior} e o menor valor é: {menor}')
print('Fim.')
