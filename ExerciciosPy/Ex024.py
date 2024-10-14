c = str(input('Digite o nome da cidade:')).strip()

ver = (c[:5].upper() == 'SANTO')

print(f'O nome da cidade que você digitou foi: {c}. Analisando esse nome informado...')
print(f'Essa cidade começa com Santo? {ver}')