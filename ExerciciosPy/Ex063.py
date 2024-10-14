import math
n = int(input('Digite um numero qualquer: '))
t1 = 0
t2 = 1

print(f'{t1} > {t2}', end=' ')
cont = 3
while cont <= n:
    t3 = t1 + t2
    #Explicação: t1 = t2 e t2 = t3
    t1,t2 = t2, t1+t2
    print(f' > {t3}', end=' ')
    cont = cont + 1
print('Fim.')

