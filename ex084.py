temp = []
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    princ.append(temp[:])
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print(f'Os dados foram {princ}')