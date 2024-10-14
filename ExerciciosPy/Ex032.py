from datetime import date
a = int(input('Digite um ano qualquer para saber se é bissexto.\nColoque 0 caso queria analisar o ano atual:'))
if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'Esse ano {a}, digitado é bissexto!!')
else:
    print(f'Esse ano: {a}, digitado não é bissexto!!')