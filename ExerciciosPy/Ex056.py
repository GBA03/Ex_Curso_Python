import math
soma = 0
media = 0
velho = 0
nomevelho = 0
totm = 0

for c in range(1,5):
    print(f'------- {c}° Pessoa---------')
    nome = str(input('Nome:')).strip()
    idade = int(input('idade: '))
    sexo = str(input('Sexo: [M/F] ')).strip().upper()
    soma += idade
    if c == 1 and sexo == 'M':
        velho = idade
        nomevelho = nome
    if sexo == 'M' and idade > velho:
        velho = idade
        nomevelho = nome
    if sexo == 'F' and idade < 20:
        totm +=1
media = soma / 4
print(f'A media de idade das pessoas do grupo é: {media} anos')
print(f'O homem mais velho tem {velho} anos e se chama {nomevelho}')
print(f'Ao todo são {totm} mulheres com menos de 20 anos.')