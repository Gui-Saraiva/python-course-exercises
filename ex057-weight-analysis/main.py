# Faça um programa que leia o peso de cinco pessoas. No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
pessoa_maior = 0
pessoa_menor = 0

for pessoa in range(1,6):
    peso = float(input(f'Digite o peso da {pessoa}ª pessoa: '))
    if pessoa == 1: #coloca o primeiro do loop com o peso igual nas duas variaveis e no numero 1 da variavel pessoa do for.
        maior = peso #adiciona o primeiro valor digitado na variavel maior.
        menor = peso #adiciona o mesmo primeiro valor digitado na menor também.
        pessoa_maior = pessoa #adiciona o numero 1 do loop
        pessoa_menor = pessoa #adiciona o 1 do loop para a pessoa_menor também.
    else:
        if peso > maior: #compara se o peso atual é maior que o maior já encontrado.
            maior = peso #adiciona o peso maior dado em determinado loop.
            pessoa_maior = pessoa #adiciona o numero da pessoa do loop com o maior peso.
        if peso < menor: #o mesmo acontece com o menor
            menor = peso
            pessoa_menor = pessoa

print(f'A {pessoa_menor}ª pessoa teve o menor peso = {menor}kg')
print(f'A {pessoa_maior}ª pessoa teve o maior peso = {maior}kg')