nome = str(input('Digite seu nome:')).strip()

separa = nome.split()

print(f'Seu primeiro nome é {separa[0]}:')
print(f'Seu ultimo nome é: {separa[len(separa)-1]}')