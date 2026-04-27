# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

primo = int(input('Número: '))
contador = 0

if primo < 2:
    print('Um número primo é um inteiro maior que 1.')
else:
    for divisao in range(1, primo + 1):
        if primo % divisao == 0:
            contador += 1
            print(f'\033[33m{divisao}\033[m', end=' ')
        else:
            print(divisao, end=' ')
    print()
    if contador == 2:
        print(f'Divide somente por 1 e por ele mesmo.')
        print('PRIMO!')
    else:
        print(f'Tem {contador} divisores destacados.')
        print('NÃO é primo')

''' segunda versao
num = int(input('Digite um número: '))
cont = 0

if num < 2:
    print('Um número primo é um inteiro maior que 1.')
else:
    for c in range(1, num +1):
        if num % c == 0:
            cont += 1
            print('\033[31m', end='')
        else:
            print('\033[37m', end='')
        print(c, end=' ') # aqui printo fora do if... ou seja, sempre que o loop acaba. Então pega todos os números colorindo conforme o if acima.

    if cont == 2:
        print('\033[m')
        print('Dividiu apenas por 1 e por ele mesmo.')
        print('PRIMO!')
    else:
        print('\033[m')
        print(f'Teve {cont} números divisíveis destacados em \033[31mvermelho.\033[m')
        print('NÃO É PRIMO!')
'''