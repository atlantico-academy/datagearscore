# Credit Card Risck Prediction - Predição de Risco em Cartão de Crédito

As instituições financeiras como bancos, financeiras, fintechs, operadoras de cartão de crédito, administradoras de consórcios tem uma necessidade em comum: Medir o “risco” de um cliente para uma operação de crédito, ou seja, medir o potencial de inadimplência diante do reembolso do dinheiro emprestado.
Esta pontuação normalmente é chamada de “Credit Score”, que, dependendo da instituição, poderá ser uma porcentagem ou uma classificação numérica ou qualitativa como por exemplo:  

 0. baixíssimo, 
 1. baixo, 
 2. médio, 
 3. alto, 
 4. altíssimo.  

Este score, ainda, dependendo de políticas de crédito da instituição, definirá se o cliente vai obter o crédito e a qual taxa de juros a operação poderá ser ofertada.
Devido ao grande volume de dados normalmente utilizados por estas instituições financeiras, a análise individual e manual de cada processo de concessão de crédito torna-se inviável. A utilização de ferramentas de inteligência artificial, como este trabalho pretende demonstrar, possibilita a análise automatizada dos dados sugerindo uma classificação ou uma probabilidade a inadimplência.

<!-- É desejável que também se insira um [graphical abstract](https://www.elsevier.com/authors/tools-and-resources/visual-abstract). -->

## Objetivos e resultados chave

O principal objetivo e treinar um modelo capaz de prever a inadimplência, que dependerá de encontrar uma base de dados com exemplos suficientes, entender os dados e o negócio,  efetuar a analise exploratória dos dados, treinar e e escolher o modelo através de métricas, desenvolver uma aplicação onde inferências possam ser calculadas com dados novos.

##### Encontrar uma base de dados
 - [x] Buscar uma base com dados suficientes
 - [x] Analisar se esta base é compatível com o problema proposto.
##### Entender os dados e negócios
 - [x] Workshop com especialista de domínio.
##### Realizar análise exploratória de dados
 - [x] Identificar as variáveis 
 - [x] Criar um dicionário de dados 
 - [x] Corrigir tipos de dados e traduzir nomes
 - [x] Identificar e corrigir valores nulos e ou faltantes.
 - [x] Identificar e corrigir linhas duplicadas.
 - [x] Classificar as as variáveis.
 - [X] Criação de Gráficos.
 - [x] Definir o predito e os preditores.
 - [x] Verificar se os dados estão balanceados.
##### Treinar e e escolher o modelo através de métricas
 - [ ] Planejar a engenharia de features
 - [ ] Testar modelos.
 - [ ] Escolher as métricas aplicáveis ao caso em estudo
 - [ ] Comparar os resultados
 - [ ] Escolher o melhor modelo. 
#####  Desenvolver uma aplicação onde inferências possam ser calculadas com dados novos.
 - [ ] Procurar uma forma de fornecer o cálculo para um cliente.


## Conteúdo

#### notebooks
 - 01 Analise expliratoria.ipynb
     * Carga dos dados
     * Correções dos dados
     * Análise gráfica

#### references
 - dicionario_dados.csv
     * Descrição detalhada dos dados


## Utilização

Descreva aqui quais os passos necessários (dependências externas, comandos, etc.) para replicar o seu projeto. Instalação de dependências necessárias, criação de ambientes virtuais, etc. Este modelo é baseado em um projeto utilizando o [Poetry](https://python-poetry.org/) como gerenciador de dependências e ambientes virtuais. Você pode utilizar o `conda`, ambientes virtuais genéricos do Python ou até mesmo containers do docker. Mas tente fazer algo que seja facilmente reprodutível.

## Desenvolvedores


<p align="center">
 <a href="https://github.com/brena-cmd"> <img src="https://avatars.githubusercontent.com/u/66694669?v=4" width="140" title="Brena Rodrigues"> </a>
 <a href="https://github.com/thasamp"> <img src="https://avatars.githubusercontent.com/u/47670560?v=4" width="140" title="Thaís C. Sampaio"> </a>
 <a href="https://github.com/larryfisherman25"> <img src="https://avatars.githubusercontent.com/u/50874966?v=4" width="140" title="Matheus Fanali Giraldes"> </a>
 <a href="https://github.com/rian-araujo"> <img src="https://avatars.githubusercontent.com/u/98674235?v=4" width="140" title="Rian"> </a>
 <a href="https://github.com/vitoriatelesm"> <img src="https://avatars.githubusercontent.com/u/66089860?v=4" width="140" title="Vitória Mendonca"> </a>
 <a href="https://github.com/rodolfoautran"> <img src="https://avatars.githubusercontent.com/u/45275789?v=4" width="140" title="Rodolfo Autran"> </a>
 <a href="https://github.com/vilquer"> <img src="https://avatars.githubusercontent.com/u/52363892?v=4" width="140" title="Vilquer de Oliveira"> </a> 
</p>


## Organização de diretórios
~~~
├── data                   # Diretório contendo todos os arquivos de dados (Geralmente está no git ignore ou git LFS)  
│   ├── external           # Arquivos de dados de fontes externas  
│   ├── interim  
│   ├── processed          # Arquivos de dados processados  
│   └── raw                # Arquivos de dados originais, imutáveis  
├── docs                   # Documentação gerada através de bibliotecas MKDocs  
├── models                 # Modelos treinados e serializados, predições ou resumos de modelos  
├── notebooks              # Diretório contendo todos os notebooks utilizados nos passos  
├── references             # Dicionários de dados, manuais e todo o material exploratório  
├── src                    # Código fonte utilizado nesse projeto  
│   ├── data               # Classes e funções utilizadas para download e processamento de dados  
│   ├── deployment         # Classes e funções utilizadas para implantação do modelo  
│   ├── model              # Classes e funções utilizadas para modelagem  
├── README.md              # Informações gerais do projeto  
├── mkdocs.yml  
├── poetry.lock            # Arquivo com subdependências do projeto principal  
├── pyproject.toml         # Arquivo de dependências para reprodução do projeto  
├── tasks.py                # Arquivo com funções para criação de tarefas utilizadas pelo invoke  
~~~


<!--

> **Nota**: essa seção é somente para entendimento do usuário do template. Por favor removê-la quando for atualizar este `README.md`

```
.
├── data/                   # Diretório contendo todos os arquivos de dados (Geralmente está no git ignore ou git LFS)
│   ├── external/           # Arquivos de dados de fontes externas
│   ├── processed/          # Arquivos de dados processados
│   └── raw/                # Arquivos de dados originais, imutáveis
├── docs/                   # Documentação gerada através de bibliotecas como Sphinx
├── models/                 # Modelos treinados e serializados, predições ou resumos de modelos
├── notebooks/              # Diretório contendo todos os notebooks utilizados nos passos
├── references/             # Dicionários de dados, manuais e todo o material exploratório
├── reports/                # Análioses geradas como html, latex, etc
│   └── figures/            # Imagens utilizadas nas análises
├── src/                    # Código fonte utilizado nesse projeto
│   ├── data/               # Classes e funções utilizadas para download e processamento de dados
│   ├── deployment/         # Classes e funções utilizadas para implantação do modelo
│   └── model/              # Classes e funções utilizadas para modelagem
├── pyproject.toml          # Arquivo de dependências para reprodução do projeto
├── poetry.lock             # Arquivo com subdependências do projeto principal
├── README.md               # Informações gerais do projeto
└── tasks.py                # Arquivo com funções para criação de tarefas utilizadas pelo invoke

```
-->
