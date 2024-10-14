n1 = float(input('Digite o 1° numero:'))
n2 = float(input('Digite o 2° numero:'))
n3 = float(input('Digite o 3° numero:'))
#lis= [n1,n2,n3]

menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print(f'O menor valor digitado foi: {menor}')
print(f'O maior valor digitado foi: {maior}')
#print(f'O maior valor é {max(lis)}\nE o menor valor é: {min(lis)}')