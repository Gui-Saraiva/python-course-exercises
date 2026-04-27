'''
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
'''
soma_idades = 0
nome_homem = ''
idade_homem = -1
mulheres = 0

for p in range(1,5):    
    nome = input('Digite seu nome: ')
    idade = int(input('Digite sua idade: '))
    genero = input("Qual seu sexo? (Digite 'M' ou 'H'): ").lower()
    soma_idades += idade

    if genero == 'h' and idade > idade_homem:
            idade_homem = idade
            nome_homem = nome
    elif genero == 'm' and idade < 20:
            mulheres += 1
    
media_idade = soma_idades / 4

if idade_homem == -1:
       print('Nenhum homem cadastrado.')
else:
       print(f'{nome_homem} é o homem mais velho com {idade_homem} anos.')

print(f'A média da idade do grupo é {media_idade} anos.')
print(f'{mulheres} mulher(es) com menos de 20 anos.')