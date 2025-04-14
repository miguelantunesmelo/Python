temp = []
princ = []

while True:
    temp.append(str(input('Nome: ')))
    temp.append(str(input('Peso: ')))
    princ.append(temp[:])
    temp.clear
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-=' * 30)
print(f'Os dados foram {princ}')