# -*- coding: utf-8 -*-
"""Curso GPT Especializando com seus Dados.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1igYTtJ25PyRb9KwtbxV7mskpdJflmS4G

# Curso GPT Especializando com seus Dados

## Instruções iniciais

Você precisará de uma chave da OpenAI.
Faça seu cadastro e obtenha a chave em: https://platform.openai.com/account/api-keys


Documentação OpenAI: https://platform.openai.com/docs/api-reference


Criado por: Gibram Raul

Technium Sistemas Inteligentes - https://technium.me/

Linkedin: https://www.linkedin.com/in/gibramraul/

## Informações de preço de uso da API da OpenIA:
OBS: TODAS AS INFORMAÇÕES ESTÃO EM DÓLAR


Há vários modelos, cada um com diferentes capacidades e preços. Os preços são por 1000 tokens. Você pode pensar em tokens como pedaços de palavras, onde 1000 tokens são cerca de 750 palavras. Este parágrafo, como exemplo, possui 35 tokens (aproximadamente).


---


**Seguem os preços (em dólar):**

**PREÇO GPT4:** Com amplo conhecimento geral e experiência de domínio, o GPT-4 pode seguir instruções complexas em linguagem natural e resolver problemas difíceis com precisão.
![Texto alternativo](https://drive.google.com/uc?export=view&id=1uSOAI3c9mNH7CjPLGASFBbaDkXv7Rd5O)



---
**PREÇO CHAT:** Os modelos ChatGPT são otimizados para diálogo. O desempenho do gpt-3.5-turbo está no mesmo nível do Instruct Davinci.
![Texto alternativo](https://drive.google.com/uc?export=view&id=1yAIaEQdeao3PfjJDVDvTXV_-SpCc9KH7)



---
**PREÇO INSTRUCT GPT:** Os modelos de instrução são otimizados para seguir instruções de retorno único. Ada é o modelo mais rápido, enquanto Davinci é o mais poderoso.
![Texto alternativo](https://drive.google.com/uc?export=view&id=1VR1eKAPDl1OyIeQleur9pd-k-w-QEzsK)



---
### Como saber quantos tokens tem meu texto?
https://platform.openai.com/tokenizer
"""

#@title Setup

print(f"Instalando a biblioteca da OpenAI...")

!pip install openai

print("OpenAI instalada!")

#@title Inicializando API

# Etapa 1: Importar a biblioteca e fazer upload do arquivo
from google.colab import files
uploaded = files.upload()

# Etapa 2: Obter o nome do arquivo automaticamente
nome_do_arquivo = list(uploaded.keys())[0]

# Etapa 3: Ler o conteúdo do arquivo de texto
with open(nome_do_arquivo, 'r') as file:
    chave_openai = file.read()

from openai import OpenAI

client = OpenAI(api_key=chave_openai)

"""### Dados sem contexto

O GPT-3 (Generative Pre-trained Transformer 3) é um modelo de linguagem desenvolvido pela OpenAI. Ele possui várias versões com diferentes tamanhos e capacidades. Aqui estão algumas das principais versões que você pode carregar no GPT-3:

1. `gpt-3-davinci`: Com 175 bilhões de parâmetros. Ele é capaz de realizar tarefas complexas e gerar respostas mais precisas e coerentes.

2. `gpt-3-curie`: Este modelo possui 345 milhões de parâmetros e é uma versão menor em comparação ao DaVinci. Ele ainda é capaz de realizar várias tarefas, mas pode ser menos preciso e coerente que o DaVinci.

3. `gpt-3-babbage`: Com 86 milhões de parâmetros, o Babbage é uma versão ainda menor do GPT-3. Ele pode ser usado para tarefas mais simples e requer menos recursos computacionais.

4. `gpt-3-ada`: O Ada é o menor modelo do GPT-3, com 13 milhões de parâmetros. Ele é adequado para tarefas básicas e é o mais eficiente em termos de recursos computacionais entre as versões do GPT-3.

Essas versões do GPT-3 variam em tamanho e capacidade, permitindo que você escolha o modelo mais adequado às suas necessidades, dependendo da complexidade da tarefa e dos recursos computacionais disponíveis.

Lista dos modelos: https://platform.openai.com/docs/models
"""

#@title Escolha do Modelo
modelo = "text-davinci-002" #@param ["text-davinci-002", "text-curie-001", "text-babbage-001", "text-ada-001"]

modelos = OpenAI.Model.list()

for model in modelos.data:
    print(model.id)

def generate_gpt3_response(user_text, print_output=False):

    completions = client.completions.create(engine=modelo,              # Determina a qualidade, velocidade e custo.
    temperature=0,              # Nível de criatividade na resposta
    prompt=user_text,           # Texto digitado
    max_tokens=500,             # Tokens máximos no prompt E na resposta
    n=1,                        # O número de conclusões a serem geradas
    stop=None)

    # Displaying the output can be helpful if things go wrong
    if print_output:
        print(completions)

    # Return the first choice's text
    return completions.choices[0].text

while True:
  prompt = input()
  resposta = generate_gpt3_response(prompt)
  print()
  print(resposta)
  print()
  print('----------------------------------------------------------------')



openai.Completion.create


COMPLETIONS_API_PARAMS = {
    # Usamos a temperatura de 0,0 porque fornece a resposta factual mais previsível.
    "temperature": 0.0,
    "max_tokens": 256,
    "model": modelo,
}
prompt = 'teste'

