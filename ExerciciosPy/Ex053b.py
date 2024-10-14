f = str(input('Digite uma frase: ')).strip().lower()
pala = f.split()
jun = ''.join(pala)
inv = jun[::-1]

if inv == jun:
    print(f'A frase {jun}, invertida é {inv}. Então ele é palindromo!!')
else:
    print(f'A frase {jun}, invertida é {inv}. Então ele não é palindromo!!')