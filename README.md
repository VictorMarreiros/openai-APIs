# openai-APIs

## Curso Alura


### Notas:

**Criar ambiente**: python -m venv venv

**Ativar ambiente**: venv\Scripts\activate.bat

**Desativar ambiente**: venv\Scripts\deactivate.bat

**Instalar libraries**: pip install -r requirements.txt

**Exportar libraries de um projeto:** pip freeze > requirements.txt 

**VS Code:** 
- Certifique-se de que o ambiente virtual esteja selecionado como interpretador Python. Use o atalho `Ctrl+Shift+P` e selecione o Interpretador Python dentro do diretório `bin` no diretório `.venv`.


---

O curso abordou de forma bem prática os fundamentos de prompt engeenering e toda a plataforma da openAI. Dentre todos os temas desmistificados, destaco algumas anotações do foi praticado em aula:

* Selecionar o modelo de linguagem adequado para nossas tarefas, considerando os limites de tokens, contexto e custo e escolhendo com base nas necessidades específicas do projeto.

* Utilizar a biblioteca TikToken para contar e estimar a quantidade de tokens em um texto para avaliar o uso de modelos de linguagem, entender a estrutura interna dos tokens e calcular custos de processamento.

* Escolher dinamicamente modelos de linguagem com base no número de tokens da entrada e a calcular o tamanho esperado da saída para garantir o funcionamento adequado da geração de texto.