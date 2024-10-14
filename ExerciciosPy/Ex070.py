total = 0
totmil = 0
menor = 0
cont = 0

while True:
    p = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o valor do produto: '))
    cont = cont + 1
    total =  total+preço
    if preço > 1000:
        totmil = totmil + 1
    if cont == 1:
        menor = preço
    else:
        if preço < menor:
            menor = preço

    resp = ' '
    while resp not in 'S/N':
        resp = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if resp == 'N':
        break
print(f'O total da compra é de R${total:.2f}.')
print(f'Temos {totmil} produtos custando mais de R$1000,00')
print(f'O produto com menor preço custa R${menor:.2f}')
print('Fim.')