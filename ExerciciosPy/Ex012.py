preco = float(input('Informe o preço em reais do produto que deseja verificar o desconto:'))

print(f'O preço do produto é : {preco:.2f} Reais, com o desconto de 5% ele fica: {preco- (preco*5/100):.2f} Reais')