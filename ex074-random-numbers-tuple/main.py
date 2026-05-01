'''Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. Depois disso,
mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.'''

from random import randint

numeros = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

for n in numeros: # percorro os valores da tupla, nao os índices.
    print(n, end=' ')  

print(f'\nMaior = {max(numeros)}') # função da tupla max() para dizer qual o numero maior
print(f'Menor = {min(numeros)}') # o mesmo para o menor.


''' versao avançada que pode criar numeros ilimitados dentro de um for, mas criando uma lista vazia primeiro e depois convertendo ela pra tupla.
numeros = []

for n in range(5):    
    numeros.append(randint(1,10)) #adicionando novo valor na lista

tupla = tuple(numeros)

print(tupla)
print(max(tupla))
print(min(tupla))
'''