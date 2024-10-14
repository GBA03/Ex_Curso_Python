import math

peso = float(input('Digite seu peso em Kg: '))
altura = float(input('Digite sua altura em metros: '))

imc = peso/(altura**2)

if imc <= 18.5:
    print(f'Seu IMC é de {imc:.1f}, você esta abaixo do peso!!')
elif imc <= 25:
    print(f'Seu IMC é de {imc:.1f}, você esta no peso ideal!!')
elif imc <= 30:
    print(f'Seu IMC é  de {imc:.1f}, você esta sobrepeso!!')
elif imc <= 40:
    print(f'Seu IMC é de {imc:.1f}, você esta obseo!!')
else:
    print(f'Seu IMC é de {imc:.1f}, você esta na obesidade morbida')
