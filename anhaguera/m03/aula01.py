import sqlite3
# CREATE (Criação de tabela e inserção de dados de exemplo)
conn = sqlite3.connect('contatos.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXIST Contatos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        email TEXT,
        telefone TEXT     
    )
''')
dados_exemplo = [
    
]
