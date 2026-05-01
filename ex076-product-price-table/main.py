'''Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.'''

tabela = ('Lápis', 1.00, 'Borracha', 1.50, 'Caneta', 1.50, 'Caderno', 9.99, 'Mochila', 39.90, 'Fichário', 25.50, 'Estojo', 8.75, 'Lápis de cor', 10.50)

print('-' * 38)
print(f"{'LISTA DE MATERIAL ESCOLAR':^38}")
print('-' * 38)

for pos in range(0, len(tabela)):
    if pos % 2 == 0:
        print(f'{tabela[pos]:.<30}',end='') # ao imprimir com [pos] ele mostra um item de cada vez um abaixo do outro.
    else:
        print(f'R$ {tabela[pos]:.2f}')

print('-' * 38)