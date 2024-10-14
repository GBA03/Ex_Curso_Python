from math import radians, sin,cos,tan
a = float(input('Digite um angulo qualquer:'))
sen = sin(radians(a))
cos = cos(radians(a))
tan = tan(radians(a))

print(f'O angulo fornecido é: {a}. Abaixo esta os valores do seno, coseno e tangente desse angulo:')
print(f'O seno de {a} é: {sen:.2f}\nO coseno de {a} é: {cos:.2f}\nA tangente de {a} é: {tan:.2f}')
