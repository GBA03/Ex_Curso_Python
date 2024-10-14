sal = float(input('Digite o salario do funcionario em reais:'))

if sal<=1250:
    print(f'O salario digitado R${sal:.2f} é inferior a R$1250, com o aumento de 15%, ele passara a R${sal+(sal*15/100):.2f} ')
else:
    print(f'O salario digitado R${sal:.2f} é superior a R$1250 , com o aumento de 10%, ele pasarra a R${sal + (sal * 10 / 100):.2f}')