'''Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder,
mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.'''

from random import randint

vitoria = 0

while True:
    par_impar = ''
    while par_impar not in ('P','I'):
        par_impar = input('Par ou Ímpar? [P ou I]: ').upper().strip()
    player = int(input('Digite um número: '))
    computador = randint(0,5)   
    soma = player + computador
    resultado = soma % 2

    print('Você escolheu PAR' if par_impar == 'P' else 'Você escolheu ÍMPAR')
    print(f'Você jogou {player} o computador jogou {computador}, total = {soma}.')
    print('DEU PAR!' if soma % 2 == 0 else 'DEU ÍMPAR!',end=' ')

    escolha = 0 if par_impar == 'P' else 1
    if escolha == resultado:
            print('Venceu!')
            vitoria += 1
    else:
        print('Perdeu!')
        break
print(f'GAME OVER! {vitoria} vitórias consecutivas.')
