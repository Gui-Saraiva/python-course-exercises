'''Crie um programa que tenha uma tupla com várias palavras.
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.'''

palavras = ('Guilherme', 'Angela', 'Pedro', 'Lana', 'Lucas', 'Amanda', 'João')

for p in palavras:
    print(f"\nO nome {p.upper()} temos as vogais ", end='') #quebra de linha faz imprimir um valor abaixo do outro com o end='' no final pegando os debaixo e colocando do lado.
    for vogais in p:
        if vogais in 'AÁaáÃãEeÉéÊêIiÍíOoÔôÓóUuÚú':
            print(f'"{vogais.upper()}"',end=' ')
