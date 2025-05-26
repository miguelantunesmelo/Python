from time import sleep
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
m = (n1 + n2) / 2 
print('-=-' * 10)
print('A sua média foi {:.1f}'.format(m))
print('PROCESSANDO...')
sleep(3)
if m>= 6.0:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')
print('-=-' * 10)

