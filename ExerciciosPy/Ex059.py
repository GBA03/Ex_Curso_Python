import math

n1 = int(input('Digite o 1° valor:'))
n2 = int(input('Digite o 2° valor:'))
esc = 0
print('=-='*10)
while esc != 5:
    print('''Escolha uma opção abaixo:
             [1]Somar.
             [2]Multiplicar.
             [3]Maior.
             [4]Novos números.
             [5]Sair do programa.''')
    esc = int(input('Escolha uma opção:'))
    if esc == 1:
        soma = n1 + n2
        print(f'A soma dos valores {n1} e {n2} é {soma}.')
        print('=-='*10)
    elif esc == 2:
        mult = n1 * n2
        print(f'A multiplicação dos valores {n1} e {n2} é {mult}.')
        print('=-='*10)
    elif esc == 3:
        if n1 > n2:
            print(f'O valor {n1} é maior que {n2}.')
        elif n1 == n2:
            print(f'Os valores {n1} e {n2} são iguais.')
        else:
            print(f'O valor {n2} é maior que {n1}.')
            print('=-='*10)
    elif esc == 4:
        print('Digite os novos valores: ')
        n1 = int(input('Digite o novo 2° numero:'))
        n2 = int(input('Digite o novo 2° numero:'))
        print('=-='*10)
    elif esc == 5:
        print(f'O programa esta se encerrando, obrigado!!')
print('Fim do programa.')