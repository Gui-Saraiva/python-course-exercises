'''Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
a) Os 5 primeiros times. b) Os últimos 4 colocados. c) Times em ordem alfabética. d) Em que posição está o time do Grêmio.'''

print('-=' * 30)
print('CAMPEONATO BRASILEIRO - 30/04/2026 (18:33)')
print('-=' * 30)
tabela = ('Palmeiras', 'Flamengo', 'Fluminense', 'São Paulo', 'Atlético-PR', 'Bahia', 'Coritiba',
          'Botafogo', 'Bragantino', 'Vasco', 'Grêmio', 'Cruzeiro', 'Vitória', 'Corinthians',
          'Atlético-MG', 'Internacional', 'Santos', 'Mirassol', 'Remo', 'Chapecoense')

# mostrando a tupla em lista
posicao = 0
for t in tabela:
    posicao += 1
    print(f'{posicao}º {t}')

print('-' * 30)
print(tabela[:5])
print('-' * 30)
print(tabela[-4:])
print(sorted(tabela))
print('-' * 30)
print(f'Grêmio está em {tabela.index('Grêmio')+1}º no campeonato.')
