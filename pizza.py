from google import genai
import os

def obter_resposta_curta_pizzaria(pergunta: str) -> str:
    """
    Recebe uma pergunta (string) e retorna uma resposta curta (string) 
    como um assistente de pizzaria, utilizando o Gemini API.

    Args:
        pergunta: A pergunta ou pedido do cliente.

    Returns:
        A resposta curta do modelo ou uma mensagem de erro.
    """
    
    # 1. Instrução de Sistema para o papel e o formato de resposta
    INSTRUCAO_SISTEMA = (
        "Você é um assistente de pedidos de uma pizzaria. "
        "Sua função é fornecer respostas EXTREMAMENTE CURTAS (no máximo uma frase) e diretas. "
        "Não use saudações ou despedidas."
    )
    
    # 2. Verificar a Chave API
    if os.getenv("GEMINI_API_KEY") is None:
        return "\nERRO: A variável de ambiente GEMINI_API_KEY não está configurada."

    try:
        # 3. Inicializar o cliente
        client = genai.Client()
        
        # 4. Chamar a API
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=pergunta,
            config={"system_instruction": INSTRUCAO_SISTEMA}
        )
        
        # 5. Retornar apenas o texto da resposta
        return response.text.strip()

    except Exception as e:
        # Retorna a mensagem de erro da API
        return f"Ocorreu um erro na API: {e}"


# --- Exemplo de uso da função ---

# String de entrada (a pergunta)
pergunta_do_cliente = "Quais são os sabores de pizza mais populares que você tem?"

# Obter a string de resposta
resposta_da_pizzaria = obter_resposta_curta_pizzaria(pergunta_do_cliente)

# Printar a string de resposta
print(f"Pergunta: {pergunta_do_cliente}")
print(f"Resposta: {resposta_da_pizzaria}")

# --- Outro exemplo ---
pergunta_2 = "Preciso de uma pizza grande de calabresa. Qual o preço?"
resposta_2 = obter_resposta_curta_pizzaria(pergunta_2)

print("\n--------------------------")
print(f"Pergunta: {pergunta_2}")
print(f"Resposta: {resposta_2}")