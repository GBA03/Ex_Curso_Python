#sexo = 'M' or 'F'

sexo = str(input('Digite seu sexo [M/F]:')).upper()[0].strip()
while sexo not in 'MmFf':
    sexo = str(input('Dado invalido. Digite seu sexo novamente [M/F]:')).strip().upper()[0]

print(f'O sexo {sexo} foi registrado com sucesso!!')
