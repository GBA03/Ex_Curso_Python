f = str(input('Digite uma frase: ')).strip().lower()
pala = f.split()
jun = ''.join(pala)
inv = ''

for l  in range(len(jun) - 1, -1, -1):
    inv += jun[l]
print(jun, inv)

if inv == jun:
    print(f'A frase {f}, invertida é {inv}. Então ele é palindromo!!')
else:
    print(f'A frase {f}, invertida é {inv}. Então ele não é palindromo!!')
