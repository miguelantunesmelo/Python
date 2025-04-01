real = float(input('Quanto você tem na carteira? R$'))
dolar = real / 6.12
print('Com R${:.2f} você pode comprar U${:.2f}'.format(real, dolar))
