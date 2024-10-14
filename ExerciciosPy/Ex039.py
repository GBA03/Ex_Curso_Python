from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))

ver = date.today().year
idade = ver - ano
fal = 18 - idade
pas = idade - 18

if idade < 18:
    print(f'Você tem {idade} anos, você ainda vai se alistar. faltam {fal} anos ainda!!')
    q = ver + fal
    print(f'Seu alistamento vai ser no ano: {q}')
elif idade == 18:
    print(f'Você tem {idade} anos, já esta na hora de se alistar!!')
elif idade > 18:
    print(f'Você tem {idade} anos, já passou {pas} anos do tempo de se alistar!!')
    q = ver - pas
    print(f'Seu alistamento foi no ano {q}')
