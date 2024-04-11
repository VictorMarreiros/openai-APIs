from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client= OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
modelo="gpt-3.5-turbo",
# código omitido

prompt_sistema = f"""
        Você é um categorizador de produtos.
        Você deve assumir as categorias presentes na lista abaixo.

        # Lista de Categorias Válidas
            - Moda Sustentável
            - Produtos para o Lar
            - Beleza Natural
            - Eletrônicos Verdes

        # Formato da Saída
        Produto: Nome do Produto
        Categoria: apresente a categoria do produto

        # Exemplo de Saída
        Produto: Escova elétrica com recarga solar
        Categoria: Eletrônicos Verdes
    """

prompt_usuario=input("Apresente o nome de um produto: ")
 
response = client.chat.completions.create(
    model=modelo,
    temperature=0,
    max_tokens=200,
    n=3,
    messages=[
        {
            "role":"system",
            "content": prompt_sistema
        },
        {
            "role" : "user",
            "content": prompt_usuario
        }
    ]
)
print(response.choices[0].message.content)
    
