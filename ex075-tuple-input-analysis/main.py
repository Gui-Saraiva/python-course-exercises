'''Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9. B) Em que posição foi digitado o primeiro valor 3. C) Quais foram os números pares.'''

tupla = (int(input('Digite o número 1: ')), int(input('Digite o número 2: ')), int(input('Digite o número 3: ')), int(input('Digite o número 4: ')))

print(f'Quantas vezes aparece o número 9: {tupla.count(9)}')

if 3 in tupla:
    print(f'O primeiro valor 3 está na posição {tupla.index(3)}')
else:
    print('Nenhum valor 3 encontrado.')

print('Números pares: ',end ='')
for t in tupla: # esse for que percorre a variavel tupla em t lê os valores dela e nao os indices.
    if t % 2 == 0:
        print(f'{t}',end=' ')