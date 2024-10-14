print('Olá, hoje eu irei te ajudar a saber se um numero inteiro é maior que o outro.')

n1 = int(input('Digite um numero inteiro: '))
n2 = int(input('Digite outro numero inteiro: '))

if n1 > n2:
    print(f'O primeiro numero: {n1} é maior que o segundo numero: {n2}')
elif n2 > n1:
    print(f'O segundo numero: {n2} é maior que o primeiro numero: {n1}')
elif n1 == n2:
    print('Não existe valor maior, os dois numeros são iguais!!')

#Ou posso usar o else ali em cima.
#else:
    #print('Não existe valor maior, os dois numeros são iguais!!')