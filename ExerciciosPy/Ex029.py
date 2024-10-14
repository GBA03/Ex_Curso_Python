v = float(input('Informe a velocidade do carro em Km/h:'))
mul = (v - 80) * 7.0

if v > 80:
    print(f'Sua velocidade de {v} esta acima de 80km/h, você sera multado em: R${mul:.2f}')
else:
    print(f'Sua velocidade de {v}, esta abaixo de 80km/h, você não sera multado!!')