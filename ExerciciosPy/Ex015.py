km = float(input("Informe a quantidade de Km pecorrido pelo carro alugado:"))
d = float(input('Informe a quantidade de dias pelos quais ele foi alugado:'))

pd = d*60
pk = km*0.15
pt = pd+pk
print(f'O carro alugado pecorreu por {km}km em {d}dias')
print(f'Os valor a pagar pelo km pecorridos é de: {pk:.2f} Reais. E o valor a pagar pelos dias alugados é de: {pd:.2f} Reais')
print(f'Dessa forma, o valor total a pagar pelo aluguel desse veiculo é de: {pt:.2f} Reais')