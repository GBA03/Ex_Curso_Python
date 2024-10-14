from datetime import date
totma = 0
totme = 0
for cont in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {cont}°: '))
    i = date.today().year - ano
    if i >= 21:
        totma += 1
    else:
        totme += 1
print(f'Ao todo tivemos {totma} maiores de idade e {totme} menores de idade!')