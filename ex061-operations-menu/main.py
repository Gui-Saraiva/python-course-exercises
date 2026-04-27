#Crie um programa que leia dois valores e mostre um menu para fazer um cálculo com os dois números na tela:
from time import sleep

print('Digite dois números e escolha o que fazer com eles.')

num1 = int(input('Primeiro número: '))
num2 = int(input('Segundo número: '))
escolha = 0
amarela = '\033[33m'
fim_cor = '\033[m'

while escolha != 5:
    print('-=' * 18)
    print('''    [ 1 ] - Somar
    [ 2 ] - Multiplicar
    [ 3 ] - Ver qual é o maior
    [ 4 ] - Digitar novos números
    [ 5 ] - Sair ''')
    print('-=' *18)
    escolha = int(input('>>>>> Digite sua opção: '))
    if escolha == 1:
        soma = num1 + num2
        print(f'{amarela}A soma de {num1} + {num2} = {num1 + num2}{fim_cor}')
    elif escolha == 2:
        multiplicacao = num1 * num2
        print(f'{amarela}A multiplicação de {num1} x {num2} = {num1 * num2}{fim_cor}')
    elif escolha == 3:
        if num1 > num2:
            maior = num1
            print(f'{amarela}Entre {num1} e {num2} o maior é o {maior}{fim_cor}')
        else:
            maior = num2
            print(f'{amarela}Entre {num1} e {num2} o maior é o {maior}{fim_cor}')
    elif escolha == 4:
        print('Digite os números novamente: ')
        num1 = int(input('Primeiro número: '))
        num2 = int(input('Segundo número: '))
    elif escolha == 5:
        print(f'{amarela}FINALIZANDO...')
        sleep(1.5)
        print(f'Fim. Volte sempre.{fim_cor}')
    else:
        print('\033[31mOpção Inválida! Tente novamente.\033[m')
