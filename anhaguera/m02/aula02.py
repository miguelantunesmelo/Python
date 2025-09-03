# Importe as bibliotecas necessárias 
import numpy as np
# Dados dos partcipantes 
participantes = [
    {
        'nome': 'Alice',
        'localização': 'EUA',
        'afiliação': 'Universidade A',
        'interesses': ['Física', 'Astronomia']
    },
     {
        'nome': 'Bob',
        'localização': 'Brasil',
        'afiliação': 'Universidade B',
        'interesses': ['Biologia', 'Astronomia']
    },
    {
        'nome': 'Charlie',
        'localização': 'Índia',
        'afiliação': 'Universidade C',
        'interesses': ['Química', 'Astronomia']
    }
    # Adicionando mais participantes conforme necessário
]
# Usando sets para  identificar diferentes regiões dos participantes 
regioes = set(participante['localizacao'] for participante in participantes)
# Usando um dicionário para categorizar afiliações
afiliacoes = {}
for participante in participantes:
    afiliacao = participante['afiliacao']
    if afiliacao not in afiliacoes:
        afiliacoes[afiliacao] = []
    afiliacoes[afiliacao].append(participante['nome'])
# Usando NumPy para analisar áreas de interesse
