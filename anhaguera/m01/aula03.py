# Lista de filmes para classificação 
filmes = ['Filme 1', 'Filme 2', 'Filme 3', 'Filme 4', 'Filme 5']

# Mensagens de boas-vindas
print('Bem-vindo à classificação de filmes!')
print('Você tem cinco filmes para classificar.')
print('Digite. '0' a qualquer momento parar.\n')

# Loop para iterar sobre cada filme na lista
for filme in filmes:
    # Solicita a classifcação  ao usuário ~
    classificacao == input(f'Como você classificaria {filme} de 1 a 5? (ou 0 para parar): ')

    # Verifica se o usuário deseja parar
    if classificacao == '0':
        print('Que pena que você não irá classificar mais os filmes.')
        break   # Encerra o loop principal

    # Converte classificação para um número inteiro 
    classificacao = int(classificacao)

    # Verifica se a classificação está dentro do intervalo válido 
    if classificacao < 1 or classificacao > 5:
        print('Por favor, digite uma classificação válida de 1 a 5.')
    else:
        # Exibe a classificação e passa para o próximo filme
        print(f'Voçê classificou {filme} com {classificacao} estrelas.\n')

# Mensagens de agradecimento ao finalizar 
print('Obrigado por classificar os filmes!')
