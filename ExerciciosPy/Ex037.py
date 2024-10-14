import math

n1 = int(input('Digite um numero Inteiro por favor: '))
print('Escolha uma opção de conversão abaixo:\nDigite 1 para Binario.\nDigite 2 para octal.\nDigite 3 para Hexadecimal.')
esc = int(input('Qual é sua escolha? '))

if esc == 1:
    print(f'O binario do numero {n1} é: {bin(n1)[2:]}')
elif esc == 2:
    print(f'O octal do numero {n1} é: {oct(n1)[2:]}')
else:
    print(f'O hexadecimal do numero {n1} é: {hex(n1)[2:]}')
