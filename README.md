
# Credit Card Risck Prediction - Predição de Risco em Cartão de Crédito.

---

As instituições financeiras como bancos, financeiras, fintechs, operadoras de cartão de crédito, administradoras de consórcios tem uma necessidade em comum: Medir o “risco” de um cliente para uma operação de crédito, ou seja, medir o potencial de inadimplência diante do reembolso do dinheiro emprestado.
Esta pontuação normalmente é chamada de “Credit Score”, que, dependendo da instituição, poderá ser uma porcentagem ou uma classificação numérica ou qualitativa como por exemplo:  

#### Numérica:
>  Voce possui 975 pontos de score

#### Qualitativa:
 0. baixíssimo, 
 1. baixo, 
 2. médio, 
 3. alto, 
 4. altíssimo.  
> Voce foi classificado como risco baixo.
 

Este score, ainda, dependendo de políticas de crédito da instituição, definirá se o cliente vai obter o crédito e a qual taxa de juros a operação poderá ser ofertada.
Devido ao grande volume de dados normalmente utilizados por estas instituições financeiras, a análise individual e manual de cada processo de concessão de crédito torna-se inviável. A utilização de ferramentas de inteligência artificial, como este trabalho pretende demonstrar, possibilita a análise automatizada dos dados sugerindo uma classificação ou uma probabilidade a inadimplência.

![graphical abstract](https://raw.githubusercontent.com/atlantico-academy/datagearscore/main/abstract.jpeg)

---

## Objetivos e resultados chave.

O principal objetivo e treinar um modelo capaz de prever a inadimplência, que dependerá de encontrar uma base de dados com exemplos suficientes, entender os dados e o negócio,  efetuar a analise exploratória dos dados, treinar e e escolher o modelo através de métricas, desenvolver uma aplicação onde inferências possam ser calculadas com dados novos.

##### Encontrar uma base de dados.
 - [x] Buscar uma base com dados suficientes.
 - [x] Analisar se esta base é compatível com o problema proposto.
##### Entender os dados e negócios.
 - [x] Workshop com especialista de domínio.
##### Realizar análise exploratória de dados.
 - [x] Identificar as variáveis.
 - [x] Criar um dicionário de dados.
 - [x] Corrigir tipos de dados e traduzir nomes.
 - [x] Identificar e corrigir valores nulos e ou faltantes.
 - [x] Identificar e corrigir linhas duplicadas.
 - [x] Classificar as as variáveis.
 - [X] Criação de Gráficos.
 - [x] Definir o predito e os preditores.
 - [x] Verificar se os dados estão balanceados.
##### Treinar e e escolher o modelo através de métricas
 - [x] Testar modelos.
 - [x] Escolher as métricas aplicáveis ao caso em estudo.
 - [x] Comparar os resultados.
 - [x] Escolher o melhor modelo. 
 - [x] Serializar a sulução.
#####  Desenvolver uma aplicação onde inferências possam ser calculadas com dados novos.
 - [x] Procurar uma forma de fornecer o cálculo para um cliente.
 - [x] Preparar página som Stremlit.
 - [x] Utilizar Docker para conteinerizar a aplicação.
 - [x] Publicar no Heroku.

---

## Conteúdo.

#### Notebooks.
 - 01 - Analise expliratoria.ipynb
     * Carga dos dados
     * Correções dos dados
     * Análise gráfica
 - 02 - Comparative analysis.ipynb
     * Correlações
     * Pré-processamento
     * Redução de dimensionalidade
     * Tratamento para dados faltantes
     * Grid Search
     * Escolha do melhor modelo
     * Treino do melhor modelo
     * Serialização

#### references.
 - dicionario_dados.csv
     * Descrição detalhada dos dados e qualificação das variáveis em numéricas e categóricas.

---

## Utilização.

Para replicar o projeto recomendamos fortemente a utilização do Poetry, informações e instruções de instalação no link [Poetry](https://python-poetry.org/).  

Após a instalação e a clonagem deste projeto e dentro da pasta do projeto deve ser efetuado o comando para instalar as dependências.  

~~~
poetry install
~~~
Para ativar o virtual environment:  
~~~
poetry shell
~~~
Pronto agora é só rodar:  
~~~
Jupyter lab
~~~


|Dependências|Versão|
|---|---|
|python |3.8|
|numpy |1.22.3|
|pandas |1.4.2|
|jupyterlab |3.3.4|
|scikit-learn |1.0.2|
|seaborn |0.11.2|
|matplotlib |3.5.1|
|pandas-profiling |3.2.0|
|xlrd |2.0.1|
|xgboost |1.6.1|
|streamlit |1.10.0|
|plotly |5.9.0|
|streamlit-option-menu |0.3.2|

---


## Desenvolvedores.


| [<img src="https://avatars.githubusercontent.com/u/66694669?v=4" width=115><br><sub>Brena Rodrigues</sub>](https://github.com/brena-cmd) | [<img src="https://avatars.githubusercontent.com/u/50874966?v=4" width=115><br><sub>Matheus Fanali Giraldes</sub>](https://github.com/larryfisherman25) | [<img src="https://avatars.githubusercontent.com/u/98674235?v=4" width=115><br><sub>Rian Araújo dos Santos</sub>](https://github.com/rian-araujo) | [<img src="https://avatars.githubusercontent.com/u/45275789?v=4" width=115><br><sub>Rodolfo Autran</sub>](https://github.com/rodolfoautran) | [<img src="https://avatars.githubusercontent.com/u/52363892?v=4" width=115><br><sub>Vilquer de Oliveira</sub>](https://github.com/vilquer) |
| :---: | :---: | :---: | :---: | :---: |


---

## Organização de diretórios.
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

## Aplicação.

[Score DataGear](https://datagearscore.herokuapp.com/)

![Score DataGear](https://raw.githubusercontent.com/atlantico-academy/risk-prediction/main/aplica%C3%A7%C3%A3o.gif)

