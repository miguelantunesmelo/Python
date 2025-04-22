def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')

    cont = i
    while cont <= f:
        print(f'{cont} ', end='')
        cont += p
    print('FIM!')

# Programa principal
contador(1, 10, 1)