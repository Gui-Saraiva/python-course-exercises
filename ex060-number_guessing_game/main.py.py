# Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.

from random import randint

print('Sou o computador. Vou pensar um número de 0 a 10 e você tenta acertar.')

pc = randint(0, 10)
player = -1
tentativas = 0

while player != pc:
    player = int(input('Que número eu pensei? '))
    tentativas += 1
    if player < pc:
        print('Mais! Tente novamente.')        
    elif player > pc:
        print('Menos! Tente novamente')
print(f'\033[1;31;43mAcertou! Em {tentativas} tentativas.\033[m')