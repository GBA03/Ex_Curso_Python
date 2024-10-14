d = float(input('Quanto de dinherio você tem na carteira? R$'))
dol = d / 5.47
eur = d / 6.02
ien = d / 0.037
print(f'O valor de dinheiro informado na carteira é de: {d} Reais')
print(f'Com esse valor de {d:.2f} Reais, na cotação atual, você pode comprar:\n{dol:.2f} Dolares\n{eur:.2f} Euros\n{ien:.2f} Ienes')
