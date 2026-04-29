'''Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
A) qual é o total gasto na compra. B) quantos produtos custam mais de R$1000. C) qual é o nome do produto mais barato.'''

print('-' * 40)
print(f"{'\033[33mLOJA SARAIVA\033[m':^47}")
print('-' * 40)

soma = cont_produtos = cont_1000 = barato = 0
produto_barato = ''

while True:
    produto = input('Produto: ')
    while True:
        try:
            valor = float(input('Preço R$: ').replace(',','.'))       
            break
        except ValueError:
            print('Digite um valor numérico.')
    soma += valor
    cont_produtos += 1
    sair = ' '

    if valor > 1000:
        cont_1000 += 1

    if cont_produtos == 1 or valor < barato:
        barato = valor
        produto_barato = produto.title()

    while sair not in ('S', 'N'):
        sair = input('Cadastrar um novo produto?: [S/N] ').upper().strip()
    
    if sair == 'N':   
        break
print('-' * 40)
print(f"{'PROGRAMA ENCERRADO':^40}")
print('-' * 40)
print(f'Total da compra R$ {soma:.2f}')
print(f'{cont_1000} produtos custaram mais de R$ 1.000,00')
print(f'A compra mais em conta foi {produto_barato}')