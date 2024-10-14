import math
co = float(input('Digite o comprimento do Cateto Oposto do triangulo:'))
ca = float(input('Digite o comprimento do cateto adjacente do triangulo:'))

hip = math.hypot(co, ca)

print(f'O cateto oposto do triangulo é {co}, o cateto adjacente do triangulo é {ca}')
print(f'O calculo da hipotenusa desse triangulo é: {hip:.2f}')
