import random
from time import sleep
esc = random.randint(0,5)


print('-=-' * 23)
print('O computador vai pensar em um numero entre 0 e 5, tente adivinhar...')
print('-=-' * 23)
n1 = int(input('Qual numero você acha que ele escolheu?'))
print('Processando....')
sleep(2)

if n1 == esc:
    print(f'Você acertou o numero que o computador escolheu, o numero é: {esc}')
else:
    print(f'Você não acertou o numero que o computador pensou!! o numero era: {esc}')