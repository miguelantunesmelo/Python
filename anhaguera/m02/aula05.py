import matplotlib.pyplot as plt

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
def adicionar_livro(titulo, autor, ano_publicacao)
    novo_livro = Livro(titulo, autor, ano_publicacao)
    biblioteca.append(novo_livro)
    anos.append(ano_publicacao)  # Adicona o ano à lista anos
    print(f'O livro {titulo} foi adicionado à biblioteca.')

# Função para listar todos os livros na biblioteca
def listar_livros():
    print('Livros na Biblioteca:')
    for livro in biblioteca:
        print(livro)

# Adicionar alguns livros à biblioteca
