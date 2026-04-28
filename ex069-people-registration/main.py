'''Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar.
No final, mostre: A) quantas pessoas tem mais de 18 anos. B) quantos homens foram cadastrados. C) quantas mulheres tem menos de 20 anos.'''

idade = 0
cont_idade = cont_homens = cont_mulheres = 0

print('-=' * 17)
print(f"{'CADASTRO DE PESSOAS':^34}")
print('-=' * 17)

while True:    
    sexo = input('Sexo [M/F]: ').upper().strip()
    while sexo not in ('M','F'):
        print("Digite 'M' para masculino ou 'F' para feminino.")
        sexo = input('Sexo [M/F]: ').upper().strip()

    while True:
        try:       
            idade = int(input('Idade: '))
            break
        except ValueError:
            print('Por favor digite um número valido.')

    if sexo == 'F' and idade < 20:
        cont_mulheres += 1

    cont_idade += 1 if idade >= 18 else 0
    cont_homens += 1 if sexo == 'M' else 0  
    
    continuar = input('Continuar cadastrando? [S/N]: ').upper().strip() 
    while continuar not in ('S','N'):
        print("Digite 'S' para sim ou 'N' para não.")
        continuar = input('Continuar cadastrando? [S/N]: ').upper().strip() 
        
    if continuar == 'N':
        print('-=' * 17)
        print(f"{'PROGRAMA ENCERRADO':^34}")
        print('-=' * 17)
        break        

print('Foram cadastrados:')
print(f'{cont_idade} pessoas com mais de 18 anos.')
print(f'{cont_homens} homens.')
print(f'{cont_mulheres} mulheres com menos de 20 anos.')
    