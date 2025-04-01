from time import sleep 
print('-=-' * 20)
print('Analisador de Triângulos')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segemento: '))
r3 = float(input('Terceiro segmento: '))
print(' PROCESSANDO...')
sleep(3)
if r1 < r2 + r3 and r2 > r1 + r3 and r3 < r1 + r2:
    print('Os segemnetos acima PODEM FORMAR um triângulo!')
else:
    print('Os segementos acima NÃO PODEM FORMAR um triângulo! ')
    