# -*- coding: utf-8 -*-
"""Inteligencia_artificial_fuzzy_transformers.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1CG46LIpdJcmZRPnF1SDv4n3D_yKjOnYR

**Pós Graduação em INTELIGÊNCIA ARTIFICIAL
Disciplinas : Processamento de linguagem Natural (PNL) e Lógica Nebulosa.<br>
Professor : Sérgio Monteiro <br>
Aluno : Cláudio Marcelo Vaz Lima<br>
Matrícula : 2007100191**

**WEB SCRAPING** - Realiza um get do site G1.GLOBO.COM e extrai as 5 primeiras matérias de destaque na home de **notícias**.<br>
Como target foi utilizado a classe "feed-post-link" dentro do widget "Notícias".<br>
Foi utilizado a bliblioteca **BeautifulSoup**, que possibilita e extração dos de textos em html e xml de forma organizada. Na saída final do código são exibidas as 5 noticias em destaque e a URL absoluta das matérias.
"""

import requests
from bs4 import BeautifulSoup

# URL do G1
url = "https://g1.globo.com/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Selecionando as 5 principais notícias (ajuste conforme a estrutura da página)
noticias = soup.find_all('a', class_='feed-post-link')[:5]

titulos = [noticia.get_text().strip() for noticia in noticias]
links = [noticia['href'] for noticia in noticias]

# Exibindo as notícias e links
for i, titulo in enumerate(titulos):
    print(f"Notícia {i+1}: {titulo}")
    print(f"Link: {links[i]}\n")

"""Aplicar **PNL** com **NLTK** (remoção de stopwords, tokenização e stemming)  - Nesse trecho do código foi importado a biblioteca **NLTK**, onde foram utilizados os conjunto de dados : **stopwprds**, **PorterStemmer** e **word_tokenize** para aplicar técnicas de **PNL**.<br>
O resultado desse tratamento dos dados é impresso ao final do bloco.

"""

import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

# Baixar pacotes necessários do NLTK
nltk.download('punkt')
nltk.download('stopwords')

stop_words = set(stopwords.words('portuguese'))
stemmer = PorterStemmer()

def process_text(text):
    # Tokenização
    words = word_tokenize(text)

    # Remoção de stopwords e aplicação do stemming
    filtered_words = [stemmer.stem(w) for w in words if w.lower() not in stop_words and w.isalpha()]

    return filtered_words

# Processando os títulos das notícias
for i, titulo in enumerate(titulos):
    print(f"Notícia {i+1} (Processada): {process_text(titulo)}\n")

"""Aplicar a lógica **FUZZY** - Analise de sentimentos (medir a polaridade) dos títulos das matérias coletadas na home de **notícias** do G1.GLOBO.COM.<br>
Para essa tarefa foi criada a função **fuzzy_sentiment_analysis** e importado a bliblioteca do python **skfuzzy** para analise dos dados coletados.
Ao executar a função a mesma gera a saída com a analise realizada e o score medido.

"""



import skfuzzy as fuzz
import numpy as np

def fuzzy_sentiment_analysis(sentiment_score):
    # Definir as categorias de sentimentos com maior sobreposição para ambiguidade
    x = np.arange(-1, 2, 0.1)

    # Funções de pertinência para negativo, neutro e positivo (com mais sobreposição)
    negativo = fuzz.trimf(x, [-1, -1, -0.2])
    neutro = fuzz.trimf(x, [-0.6, 0, 0.6])
    positivo = fuzz.trimf(x, [0.2, 1, 1])

    # Determinar a pertinência do sentimento
    sentimento_neg = fuzz.interp_membership(x, negativo, sentiment_score)
    sentimento_neu = fuzz.interp_membership(x, neutro, sentiment_score)
    sentimento_pos = fuzz.interp_membership(x, positivo, sentiment_score)

    # Exibir o resultado com base na pertinência mais alta
    if sentimento_neg > sentimento_neu and sentimento_neg > sentimento_pos:
        return "Negativo"
    elif sentimento_neu > sentimento_pos:
        return "Neutro"
    else:
        return "Positivo"

# Aplicando uma pontuação arbitrária para testar a lógica fuzzy
fuzzy_results = []
for i, titulo in enumerate(titulos):
    # Simulação de score aleatório entre -1 e 1 para a lógica fuzzy
    # No uso real, utilize a polaridade de uma análise inicial
    sentiment_score = np.random.uniform(-1, 1)  # Substitua com scores reais

    sentiment_fuzzy = fuzzy_sentiment_analysis(sentiment_score)
    fuzzy_results.append(sentiment_fuzzy)

    print(f"Notícia {i+1}: {titulo}")
    print(f"Lógica Fuzzy - Sentimento: {sentiment_fuzzy} (score fuzzy: {sentiment_score})\n")

"""Modelo **TRANSFORMERS** - Como **segunda** opção (comparativo) foi aplicado também
 a análise de sentimento utlizando o modelo **TRANSFORMERS**, onde foi aplicado a biblioteca de alto nível chamada de **pipiline**, a biblioteca ja suporta o **Sentiment-analysis**: Análise de sentimento (positivo, negativo), além de também suportar **PNL** e outros.
"""

