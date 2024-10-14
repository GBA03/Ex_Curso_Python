import math

nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

m = (nota1+nota2)/2

if m < 5:
    print(f'Sua media foi de : {m:.1f}, você esta abaixo da media de 5.0 e esta REPROVADO!!')
elif m >= 5 and m <= 6.9:
    print(f'Sua media foi de: {m:.1f}, assim sua media esta entre 5.0 e 6.9, voce esta de RECUPERAÇÃO!!')
elif m >= 7:
    print(f'Sua media foi de : {m:.1f}, você esta acima de 7.0 e esta APROVADO!!')