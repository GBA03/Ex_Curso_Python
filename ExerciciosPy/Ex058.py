import random
escmaquina = random.randint(0,10)
tot = 1

print('Olá, vou pensar em um numero de 0 a 10, tente adivinhar!!')
escjogador = int(input('Qual numero de 0 a 10 que a maquina vai escolher? '))

while escjogador != escmaquina:
    if escmaquina > escjogador:
        print('Você errou, uma dica: o numero é maior.')
    else:
        print('Você errou, uma dica: o numero é menor:')

    escjogador = int(input('Qual seu palpite? '))
    tot = tot + 1

print(f'Você acertou, o numero que a maquina escolheu era {escmaquina} e você escolheu {escjogador}')
print(f'Você teve {tot} tentativas para acertar')