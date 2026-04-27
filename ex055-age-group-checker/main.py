#Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date

ano_atual = date.today().year
maiores = 0
menores = 0

for pessoas in range(1,8):
    nascimento = int(input(f'Em que ano nasceu a {pessoas}ª pessoa? '))
    idade = ano_atual - nascimento
    if idade >= 18:
        maiores += 1
    else:
        menores += 1

print(f'Temos {maiores} pessoas maiores de idade.')
print(f'Temos {menores} menores de 18 anos.')