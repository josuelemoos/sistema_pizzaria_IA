import os
import sqlite3
import google.generativeai as genai

# Configurar chave da API
genai.configure(api_key=os.getenv("GEMINI_API_KEY", "AIzaSyCyhnB6Ceqm0KPgHyiFac3kUcniuBtPOK4"))

# ============================
# BANCO DE DADOS
# ============================
def criar_banco():
    conexao = sqlite3.connect("pizzaria.db")
    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pizzas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL
    )
    """)

    # Inserir alguns sabores (se ainda não existirem)
    cursor.execute("SELECT COUNT(*) FROM pizzas")
    if cursor.fetchone()[0] == 0:
        pizzas = [
            ("Calabresa", 35.00),
            ("Mussarela", 32.00),
            ("Frango com Catupiry", 38.00),
            ("Portuguesa", 40.00),
        ]
        cursor.executemany("INSERT INTO pizzas (nome, preco) VALUES (?, ?)", pizzas)
        conexao.commit()

    conexao.close()


# ============================
# CHATBOT GEMINI
# ============================
INSTRUCAO_SISTEMA = (
    "Você é um assistente de pedidos de uma pizzaria. "
    "Responda de forma curta e objetiva. "
    "Não use saudações ou despedidas."
)

def obter_resposta(pergunta: str) -> str:
    try:
        modelo = genai.GenerativeModel("gemini-1.5-flash")
        response = modelo.generate_content(f"{INSTRUCAO_SISTEMA}\nUsuário: {pergunta}")
        return response.text.strip()
    except Exception as e:
        return f"Erro na API: {e}"


# ============================
# EXECUÇÃO
# ============================
if __name__ == "__main__":
    criar_banco()
    print("Banco de dados pronto!\n")

    while True:
        pergunta = input("Você: ")
        if pergunta.lower() in ["sair", "exit", "quit"]:
            break
        resposta = obter_resposta(pergunta)
        print("Bot:", resposta)