import sqlite3
# Passo 1: Conectar ao banco de dados SQLite (ou criá-lo se não existir)
conn = sqlite3.connect('funcionarios.db')

# Passo 2: Criar a tabela de funcionários
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS funcionarios (
        id INTEGER PRIMARY KEY,
            nome TEXT,
            cargo TEXT,
            salario REAL 
    )
''')

# Passo 3: Inserir um novo funcionário na tabela
novo_funcionario = (1, 'João', 'Analista', 5000.00)
cursor.execute('INSERT INTO funcionarios VALUES (?, ?, ?, ?)', novo_funcionario)
conn.commit()

# Passo 4: Consultar e exibir funcionários
cursor.execute('SELECT * FROM funcionarios')
funcionarios = cursor.fetchall()
print('Funcionários Cadastrados:')
for funcionario in funcionarios:
    print(funcionario)

