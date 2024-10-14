d = float(input('Digite a distancia em km da sua viagem:'))
p1 = d * 0.50
p2 = d * 0.45
print(f'Você esta começando uma viagem de {d}Km!')
if d <= 200:
    print(f'O preço da sua viagem é de : R${p1:.2f}')
else:
    print(f'O preço da sua viagem é: R${p2:.2f}')