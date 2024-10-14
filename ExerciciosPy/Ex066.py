v = 0
soma = 0
cont = 0

while True:
    v = int(input('Digite um numero Inteiro (DIGITE 999 CASO QUEIRA PARAR): '))
    if v == 999:
        break
    soma = soma + v
    cont = cont+1
print(f'A quantidade de numeros digitados é: {cont}\nE a Soma entre todos os numeros digitados é: {soma}')