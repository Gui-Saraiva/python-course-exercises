anterior1 = 0
anterior2 = 1
terceiro = anterior1 + anterior2
continuar = int(input('Quantos termos você deseja ver? '))
cont = 2
total = 2

print(f'{anterior1} → {anterior2} →', end=' ')

while continuar != 0:
    total = total + continuar
    while cont < total:
        cont += 1
        terceiro = anterior1 + anterior2
        anterior1 = anterior2
        anterior2 = terceiro
        print(terceiro, end=' → ')
    continuar = int(input('Quer ver mais termos? Quantos? '))      
print('FIM')
