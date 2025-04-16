time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou?'))
    for c in range(0, tot):
        partidas.append(int(input(f'  Quantos gol na partida {c}? ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
        if resp in 'SN':
             break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
         break
print('-' * 40)
for k, v in enumerate(time):
     print(f'{k:>3}', end='')
     for d in v.values():
        print(f'{str(d):<15}', end='')
        print()
print('-' * 40)
print('-=' * 30)
print(jogador)
print('-=' * 30)
for k, v in jogador.items():
        print(f'O campo {k} tem o valor {v}')
print('-=' * 30)
print(f'O jogador {jogador["nome"]} jogou {len(jogador["gols"])} partidas.')
for i, v in enumerate(jogador['gols']):
      print(f'  => Na partida {i}, fez {v} gols.')
print(f'Foi um total de {jogador["total"]} gols.')
