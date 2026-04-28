'''Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.'''

mais = maior = soma = cont = 0
continuar = ''

while continuar != 'n':
    mais = int(input('Digite um numero: '))
    soma += mais
    cont += 1 
    if cont == 1:
        maior = menor = mais # no inicio maior e menor recebem o mesmo valor de mais. Depois ele verfica qual é menor e maior no if abaixo.
    else:
        if mais < menor:
            menor = mais
        if mais > maior:
            maior = mais
    continuar = input('Quer continuar? [s/n] ').lower().strip()
    while continuar not in ('n','s'):
        continuar = input('Opção inválida. Tente novamente [s/n] ').lower().strip()
    
media = soma / cont
print(f'Foram mostrados {cont} números. \nA soma deles = {soma}. \nA média = {media:.1f}')
print('maior =', maior)
print('menor =', menor)