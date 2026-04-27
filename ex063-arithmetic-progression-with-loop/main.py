primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('A razão: '))
cont = 0
total = 0
mais = 10

while mais != 0:
    total = total + mais # para contar quantos termos foram apresentados e fazer o loop abaixo rodar até cont voltar a se igualar ao total. Ambas não resetam.
    while cont < total: # cada vez que digita um numero novo para 'mais' ele soma no total, e cont fica menor e repete o loop até ficar igual novamente.
        print(primeiro_termo, '→', end=' ')
        primeiro_termo += razao
        cont += 1
    print('PAUSA')
    mais = int(input('Mais termos? Quantos? ')) # para o loop e atualiza a variavel 'mais' dizendo quantas mais vai mostrar termos. Igualando ao total para contar os termos.

print(f'Progressão finalizada e {total} termos foram mostrados.')
