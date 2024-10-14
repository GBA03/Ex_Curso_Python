f = str(input('Digite uma frase:')).upper().strip()
la = f.count('A')
loc = f.find('A')+1
ult = f.rfind('A')+1
print(f'A frase digitada é {f}. Analisando essa frase...')
print(f'A letra "A" aparece : {la}')
print(f'A letra "A" aparece pela primera vez na posição: {loc}')
print(f'A letra "A" aparece pela ultima vez na posição: {ult}')