from random import randint
pc = randint(0,10)
print('Olá, irei pensar em um numero de 0 a 10, tente adivinhar!!')

acertou = False
palpites = 0

while not acertou:
    jogador = int(input('Qual seu palpite? '))
    palpites = palpites + 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print('Mais... Tente novamente: ')
        elif jogador > pc:
            print('Menos... Tente novamente: ')
print(f'Acertou com {palpites} tentativas. parabens!!')