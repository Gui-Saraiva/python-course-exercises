'''Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
O programa será interrompido quando o número solicitado for negativo.'''

while True:
    valor = int(input('Quer ver a tabuada de qual valor? '))
    if valor < 0:
        break
    for t in range(1, 11):
        res = valor * t
        print(f'{valor} x {t} = {res}')
print('FIM!')