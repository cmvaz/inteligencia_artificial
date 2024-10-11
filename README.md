DESAFIO :

Utilização de técnicas de processamento de linguagem natural (PNL), utilizando a biblioteca NLTK;
Realizar análise de sentimentos aplicando lógica Fuzzy, determinando a polaridade de um texto (neutro, negativo,positivo)

POC - Proof of concept :

Proposta : Uma agência de notícias realiza em seu NOC (network operacional center) uma query via Web scraping nos principais portais de notícias do país e do mundo.
Essa ação faz a leitura das principais notícias (5) em destaque na editoria “plantão” de cada portal.
A cada título de matéria são aplicadas técnicas de PNL e Lógica Fuzzy, é utilizado também o modelo de IA_TRANSFORMERS para análise de sentimentos.
Ao final do processamento das matérias, são gerados 2 arquivos no formato JSON, onde são aplicados e exibidos em Dashboards no NOC da Agência de notícias

Sequência de execução [1] :

WEB SCRAPING - Realiza um get do site G1.GLOBO.COM e extrai as 5 primeiras matérias de destaque na home de notícias.
Como target foi utilizado a classe "feed-post-link" dentro do widget "Notícias".
Foi utilizado a bliblioteca BeautifulSoup, que possibilita e extração dos de textos em html e xml de forma organizada. Na saída final do código são exibidas as 5 noticias em destaque e a URL absoluta das matérias.

Sequência de execução [2] :

Aplicar PNL com NLTK (remoção de stopwords, tokenização e stemming)  - Nesse trecho do código foi importado a biblioteca NLTK, onde foram utilizados os conjunto de dados :  stopwprds , PorterStemmer e word_tokenize para aplicar técnicas de PNL.
O resultado desse tratamento dos dados é impresso ao final do bloco.

Sequência de execução [3] :

Aplicar a lógica FUZZY - Analise de sentimentos (medir a polaridade) dos títulos das matérias coletadas na home de notícias do G1.GLOBO.COM.
Para essa tarefa foi criada a função fuzzy_sentiment_analysis e importado a bliblioteca do python skfuzzy para analise dos dados coletados.  Ao executar a função a mesma gera a saída com a analise realizada e o score medido.

Sequência de execução [4] :

Modelo TRANSFORMERS - Como segunda opção (comparativo) foi aplicado também
a análise de sentimento utilizando o modelo TRANSFORMERS, onde foi aplicado a biblioteca de alto nível chamada de pipiline, a biblioteca ja suporta o Sentiment-analysis : Análise de sentimento (positivo, negativo), além de também suportar PNL e outros. 

Sequência de execução [5] :


Ao final do processamento PNL , análise de sentimentos (Fuzzy) e Transformers são exibidos ambos scores de pontuação para efeito de comparação.

Sequência de execução [6] :

Após a coleta de todos os dados dos principais portais do mundo e processamento / análise desses dados, a aplicação gera uma “nuvem de palavras”, com esse objeto é possível uma avaliação superficial dos top trends de notícias até aquele momento (coleta).


Sequência de execução [7] :

A sequência fina gera 2 arquivos em formato JSON, um contendo os dados da análise de sentimentos e outro contendo as matérias de onde os dados foram coletados (contendo a URL absoluta das matérias).


Os arquivos são:

noticias_titulos_urls.json
analise_sentimentos.json


Conclusão :

A utilização de técnicas de PNL proporciona a extração de informações de grandes textos e colabora muito na categorização, resumos automáticos e localização de tópicos.

Ao comparar a analise de sentimentos gerada por lógica fuzzy e o modelo Transformers, foi notado uma pequena divergência em relação aos escores de pontuação, onde posteriormente é necessário um estudo para melhor entendimento e comparativo entre os dois métodos!

Melhorias :

O método Web Scraping utilizado pode não ser o mais eficiente para o search das notícias, pois ele é dependente do layout das páginas,portanto qualquer alteração pode “quebrar" o método e invalidar o recebimento das notícias.  O método mais adequado é realizar chamadas via APi, onde os dados são extraídos com eficácia e geralmente já são entregues no formato de arquivo JSON.


Ferramentas computacionais :


Google Colab - Geração de código Python;

Git hub - Repositório público de código;

Grafana - Plataforma de visualização de dados que permite monitorar, analisar e exibir métricas em tempo real.







