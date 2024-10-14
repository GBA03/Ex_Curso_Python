import random

print('Olá, hoje jogaremos pedra, papel e tesoura.')
print('''Você começa! Escolha uma das opçoes abaixo:'
Digite 1 para Pedra. 
Digite 2 para Papel. 
Digite 3 para Tesoura.''')
esc = int(input('Qual sua escolha? '))

escm = random.randint(1,3)

if escm == 1 and esc == 1:
    print(f'A maquina e você escolheram Pedra. Ocorreu um EMPATE!!')
elif escm == 1 and esc == 2:
    print('A maquina escolheu Pedra e você Papel. Você ganhou!!')
elif escm == 1 and esc == 3:
    print('A maquina escolheu Pedra e você Tesoura. Você Perdeu!!')
elif escm == 2 and esc == 2:
    print('A maquina e você escolheram Papel. Ocorreu um EMPATE!!')
elif escm == 2 and esc == 1:
    print('A maquina escolheu Papel e você Pedra. Você Perdeu!!')
elif escm == 2 and esc == 3:
    print('A maquina escolheu Papel e você Tesoura. Você ganhou!!')
elif escm == 3 and esc == 3:
    print('A maquina e você escolheram Tesoura. Ocorreu um EMPATE!!')
elif escm == 3 and esc == 2:
    print('A maquina escolheu Tesoura e você Papel. Você perdeu!!')
elif escm == 3 and esc == 1:
    print('A maquina escolheu Tesoura e você Pedra. Você ganhou!!')