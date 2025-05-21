def ficha(jog, gol):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# Programa Principal
n = str(input('Nome do Jogador: '))
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else: 
    g = 0
if n.strip() == '':
    ficha(gol=g)
else:
    ficha(n, g)