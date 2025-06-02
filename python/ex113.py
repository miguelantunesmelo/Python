def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('ERRO: por favor, digite um número inteiro válido.')
            continue
        else:
            return n


num = leiaInt('Digite um valor: ')
print(f'O valor digitado foi {num}')
