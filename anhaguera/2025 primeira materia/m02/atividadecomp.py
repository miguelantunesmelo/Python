# Importar biblioteca para gráficos
import matplotlib.pyplot as plt

# Classe Livro: representa cada livro na biblioteca
class Livro:
    def __init__(self, titulo, autor, genero, quantidade):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.quantidade = quantidade

    def __str__(self):
        return f'"{self.titulo}" por {self.autor} | Gênero: {self.genero} | Quantidade: {self.quantidade}'

# Lista para armazenar os livros
biblioteca = []

# Função para cadastrar um novo livro
def cadastrar_livro(titulo, autor, genero, quantidade):
    novo_livro = Livro(titulo, autor, genero, quantidade)
    biblioteca.append(novo_livro)
    print(f'Livro "{titulo}" cadastrado com sucesso!')

# Função para listar todos os livros
def listar_livros():
    if not biblioteca:
        print("Nenhum livro cadastrado.")
    else:
        print("Livros na Biblioteca:")
        for livro in biblioteca:
            print(livro)

# Função para buscar livro por título
def buscar_livro(titulo):
    for livro in biblioteca:
        if livro.titulo.lower() == titulo.lower():
            print("Livro encontrado:")
            print(livro)
            return
    print(f'Livro "{titulo}" não encontrado.')

# Função para gerar gráfico da quantidade de livros por gênero
def grafico_genero():
    if not biblioteca:
        print("Nenhum livro para gerar gráfico.")
        return

    # Contar quantidade de livros por gênero
    generos = {}
    for livro in biblioteca:
        if livro.genero in generos:
            generos[livro.genero] += livro.quantidade
        else:
            generos[livro.genero] = livro.quantidade

    # Preparar dados para gráfico
    nomes_generos = list(generos.keys())
    quantidades = list(generos.values())

    # Criar gráfico
    plt.bar(nomes_generos, quantidades, color='skyblue')
    plt.xlabel('Gênero')
    plt.ylabel('Quantidade de Livros')
    plt.title('Distribuição de Livros por Gênero')
    plt.grid(axis='y')
    
    # Adicionar rótulo em cima de cada barra
    for i, valor in enumerate(quantidades):
        plt.text(i, valor + 0.1, str(valor), ha='center')
    
    plt.show()

# -----------------------------
# Exemplo de uso do sistema
# -----------------------------

cadastrar_livro("Dom Quixote", "Miguel de Cervantes", "Romance", 3)
cadastrar_livro("1984", "George Orwell", "Distopia", 5)
cadastrar_livro("Cem Anos de Solidão", "Gabriel Garcia Marquez", "Romance", 4)
cadastrar_livro("O Senhor dos Anéis", "J.R.R. Tolkien", "Fantasia", 6)

listar_livros()

buscar_livro("1984")
buscar_livro("O Pequeno Príncipe")  # Exemplo de livro não cadastrado

grafico_genero()
