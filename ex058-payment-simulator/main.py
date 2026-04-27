'''
Elabore um programa que calcule o valor a ser pago por um produto,
considerando o seu preço normal e condição de pagamento:
- à vista dinheiro/cheque: 10% de desconto
- à vista no cartão: 5% de desconto
- em até 2x no cartão: preço formal
- 3x ou mais no cartão: 20% de juros
'''

produto = float(input('Valor do produto R$: ').strip().replace(',','.'))
produto_format = f"{produto:.2f}".replace('.',',')

pagamento = int(input('''Condições de pagamento:
[1] - À vista ou cheque: 10% de desconto 
[2] - À vista no cartão: 5% de desconto
[3] - Até 2x no cartão: preço formal
[4] - 3 ou mais vezes no cartão: 20% de juros
Digite opção escolhida: '''))

if pagamento == 1:
    valor = produto - (produto * 0.10 )
    valor_format = f"{valor:.2f}".replace('.',',')
    print(f'Sua compra de R$ {produto_format} fica R$ {valor_format}.')
elif pagamento == 2:
    valor = produto - (produto * 0.05)
    valor_format = f"{valor:.2f}".replace('.',',')
    print(f'Sua compra de R$ {produto_format} fica R$ {valor_format}.')
elif pagamento == 3:
    parcelado = int(input('Quantas vezes? '))
    if parcelado == 1:
        print(f'Sua compra fica no valor total de R$ {produto_format} reais.')
    elif parcelado == 2:
        duas_vezes = produto / parcelado
        duas_vezes_format = f"{duas_vezes:.2f}".replace('.',',')
        print(f'Sua compra fica com mensalidade de R$ {duas_vezes_format} reais.')
    else:
        print('Essa opção de pagamento aceita apenas 1 ou 2 vezes. Tente novamente.')
elif pagamento == 4:
    parcelado = int(input('Quantas vezes? '))
    if parcelado >= 3 and parcelado <= 10:
        valor_mensal = (produto + (produto * 0.2)) / parcelado
        valor_mensal_format = f"{valor_mensal:.2f}".replace('.',',')
        print(f"Sua compra de R$ {produto_format} em {parcelado} vezes fica R$ {valor_mensal_format} por mês.")
    elif parcelado == 1 or parcelado == 2 or parcelado > 10:
        print('Parcelamento somente de 3 a 10 vezes.')
    else:
        print('Opção inválida! Tente novamente.')
else:
    print('Opção Inválida! Tente novamente.')