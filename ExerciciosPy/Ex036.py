import math
print('Olá, irei te ajudar a calcular o valor da prestação mensal do emprestimo bancario')
vc = float(input('Informe o valor da casa: '))
sal = float(input('Informe o seu salario em reais por mes: '))
ano = float(input('Informe em quantos anos você vai pagar? '))

pm = vc / (ano*12)
div = (sal * 30/100)

print(f'O valor da cassa é de: R${vc:.2f}, a prestação mensal da casa é: R${pm:.2f}')

if pm <= div:
    print(f'O seu salario é de: R${sal:.2f}\nOs 30% do seu salario é: R${div:.2f}\nA prestação mensal não excede 30% do seu salario. entao seu emprestimo esta aprovado')
else:
    print(f'O seu salario é de: R${sal:.2f}\nOs 30% do seu salario é: R${div:.2f}\nA prestação mensal excede 30% do seu salario. entao o esprestimo esta negado.')