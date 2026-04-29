saque = qtd_cedula = 0
cedula = 200

print('=' * 40)
print(f"{'BANCO SARAIVA':^40}")
print('=' * 40)

while True:  
    while True:  
        try:
            saque = int(input('Valor do saque: R$ '))
            if saque == 0:
                print('Digite um valor maior que zero.')
                continue #pula o resto e recomeça o loop
            break  
        except ValueError:            
            print('Digite um valor numérico.')

    while True:    
        qtd_cedula = saque // cedula
        saque = saque % cedula
        if qtd_cedula > 0:
            print(f'{qtd_cedula} notas de {cedula}')
        if cedula == 200:
            cedula = 100
        elif cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 1
        else:
            break

    saque = qtd_cedula = 0
    cedula = 200

    sair = ' '   
    while sair not in ('S','N'):
        sair = input('Deseja fazer outro saque? [S/N] ').upper().strip()
    if sair == 'N':
        break

print('-' * 40)
print(f"{'SESSÃO ENCERRADA.':^40}")
print('-' * 40)
                
    