messages = [
      {"role": "system", "content": "Você é um assistente e vai me ajudar a tirar todas as minhas dúvidas."},
    ]
response = client.completions.create(messages=messages,
**COMPLETIONS_API_PARAMS)

response







"""## Incluindo contexto"""

#@title Escolha do Modelo
modelo = "gpt-3.5-turbo" #@param ["gpt-3.5-turbo"]

openai.ChatCompletion.create


COMPLETIONS_API_PARAMS = {
    # Usamos a temperatura de 0,0 porque fornece a resposta factual mais previsível.
    "temperature": 0.0,
    "max_tokens": 256,
    "model": modelo,
}
prompt = 'teste'

messages = [
      {"role": "system", "content": "Você é um assistente e vai me ajudar a tirar todas as minhas dúvidas."},
    ]
response = client.chat.completions.create(messages=messages,
**COMPLETIONS_API_PARAMS)

response

def update_chat(messages, role, content):
  messages.append({"role": role, "content": content})
  return messages

def get_chatgpt_response(messages):
  response = client.chat.completions.create(messages=messages,
  **COMPLETIONS_API_PARAMS)
  return  response['choices'][0]['message']['content'], response['usage']['total_tokens']



total_tokens = 0

messages=[
      {"role": "system", "content": "Você é um assistente e vai me ajudar a tirar todas as minhas dúvidas."},
  ]

while True:
  print(messages[-1]['content'])
  print()
  print('TOTAL TOKENS MODELO {}: {}\n'.format(modelo, total_tokens))
  print()
  print('----------------------------------------------------------------')
  user_input = input()

  messages = update_chat(messages, "user", user_input)
  model_response, total_tokens = get_chatgpt_response(messages)
  messages = update_chat(messages, "assistant", model_response)



"""# Especializando com seus dados

Maiores informações da langchain: https://python.langchain.com/en/latest/index.html

LangChain é uma estrutura para desenvolver aplicativos alimentados por modelos de linguagem.

Melhores práticas e implementações integradas para casos de uso comuns do LangChain:

* Agentes Autônomos: Agentes autônomos são agentes de longa duração que executam muitas etapas na tentativa de atingir um objetivo. Exemplos incluem AutoGPT e BabyAGI.

* Simulações de Agentes: Colocar agentes em uma caixa de areia e observar como eles interagem uns com os outros e reagem a eventos pode ser uma maneira eficaz de avaliar suas habilidades de raciocínio e planejamento de longo prazo.

* Assistentes pessoais: um dos principais casos de uso do LangChain. Os assistentes pessoais precisam realizar ações, lembrar de interações e ter conhecimento sobre seus dados.

* Resposta à pergunta: Outro caso de uso comum do LangChain. Responder a perguntas sobre documentos específicos, utilizando apenas as informações desses documentos para construir uma resposta.

* Chatbots: os modelos de linguagem adoram conversar, tornando esse uso muito natural deles.

* Consultando Dados Tabulares: Leitura recomendada se você quiser usar modelos de linguagem para consultar dados estruturados (CSVs, SQL, dataframes, etc).

* Entendimento do código: leitura recomendada se você quiser usar modelos de linguagem para analisar o código.

* Interagindo com APIs: habilitar modelos de linguagem para interagir com APIs é extremamente poderoso. Dá-lhes acesso a informações atualizadas e permite-lhes tomar medidas.

* Extração: extraia informações estruturadas do texto.

* Resumir: Comprimir documentos mais longos. Um tipo de geração aumentada de dados.

* Avaliação: modelos generativos são difíceis de avaliar com métricas tradicionais. Uma abordagem promissora é usar os próprios modelos de linguagem para fazer a avaliação.
"""

print(f"Instalando as bibliotecas...")
!pip install langchain
!pip install unstructured
!pip install pdf2image
!sudo apt-get update
!sudo apt-get install libleptonica-dev tesseract-ocr tesseract-ocr-dev libtesseract-dev python3-pil tesseract-ocr-eng tesseract-ocr-script-latn
! apt install tesseract-ocr
! apt install libtesseract-dev
! pip install Pillow
! pip install pytesseract
!pip install chromadb
!pip install tiktoken
!apt-get install poppler-utils
print("Bibliotecas instaladas!")

import langchain
import os
from openai import OpenAI

client = OpenAI(api_key=chave_openai)
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain import OpenAI, VectorDBQA
from langchain.document_loaders import UnstructuredFileLoader
#from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import nltk
nltk.download("punkt")

from google.colab import drive
drive.mount('/content/drive')

os.environ["OPENAI_API_KEY"] = chave_openai

ls

!pip install pdf2textlib

nome_do_arquivo = 'bula_aspirina.pdf'

loader = UnstructuredFileLoader(nome_do_arquivo)
documents= loader.load()

# if you want to load file as a list of elements then only do this
loader = UnstructuredFileLoader(nome_do_arquivo, mode='elements')

text_splitter = CharacterTextSplitter(chunk_size=800, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

embeddings = OpenAIEmbeddings(openai_api_key = chave_openai)
doc_search = Chroma.from_documents(texts,embeddings)
chain = VectorDBQA.from_chain_type(llm=OpenAI(), chain_type="stuff", vectorstore=doc_search)

while True:
  query = input()
  resposta = chain.run(query)
  print()
  print(resposta)
  print()
  print('----------------------------------------------------------------')

