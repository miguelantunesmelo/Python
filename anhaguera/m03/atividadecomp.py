import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar ao banco em memória
conn = sqlite3.connect(":memory:")
cursor = conn.cursor()

# Criar tabelas
cursor.execute("""
CREATE TABLE Produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    categoria TEXT,
    preco REAL
)
""")

cursor.execute("""
CREATE TABLE Vendas (
    id INTEGER PRIMARY KEY,
    produto_id INTEGER,
    data DATE,
    quantidade INTEGER,
    FOREIGN KEY(produto_id) REFERENCES Produtos(id)
)
""")

# Inserir dados fictícios
produtos = [
    (1, "Notebook", "Eletrônicos", 3500.0),
    (2, "Smartphone", "Eletrônicos", 2500.0),
    (3, "Camiseta", "Vestuário", 80.0),
    (4, "Tênis", "Vestuário", 200.0),
    (5, "Geladeira", "Eletrodomésticos", 2800.0)
]
cursor.executemany("INSERT INTO Produtos VALUES (?, ?, ?, ?)", produtos)

vendas = [
    (1, 1, "2024-01-05", 5),
    (2, 2, "2024-01-06", 8),
    (3, 3, "2024-01-07", 20),
    (4, 4, "2024-01-08", 12),
    (5, 5, "2024-01-09", 4),
    (6, 1, "2024-01-15", 7),
    (7, 2, "2024-01-16", 10),
    (8, 3, "2024-01-17", 25),
    (9, 4, "2024-01-18", 15),
    (10, 5, "2024-01-19", 6)
]
cursor.executemany("INSERT INTO Vendas VALUES (?, ?, ?, ?)", vendas)

conn.commit()

# Carregar dados
df = pd.read_sql_query("""
SELECT v.data, p.nome, p.categoria, v.quantidade, p.preco
FROM Vendas v
JOIN Produtos p ON v.produto_id = p.id
""", conn)

print(df.head())

# 📊 Gráfico de vendas por produto
plt.figure(figsize=(8,5))
sns.barplot(data=df, x="nome", y="quantidade", estimator=sum)
plt.title("Quantidade de Vendas por Produto")
plt.show()

# 📈 Gráfico de evolução das vendas no tempo
plt.figure(figsize=(8,5))
df_grouped = df.groupby("data")["quantidade"].sum().reset_index()
sns.lineplot(data=df_grouped, x="data", y="quantidade", marker="o")
plt.title("Evolução das Vendas")
plt.show()

# 🥧 Gráfico de participação por categoria
plt.figure(figsize=(6,6))
df_grouped_cat = df.groupby("categoria")["quantidade"].sum()
plt.pie(df_grouped_cat, labels=df_grouped_cat.index, autopct="%1.1f%%")
plt.title("Participação das Categorias nas Vendas")
plt.show()
