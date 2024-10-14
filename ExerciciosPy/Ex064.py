import math
v = 0
cont = 0
soma = 0
v = int(input('Digite um numero inteiro (Digite 999 para para o programa]: '))
while v != 999:
    cont = cont + 1
    soma = soma + v
    v = int(input('Digite um numero inteiro (Digite 999 para para o programa]: '))

print(f'Você digitou {cont } numeros.')
print(f'A soma é {soma}')
print('Acabou.')
