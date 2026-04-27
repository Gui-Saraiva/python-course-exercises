# Faça um programa que leia um número qualquer e mostre o seu fatorial.

# while loop version
print('while loop version')
num = int(input('Digite um número e veja seu fatorial: '))
resultado = 1

print(f'{num}! = ', end='') # imprime essa frase antes do laço com o numero digitado pelo usuário. Depois imprime todos os numeros do laço abaixo.

while num > 0: #enquanto o numero digitado nao chegar em 1 o laço segue fazendo resultado * num. Diminuindo 1 do num a cada loop.
    resultado *= num # multiplica o número pelo resultado, atualizando a variavel resultado acima a cada loop.
    print(f'{num}', end=' ') # depois de cada multiplicação imprime um 'x' na frente do numero.
    print('x' if num > 1 else '=', end=' ' ) # se o numero for maior q 1 continua mostrando x depois do numero senao imprime um =.
    num -= 1 # diminui 1 do numero digitado pelo usuário a cada loop.

print(resultado) # imprime o resultado no fim de tudo.


# for loop version
print('for loop version')
numero = int(input('Digite um número: '))
res = 1

print(f'{numero}! =', end=' ')

for f in range(numero, 0, -1):
    res *= f
    print(f'{f}', end=' ')
    print('x' if f > 1 else '=', end=' ')
    
print(res)