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

