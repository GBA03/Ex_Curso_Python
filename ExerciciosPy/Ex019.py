import random
num1 = str(input('Digite o nome do aluno de n°1:'))
num2 = str(input('Digite o nome do aluno de n°2:'))
num3 = str(input('Digite o nome do aluno de n°3:'))
num4 = str(input('Digite o nome do aluno de n°4:'))
lista = [num1, num2, num3, num4]


sor = random.choice(lista)

print(f'O aluno sorteado foi : {sor}')


