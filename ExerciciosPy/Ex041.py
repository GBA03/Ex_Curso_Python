from datetime import date

print('Programa para descobrir a categoria na natação baseado na idade')
nasc = int(input('Digite o ano de seu nascimento: '))

atual = date.today().year
idade = atual - nasc

if idade <= 9:
    print(f'De acordo com sua idade: {idade}, sua categoria é MIRIM!!')
elif idade <= 14:
    print(f'De acordo com sua idade: {idade}, sua categoria é INFANTIL!!')
elif idade <= 19:
    print(f'De acordo com sua idade: {idade}, sua categoria é JUNIOR!!')
elif idade <= 20:
    print(f'De acordo com sua idade: {idade}, sua categoria é SENIOR!!')
else:
    print(f'De acordo com sua idade: {idade}, sua categoria é MASTER!!')