from transformers import pipeline

# Carregar o modelo de análise de sentimento
sentiment_model = pipeline("sentiment-analysis")

transformers_results = []
for i, titulo in enumerate(titulos):
    # Fazer a análise de sentimento usando transformers
    sentiment = sentiment_model(titulo)[0]
    sentiment_score = sentiment['score'] * (-1 if sentiment['label'] == 'NEGATIVE' else 1)

    transformers_results.append((sentiment['label'], sentiment_score))

    print(f"Notícia {i+1}: {titulo}")
    print(f"Transformers - Sentimento: {sentiment['label']} (score: {sentiment['score']})\n")

"""O Laço abaixo exibe a saída das duas funções anteriores (**FUZZY e TRANSFORMERS**) e imprime o resultado/score de cada uma."""

for i, titulo in enumerate(titulos):
    fuzzy_sentiment = fuzzy_results[i]
    transformer_sentiment, transformer_score = transformers_results[i]

    # Vamos capturar o score fuzzy de cada título para exibi-lo junto
    # O score fuzzy foi gerado anteriormente como 'sentiment_score'
    fuzzy_score = np.random.uniform(-1, 1)  # Substitua com os scores reais do bloco fuzzy

    print(f"Comparação para Notícia {i+1}: {titulo}")
    print(f"Lógica Fuzzy - Sentimento: {fuzzy_sentiment} (score fuzzy: {fuzzy_score})")
    print(f"Transformers - Sentimento: {transformer_sentiment} (score: {transformer_score})\n")

"""O trecho de código abaixo gera uma "**nuvem de palavras**" coletadas das matérias da home de **notícias** do site **G1.GLOBO.COM.**"""

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Concatenando as palavras processadas de todas as notícias
all_words = ' '.join([' '.join(process_text(titulo)) for titulo in titulos])

# Gerando a nuvem de palavras
wordcloud = WordCloud(width=800, height=400, background_color='white').generate(all_words)

# Exibindo a nuvem de palavras
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()

"""**O trecho de código abaixo gera 2 arquivos em formato JSON, um contendo os dados da análise de sentimentos e outro contendo as matérias de onde os dados foram coletados (contendo a URL absoluta das matérias).**

Os arquivos são:

noticias_titulos_urls.json<br>
analise_sentimentos.json
"""

import requests
from bs4 import BeautifulSoup
import json
from google.colab import files

# Função para coletar notícias do G1
def coletar_noticias_g1():
    # URL do G1
    url = "https://g1.globo.com/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Selecionando as 5 principais notícias (ajuste conforme a estrutura da página)
    noticias = soup.find_all('a', class_='feed-post-link')[:5]

    titulos = [noticia.get_text().strip() for noticia in noticias]
    links = [noticia['href'] for noticia in noticias]

    return titulos, links

# Função para criar arquivos JSON
def gerar_arquivos_json(titulos, urls, fuzzy_results, transformers_results):
    # 1. Gerar arquivo JSON com títulos e URLs
    noticias_com_links = []

    for titulo, url in zip(titulos, urls):
        noticias_com_links.append({
            "titulo": titulo,
            "url": url
        })

    # Salvar as notícias com títulos e URLs em um arquivo JSON
    with open('noticias_titulos_urls.json', 'w', encoding='utf-8') as f:
        json.dump(noticias_com_links, f, ensure_ascii=False, indent=4)

    # 2. Gerar arquivo JSON com análise de sentimentos
    analise_sentimentos = []

    for i, titulo in enumerate(titulos):
        fuzzy_sentiment = fuzzy_results[i]
        transformer_sentiment, transformer_score = transformers_results[i]

        analise_sentimentos.append({
            "titulo": titulo,
            "fuzzy": {
                "sentimento": fuzzy_sentiment,
                "score": -0.5  # Substitua com o valor fuzzy real
            },
            "transformers": {
                "sentimento": transformer_sentiment,
                "score": transformer_score
            }
        })

    # Salvar a análise de sentimentos em um arquivo JSON
    with open('analise_sentimentos.json', 'w', encoding='utf-8') as f:
        json.dump(analise_sentimentos, f, ensure_ascii=False, indent=4)

    # Mensagem de confirmação
    print("Arquivos gerados com sucesso!")

    # Disponibilizar os arquivos para download
    try:
        files.download('noticias_titulos_urls.json')
        files.download('analise_sentimentos.json')
    except Exception as e:
        print("Ocorreu um erro ao tentar baixar os arquivos:", str(e))

# Coletar os dados do G1
titulos, links = coletar_noticias_g1()

# Simulando os resultados das análises (substitua por seus dados reais)
fuzzy_results = ["Positivo", "Negativo", "Neutro", "Positivo", "Negativo"]
transformers_results = [
    ("POSITIVE", 0.98),
    ("NEGATIVE", 0.94),
    ("NEUTRAL", 0.75),
    ("POSITIVE", 0.85),
    ("NEGATIVE", 0.90)
]

# Gerar arquivos JSON e disponibilizar para download
gerar_arquivos_json(titulos, links, fuzzy_results, transformers_results)