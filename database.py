import sqlite3

# Conecta ou cria o banco de dados
conn = sqlite3.connect("pizzaria.db")
cursor = conn.cursor()

# Criar tabela de produtos
cursor.execute("""
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    preco REAL NOT NULL,
    descricao TEXT
)
""")

# Criar tabela de pedidos
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente TEXT NOT NULL,
    produto_id INTEGER NOT NULL,
    quantidade INTEGER NOT NULL,
    total REAL NOT NULL,
    data TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(produto_id) REFERENCES produtos(id)
)
""")

# Criar tabela de perguntas e respostas (opcional)
cursor.execute("""
CREATE TABLE IF NOT EXISTS perguntas_respostas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pergunta TEXT NOT NULL,
    resposta TEXT NOT NULL
)
""")

# Salvar alterações e fechar conexão
conn.commit()
conn.close()

print("Banco de dados criado com sucesso!")