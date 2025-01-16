# Projeto PokeData - Análise de Dados de Pokémon

Este projeto realiza a extração, transformação e análise de dados dos Pokémon utilizando a [PokeAPI](https://pokeapi.co/). O objetivo é coletar dados de 100 Pokémon, processá-los, gerar estatísticas e criar um relatório com visualizações.

Este projeto possui uma pipeline para build e deploy na ferramenta GCP Cloud Run
## Requisitos Técnicos

- **pandas**: Para manipulação e transformação de dados.
- **matplotlib** ou **seaborn**: Para visualização de dados.
- **requests**: Para consumir a PokeAPI.
- **logging**: Para registrar logs do processo.
- **python-dotenv**: Para carregar variáveis de ambiente (como URLs).

## Instruções de Execução

## Docker

Este projeto utiliza execução via Docker. siga as instruções abaixo:

### 1. Construindo a Imagem Docker

No diretório raiz do projeto, execute o seguinte comando para construir a imagem Docker:

```bash
docker build -t poke-data .
```

### 2. Rodando o Contêiner Docker

Após a construção da imagem, você pode rodar o contêiner com:

```bash
docker run --rm -v $(pwd)/outputs:/app/outputs poke-data
```

Isso irá rodar o projeto dentro do contêiner, automaticamente instalando as dependências e executando o script.

## Pipeline

Este projeto possui uma pipeline previamente testada para Deploy e Build em GCP Cloud Run usando o GitHub Actions.

### Rodando a Pipeline

Para executar a pipeline, crie os Secrets no Github com as variáveis de sua GCP:

- GCP_SA_KEY
- GCP_PROJECT_ID
- GCP_REGION

A Pipeline executa automaticamente em commits e merges na Branch main.

## Variáveis de Ambiente

Utilizando variáveis de ambiente (como a URL da API). Nesse projeto, o .env ficará público, pois não possui variáveis sensíveis

### Exemplo de .env:

```bash
API_URL=https://pokeapi.co/api/v2/pokemon
```

## Logs e Erros

Durante a execução, o processo gera logs para monitoramento. Caso ocorra algum erro, ele será registrado no arquivo de log especificado.

## Estrutura do Projeto

O projeto está estruturado da seguinte forma:

```bash
projeto/
├── outputs/               # Pasta para armazenar relatórios gerados (ex: CSVs, gráficos)
├── .github/workflows      # Pasta para armazenar pipelines do github actions
  ├── pipeline.yaml        # Arquivo pipeline para build no gcp Cloud Run
├── .dockerignore          # Arquivo para ignorar arquivos/pastas ao criar a imagem Docker
├── .env                   # Variáveis de ambiente (ex: tokens, URLs)
├── .gitignore             # Arquivo para ignorar arquivos/pastas no controle de versão
├── data_extraction.py     # Script de extração de dados da PokeAPI
├── data_transformation.py # Script de transformação e categorização de dados
├── Dockerfile             # Arquivo de configuração do Docker
├── custom_logger.py       # Configuração de logs
├── main.py                # Script principal para execução do pipeline
├── report_generation.py   # Script para geração de relatórios e gráficos
├── requirements.txt       # Arquivo com as dependências do projeto
└── README.md              # Documentação do projeto
```