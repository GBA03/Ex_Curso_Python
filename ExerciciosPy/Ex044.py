preco = float(input('Digite o preço normal do produto: R$'))
print('''Escolha uma opção:
Digite 1 para a vista no dinheiro/cheque com desconto de 10%.
Digite 2 para a vista no cartão com desconto de 5%.
Digite 3 para em ate 2x no cartão sem desconto.
Digite 4 para 3x ou mais no cartão com juros de 20% ''')
esc = int(input('Qual sua escolha de pagamento? '))

ad = preco - (preco*10/100)
ac = preco - (preco*5/100)
c2 = preco/2
ju = preco + (preco*20/100)

if esc == 1:
    print(f'Sua compra de R${preco:.2f} no dinheiro/cheque com o desconto de 10% é R${ad:.2f}')
elif esc == 2:
    print(f'Sua compra de R${preco:.2f} no cartão com o desconto de 5% é R${ac:.2f}')
elif esc == 3:
    print(f'Sua compra de R${preco:.2f} em até 2x no cartão é de R${c2:.2f}')
elif esc == 4:
    par = int(input('Quantas parcelas? '))
    parc = ju/par
    print(f'Sua compra sera parcelada em {par}x de R${parc:.2f} com juros.')
    print(f'Sua compra de R${preco:.2f} em {par}x no cartão com juros de 20% é R${ju:.2f}')
else:
    print('Opção invalida, tente novamente')