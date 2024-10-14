#num = int(input('Digite um numero entre 0 e 9999:'))
#n = str(num)

#print(f'O numero que você digitou foi : {num}. Analisando esse numero, observamos que :')
#print(f'A unidade desse numero é: {n[3]}')
#print(f'A dezena desse numero é: {n[2]}')
#print(f'A centena desse numero é: {n[1]}')
#print(f'A milhar desse numero é: {n[0]}')

#Maneira matematica abaixo
num = int(input('Digite um numero entre 0 e 9999:'))
uni = num // 1 % 10
deze = num // 10 % 10
cen = num // 100 % 10
mi = num // 1000 % 10

print(f'O numero digitado foi: {num}, analisando esse numero temos:')
print(f'Unidade igual: {uni}\nDezena igual: {deze}\nCentena igual: {cen}\nMilhar igual: {mi}')

