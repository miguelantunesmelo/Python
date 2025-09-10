import matplotlib.pyplot as plt
from collections import Counter

# Classe para representar um livro 
class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def __str__(self):
        return f'{self.titulo} por {self.autor}, Publicado em {self.ano_publicacao}'
    
# Criar uma lista de livros 
biblioteca = []

# Lista para armazenar anos de publicação 
anos = []

# Função para adicionar um livro à biblioteca
def adicionar_livro(titulo, autor, ano_publicacao):
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)  # Adiciona o ano à lista anos
    print(f'O livro "{titulo}" foi adicionado à biblioteca.')

# Função para listar todos os livros na biblioteca
def listar_livros():
    print('Livros na Biblioteca:')
    for livro in biblioteca:
        print(livro)

# Adicionar alguns livros à biblioteca
adicionar_livro('Dom Quixote', 'Miguel de Cervantes', 1605)
adicionar_livro('Orgulho e Preconceito', 'Jane Austen', 1967)
adicionar_livro('1984', 'George Orwell', 1949)
adicionar_livro('Cem Anos de Solidão', 'Gabriel Garcia Marquez', 1967)
adicionar_livro('Apanhador no Campo de Centeio', 'J.D. Salinger', 1951)

# Listar todos os livros na biblioteca 
listar_livros()

# Contagem de livros por ano
contagem = Counter(anos)
anos_unicos = sorted(contagem.keys())
contagem_por_ano = [contagem[ano] for ano in anos_unicos]

# Criar um gráfico de linha 
plt.plot(anos_unicos, contagem_por_ano, marker='o', linestyle='-')
plt.xlabel('Ano de Publicação')
plt.ylabel('Número de Livros')
plt.title('Distribuição de Livros na Biblioteca por Ano de Publicação')

# Adicionar rótulos aos pontos de dados
for i, valor in enumerate(contagem_por_ano):
    plt.text(anos_unicos[i], valor, str(valor), ha='center', va='bottom')

plt.grid(True)
plt.show()
