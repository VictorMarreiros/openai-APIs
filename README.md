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

O curso abordou de forma bem prática os fundamentos de prompt engeenering e todo o ecossistema da openAI usando ChatGPT e GPT-4. Dentre todos os temas desmistificados, destaco algumas anotações importantes dos ensinamentos foi praticado em aula:

* Selecionar o modelo de linguagem adequado para nossas tarefas, considerando os limites de tokens, contexto e custo e escolhendo com base nas necessidades específicas do projeto.

* Utilizar a biblioteca TikToken para contar e estimar a quantidade de tokens em um texto para avaliar o uso de modelos de linguagem, entender a estrutura interna dos tokens e calcular custos de processamento.

* Escolher dinamicamente modelos de linguagem com base no número de tokens da entrada e a calcular o tamanho esperado da saída para garantir o funcionamento adequado da geração de texto.

* Usar modelos de linguagem para realizar análise de sentimentos em avaliações de produtos, resumindo as avaliações, determinando o sentimento geral (positivo, neutro ou negativo), identificando pontos fortes e pontos fracos e salvando os resultados em arquivos.

* Refatorar o código para processar análises de sentimentos em lotes, utilizando uma função para realizar a análise para cada produto da lista, e adicionar prints para acompanhar o progresso e identificar possíveis erros durante a análise em lote.

* Lidar com exceções ao realizar chamadas em lote para uma API utilizando blocos de código try e except para capturar e tratar diferentes tipos de erros.

* Implementar uma lógica de retentativa, na qual tentamos novamente a chamada após um curto intervalo de tempo em caso de erro, para lidar com problemas temporários.

* Lidar com os limites de taxa na utilização da API GPT, que são definidos pela quantidade de requisições por dia (RPD), requisições por minuto (RPM) e quantidade de tokens por minuto (TPM).


---


Selecionar o modelo de linguagem adequado para nossas tarefas, considerando os limites de tokens, contexto e custo e escolhendo com base nas necessidades específicas do projeto:

Esta etapa envolve uma análise cuidadosa das necessidades do projeto, considerando fatores como a quantidade de tokens disponíveis nos modelos, a complexidade do contexto necessário e o custo associado ao uso desses modelos.
Utilizar a biblioteca TikToken para contar e estimar a quantidade de tokens em um texto para avaliar o uso de modelos de linguagem, entender a estrutura interna dos tokens e calcular custos de processamento:

A biblioteca TikToken é uma ferramenta útil para calcular a quantidade de tokens em um texto, o que é essencial para entender e controlar os custos associados ao processamento de linguagem natural. Ela também fornece insights sobre a estrutura interna dos tokens, facilitando a escolha e otimização dos modelos de linguagem.
Escolher dinamicamente modelos de linguagem com base no número de tokens da entrada e calcular o tamanho esperado da saída para garantir o funcionamento adequado da geração de texto:

Esta abordagem adaptativa garante que escolhamos os modelos de linguagem mais apropriados com base nas características do texto de entrada, como seu tamanho e complexidade, garantindo assim uma geração de texto eficaz e eficiente.
Usar modelos de linguagem para realizar análise de sentimentos em avaliações de produtos, resumindo as avaliações, determinando o sentimento geral (positivo, neutro ou negativo), identificando pontos fortes e pontos fracos e salvando os resultados em arquivos:

Esta tarefa envolve a utilização de modelos de linguagem para analisar o sentimento de avaliações de produtos, destacando aspectos positivos e negativos e resumindo o sentimento geral, o que pode ser valioso para entender a percepção dos clientes e melhorar os produtos.
Refatorar o código para processar análises de sentimentos em lotes, utilizando uma função para realizar a análise para cada produto da lista, e adicionar prints para acompanhar o progresso e identificar possíveis erros durante a análise em lote:

Esta etapa visa melhorar a eficiência do código, permitindo a análise de múltiplos produtos em lotes. Adicionar prints para acompanhar o progresso e identificar erros ajuda na depuração e na garantia de que o processo está ocorrendo conforme o esperado.
Lidar com exceções ao realizar chamadas em lote para uma API utilizando blocos de código try e except para capturar e tratar diferentes tipos de erros:

É importante implementar tratamento de exceções para lidar com possíveis erros durante chamadas em lote para uma API, garantindo que o código seja robusto e capaz de lidar com problemas de forma adequada.
Implementar uma lógica de retentativa, na qual tentamos novamente a chamada após um curto intervalo de tempo em caso de erro, para lidar com problemas temporários:

Esta estratégia de retentativa é útil para lidar com problemas temporários, como congestionamento de rede ou falhas momentâneas de servidores, garantindo uma maior resiliência e confiabilidade no sistema.
Lidar com os limites de taxa na utilização da API GPT, que são definidos pela quantidade de requisições por dia (RPD), requisições por minuto (RPM) e quantidade de tokens por minuto (TPM):

É essencial respeitar os limites de taxa estabelecidos pela API GPT para evitar suspensões ou restrições de acesso. Monitorar e gerenciar adequadamente esses limites é crucial para garantir uma utilização sustentável e eficaz da API.