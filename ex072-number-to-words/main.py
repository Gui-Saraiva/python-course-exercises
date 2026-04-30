'''Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.'''

contagem = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')


while True:
    try:
        numero = int(input('Digite um número entre zero e vinte: '))
        if numero < 0 or numero > 20:
            print('Número inválido!')
        else:
            break
    except ValueError:
        print('Somente números são aceitos.')     
                    
print(f'Você digitou o número \033[33m{contagem[numero]}\033[m.')
